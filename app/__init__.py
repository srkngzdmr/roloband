"""ROLOBAND Flask uygulama factory."""
import os
from pathlib import Path
from flask import Flask, render_template
from config import config
from app.extensions import db, migrate, login_manager, csrf, ckeditor, cache, limiter


def create_app(config_name=None):
    config_name = config_name or os.getenv("FLASK_ENV", "development")
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(config[config_name])

    Path(app.instance_path).mkdir(parents=True, exist_ok=True)
    for sub in ("videos", "images", "products"):
        (app.config["UPLOAD_FOLDER"] / sub).mkdir(parents=True, exist_ok=True)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    csrf.init_app(app)
    ckeditor.init_app(app)
    cache.init_app(app)
    limiter.init_app(app)

    from app import models  # noqa: F401

    @login_manager.user_loader
    def load_user(user_id):
        return models.AdminUser.query.get(int(user_id))

    from app.blueprints.public.routes import public_bp
    from app.blueprints.admin.routes import admin_bp

    app.register_blueprint(public_bp)
    app.register_blueprint(admin_bp, url_prefix="/admin")

    from app.models import SiteSetting, MenuItem

    @app.context_processor
    def inject_globals():
        try:
            settings = SiteSetting.as_dict()
        except Exception:
            settings = {}
        try:
            main_menu = MenuItem.get_main_menu()
        except Exception:
            main_menu = []
        return {
            "settings": settings,
            "main_menu": main_menu,
            "site_name": app.config["SITE_NAME"],
        }

    @app.errorhandler(404)
    def not_found(e):
        return render_template("errors/404.html"), 404

    @app.errorhandler(500)
    def server_error(e):
        return render_template("errors/500.html"), 500

    from app.utils.cli import register_cli
    register_cli(app)

    return app