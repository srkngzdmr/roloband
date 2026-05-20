"""Flask uygulama yapılandırması."""
import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")


class BaseConfig:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-change-me")

    # Database
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL", f"sqlite:///{BASE_DIR / 'instance' / 'roloband.db'}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Upload (videolar için yüksek limit)
    MAX_CONTENT_LENGTH = int(os.getenv("MAX_CONTENT_LENGTH_MB", "200")) * 1024 * 1024
    UPLOAD_FOLDER = BASE_DIR / "app" / "static" / "uploads"
    ALLOWED_IMAGE_EXTENSIONS = {"png", "jpg", "jpeg", "webp", "gif", "svg"}
    ALLOWED_VIDEO_EXTENSIONS = {"mp4", "webm", "mov"}

    # CKEditor
    CKEDITOR_PKG_TYPE = "standard"
    CKEDITOR_FILE_UPLOADER = "admin.ckeditor_upload"
    CKEDITOR_ENABLE_CSRF = True
    CKEDITOR_HEIGHT = 400

    # Site
    SITE_NAME = os.getenv("SITE_NAME", "ROLOBAND")
    SITE_URL = os.getenv("SITE_URL", "https://www.roloband.com")

    # Session / güvenlik
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"
    REMEMBER_COOKIE_HTTPONLY = True

    # Cache
    CACHE_TYPE = "SimpleCache"
    CACHE_DEFAULT_TIMEOUT = 300


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TEMPLATES_AUTO_RELOAD = True


class ProductionConfig(BaseConfig):
    DEBUG = False
    SESSION_COOKIE_SECURE = True
    REMEMBER_COOKIE_SECURE = True
    PREFERRED_URL_SCHEME = "https"


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig,
}
