"""Flask CLI komutları: db, seed, create-admin."""
import os
import click
from flask import Flask
from app.extensions import db


def register_cli(app: Flask) -> None:
    @app.cli.command("init-db")
    def init_db():
        """Veritabanı tablolarını oluştur."""
        with app.app_context():
            db.create_all()
            click.echo("✓ Veritabanı tabloları oluşturuldu.")

    @app.cli.command("create-admin")
    @click.option("--email", default=None)
    @click.option("--password", default=None)
    def create_admin(email, password):
        """İlk admin kullanıcısını oluştur."""
        from app.models import AdminUser
        email = email or os.getenv("ADMIN_EMAIL", "admin@roloband.com")
        password = password or os.getenv("ADMIN_PASSWORD", "ChangeMe!2026")

        if AdminUser.query.filter_by(email=email).first():
            click.echo(f"⚠ {email} zaten var.")
            return

        user = AdminUser(email=email, full_name="ROLOBAND Yönetici", role="admin")
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        click.echo(f"✓ Admin oluşturuldu: {email}")

    @app.cli.command("seed")
    def seed():
        """Demo veriler (kategoriler, ürünler, ayarlar, menü)."""
        from app.utils.seeder import run_seed
        run_seed()
        click.echo("✓ Seed tamamlandı.")
