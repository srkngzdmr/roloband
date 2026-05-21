from __future__ import annotations
from typing import List, Optional
"""ROLOBAND veritabanı modelleri."""
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from slugify import slugify
from app.extensions import db


# ---------------------------------------------------------------------------
# Admin kullanıcı
# ---------------------------------------------------------------------------
class AdminUser(db.Model, UserMixin):
    __tablename__ = "admin_users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    full_name = db.Column(db.String(120), nullable=False, default="Yönetici")
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), default="admin")  # admin | editor
    is_active = db.Column(db.Boolean, default=True)
    last_login = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, raw: str) -> None:
        self.password_hash = generate_password_hash(raw)

    def check_password(self, raw: str) -> bool:
        return check_password_hash(self.password_hash, raw)

    def __repr__(self) -> str:
        return f"<AdminUser {self.email}>"


# ---------------------------------------------------------------------------
# Dinamik sayfalar (Hakkımızda, Kalite, KVKK vb.)
# ---------------------------------------------------------------------------
class Page(db.Model):
    __tablename__ = "pages"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    slug = db.Column(db.String(220), unique=True, nullable=False, index=True)
    content = db.Column(db.Text)  # CKEditor HTML
    excerpt = db.Column(db.String(300))
    cover_image = db.Column(db.String(300))

    # i18n — English overrides
    title_en = db.Column(db.String(200))
    excerpt_en = db.Column(db.String(300))
    content_en = db.Column(db.Text)

    # SEO
    meta_title = db.Column(db.String(200))
    meta_description = db.Column(db.String(300))
    meta_keywords = db.Column(db.String(300))

    is_published = db.Column(db.Boolean, default=True, index=True)
    show_in_menu = db.Column(db.Boolean, default=False)
    order_index = db.Column(db.Integer, default=0)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def generate_slug(self) -> None:
        base = slugify(self.title or "")
        slug, i = base, 1
        while Page.query.filter(Page.slug == slug, Page.id != self.id).first():
            i += 1
            slug = f"{base}-{i}"
        self.slug = slug


# ---------------------------------------------------------------------------
# Ürün kategorileri (12.7mm, 25.4mm, 50.8mm, Radius, Aksesuar)
# ---------------------------------------------------------------------------
class ProductCategory(db.Model):
    __tablename__ = "product_categories"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    slug = db.Column(db.String(160), unique=True, nullable=False, index=True)
    short_description = db.Column(db.String(300))
    description = db.Column(db.Text)
    icon = db.Column(db.String(100))  # ikon class veya görsel path
    cover_image = db.Column(db.String(300))
    pitch_mm = db.Column(db.Float)  # 12.7 / 25.4 / 50.8 / null
    order_index = db.Column(db.Integer, default=0)
    is_active = db.Column(db.Boolean, default=True, index=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    products = db.relationship(
        "Product",
        backref="category",
        lazy="dynamic",
        cascade="all, delete-orphan",
    )

    def generate_slug(self) -> None:
        base = slugify(self.name or "")
        slug, i = base, 1
        while ProductCategory.query.filter(
            ProductCategory.slug == slug, ProductCategory.id != self.id
        ).first():
            i += 1
            slug = f"{base}-{i}"
        self.slug = slug


# ---------------------------------------------------------------------------
# Ürünler (ROLO BAND Seri 1270, 1271, 2500, 2535, 5000 ...)
# ---------------------------------------------------------------------------
class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(
        db.Integer, db.ForeignKey("product_categories.id"), nullable=False, index=True
    )

    name = db.Column(db.String(200), nullable=False)
    code = db.Column(db.String(80), index=True)  # ör. "Seri 1270"
    slug = db.Column(db.String(220), unique=True, nullable=False, index=True)
    short_description = db.Column(db.String(400))
    description = db.Column(db.Text)  # CKEditor
    usage_areas = db.Column(db.Text)  # CKEditor

    # i18n — English overrides
    description_en = db.Column(db.Text)
    usage_areas_en = db.Column(db.Text)

    # Teknik özellikler
    pitch_mm = db.Column(db.Float)            # 12.7
    thickness_mm = db.Column(db.Float)        # 10
    pin_diameter_mm = db.Column(db.Float)     # 5
    open_area_pct = db.Column(db.Float)       # 0 / 18 / 35
    surface_type = db.Column(db.String(80))   # Kapalı / Açık / Süzgeçli
    materials = db.Column(db.String(200))     # POM, PP, PE
    temp_min = db.Column(db.Float)            # -70
    temp_max = db.Column(db.Float)            # 105
    certifications = db.Column(db.String(200), default="FDA, EU")

    # Medya
    cover_image = db.Column(db.String(300))
    gallery = db.Column(db.Text)  # virgülle ayrılmış path'ler
    datasheet_pdf = db.Column(db.String(300))

    # SEO
    meta_title = db.Column(db.String(200))
    meta_description = db.Column(db.String(300))

    # Durum
    is_featured = db.Column(db.Boolean, default=False, index=True)
    is_active = db.Column(db.Boolean, default=True, index=True)
    order_index = db.Column(db.Integer, default=0)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def generate_slug(self) -> None:
        base = slugify(f"{self.code or ''} {self.name or ''}".strip())
        slug, i = base, 1
        while Product.query.filter(Product.slug == slug, Product.id != self.id).first():
            i += 1
            slug = f"{base}-{i}"
        self.slug = slug

    @property
    def gallery_list(self) -> List[str]:
        if not self.gallery:
            return []
        return [g.strip() for g in self.gallery.split(",") if g.strip()]


# ---------------------------------------------------------------------------
# Medya kütüphanesi (Hero video, banner görselleri vb.)
# ---------------------------------------------------------------------------
class Media(db.Model):
    __tablename__ = "media"

    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(300), nullable=False)
    original_name = db.Column(db.String(300))
    file_path = db.Column(db.String(400), nullable=False)
    file_type = db.Column(db.String(20))  # image | video | pdf
    mime_type = db.Column(db.String(80))
    file_size = db.Column(db.Integer)
    alt_text = db.Column(db.String(200))
    tag = db.Column(db.String(50), index=True)  # hero, product, gallery vb.
    uploaded_at = db.Column(db.DateTime, default=datetime.utcnow)


