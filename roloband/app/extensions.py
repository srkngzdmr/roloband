"""Flask uzantıları (extensions) — circular import'ları önler."""
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from flask_ckeditor import CKEditor
from flask_caching import Cache
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
csrf = CSRFProtect()
ckeditor = CKEditor()
cache = Cache()
limiter = Limiter(key_func=get_remote_address, default_limits=["500 per hour"])

login_manager.login_view = "admin.login"
login_manager.login_message = "Lütfen yönetici paneline erişmek için giriş yapın."
login_manager.login_message_category = "warning"
