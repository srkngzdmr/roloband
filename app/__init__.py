"""
Sivent Platform - Application Factory
"""
import os
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, render_template

from config import config
from app.extensions import db, login_manager, csrf, migrate


def create_app(config_name='production'):
    """Application factory."""
    app = Flask(
        __name__,
        instance_relative_config=True,
        template_folder='templates',
        static_folder='static'
    )

    # --- Konfigürasyon yükle ---
    app.config.from_object(config[config_name])

    # Instance ve upload klasörlerini garanti altına al
    os.makedirs(app.instance_path, exist_ok=True)
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    # --- Extension'ları başlat ---
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)
    migrate.init_app(app, db)

    # --- Blueprint'leri kaydet ---
    from app.main import main_bp
    from app.auth import auth_bp
    from app.admin import admin_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(admin_bp, url_prefix='/admin')

    # --- Error Handler'lar ---
    register_error_handlers(app)

    # --- Context Processors ---
    register_context_processors(app)

    # --- Logging (Production) ---
    if not app.debug and not app.testing:
        configure_logging(app)

    # --- İlk açılışta DB oluştur ---
    with app.app_context():
        try:
            db.create_all()
        except Exception as e:
            app.logger.warning(f'DB create_all hatası: {e}')

    # --- Shell context ---
    @app.shell_context_processor
    def make_shell_context():
        from app.models import User, Sector, SectorMedia, Settings
        return dict(db=db, User=User, Sector=Sector,
                    SectorMedia=SectorMedia, Settings=Settings)

    return app


def register_error_handlers(app):
    @app.errorhandler(404)
    def not_found(error):
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def internal_error(error):
        db.session.rollback()
        return render_template('errors/500.html'), 500

    @app.errorhandler(413)
    def too_large(error):
        return render_template('errors/500.html',
                               message="Dosya boyutu çok büyük (max 25MB)"), 413

    @app.errorhandler(403)
    def forbidden(error):
        return render_template('errors/404.html'), 403


def register_context_processors(app):
    from app.models import Settings, Sector

    @app.context_processor
    def inject_globals():
        try:
            settings = Settings.get_singleton()
            footer_sectors = Sector.query.filter_by(is_active=True).order_by(
                Sector.display_order).limit(10).all()
        except Exception:
            settings = None
            footer_sectors = []
        return dict(
            site_settings=settings,
            footer_sectors=footer_sectors,
            BRAND_NAME=app.config['BRAND_NAME'],
            CONTACT_EMAIL=app.config['CONTACT_EMAIL'],
            CONTACT_PERSON=app.config['CONTACT_PERSON'],
        )


def configure_logging(app):
    log_dir = os.path.join(os.path.dirname(app.instance_path), 'logs')
    try:
        os.makedirs(log_dir, exist_ok=True)
        file_handler = RotatingFileHandler(
            os.path.join(log_dir, 'sivent.log'),
            maxBytes=1024 * 1024 * 5,
            backupCount=5
        )
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
        ))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)
        app.logger.setLevel(logging.INFO)
        app.logger.info('Sivent Platform startup')
    except Exception as e:
        print(f'Logging setup failed: {e}')