# ---------------------------------------------------------------------------
# Site ayarları (key-value) — Hero video, telefon, e-posta vb.
# ---------------------------------------------------------------------------
class SiteSetting(db.Model):
    __tablename__ = "site_settings"

    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(80), unique=True, nullable=False, index=True)
    value = db.Column(db.Text)
    value_type = db.Column(db.String(20), default="text")  # text | url | image | video | html
    label = db.Column(db.String(150))
    group_name = db.Column(db.String(50), default="general")  # general | hero | contact | social

    @classmethod
    def get(cls, key: str, default: Optional[str] = None) -> Optional[str]:
        row = cls.query.filter_by(key=key).first()
        return row.value if row and row.value else default

    @classmethod
    def set(cls, key: str, value: str, **kw) -> "SiteSetting":
        row = cls.query.filter_by(key=key).first()
        if not row:
            row = cls(key=key, **kw)
            db.session.add(row)
        row.value = value
        for k, v in kw.items():
            setattr(row, k, v)
        return row

    @classmethod
    def as_dict(cls) -> dict:
        return {r.key: r.value for r in cls.query.all()}


# ---------------------------------------------------------------------------
# Menü öğeleri (üst nav)
# ---------------------------------------------------------------------------
class MenuItem(db.Model):
    __tablename__ = "menu_items"

    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(120), nullable=False)
    url = db.Column(db.String(300), nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey("menu_items.id"))
    order_index = db.Column(db.Integer, default=0)
    is_active = db.Column(db.Boolean, default=True)
    open_in_new_tab = db.Column(db.Boolean, default=False)

    children = db.relationship(
        "MenuItem",
        backref=db.backref("parent", remote_side=[id]),
        cascade="all, delete-orphan",
    )

    @classmethod
    def get_main_menu(cls) -> List["MenuItem"]:
        return (
            cls.query.filter_by(parent_id=None, is_active=True)
            .order_by(cls.order_index.asc())
            .all()
        )


# ---------------------------------------------------------------------------
# İletişim formu mesajları
# ---------------------------------------------------------------------------
class ContactMessage(db.Model):
    __tablename__ = "contact_messages"

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(150), nullable=False)
    company = db.Column(db.String(200))
    email = db.Column(db.String(150), nullable=False)
    phone = db.Column(db.String(50))
    subject = db.Column(db.String(200))
    message = db.Column(db.Text, nullable=False)
    is_read = db.Column(db.Boolean, default=False, index=True)
    ip_address = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
