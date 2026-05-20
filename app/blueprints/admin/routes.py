"""Admin panel route'ları."""
from datetime import datetime
from functools import wraps
from flask import (
    Blueprint, render_template, request, redirect, url_for, flash, abort,
    jsonify, current_app
)
from flask_login import login_user, logout_user, login_required, current_user
from app.extensions import db, csrf, limiter
from app.models import (
    AdminUser, Page, ProductCategory, Product, SiteSetting,
    MenuItem, ContactMessage, Media,
)
from app.blueprints.admin.forms import (
    LoginForm, PageForm, CategoryForm, ProductForm,
    HeroSettingsForm, GeneralSettingsForm, MenuItemForm,
)
from app.utils.uploads import save_upload, delete_upload

admin_bp = Blueprint("admin", __name__, template_folder="../../templates/admin")


# ---------------------------------------------------------------------------
# Blueprint-level context: admin sidebar'da okunmamış mesaj sayısı
# ---------------------------------------------------------------------------
@admin_bp.app_context_processor
def inject_admin_context():
    if current_user.is_authenticated and getattr(current_user, "role", None) == "admin":
        try:
            unread = ContactMessage.query.filter_by(is_read=False).count()
        except Exception:
            unread = 0
        return {"unread_count": unread}
    return {"unread_count": 0}


# ---------------------------------------------------------------------------
# Yetki dekoratörü
# ---------------------------------------------------------------------------
def admin_required(fn):
    @wraps(fn)
    @login_required
    def wrapper(*a, **kw):
        if current_user.role != "admin":
            abort(403)
        return fn(*a, **kw)
    return wrapper


# ---------------------------------------------------------------------------
# Login / logout
# ---------------------------------------------------------------------------
@admin_bp.route("/login", methods=["GET", "POST"])
@limiter.limit("20 per hour", methods=["POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("admin.dashboard"))
    form = LoginForm()
    if form.validate_on_submit():
        user = AdminUser.query.filter_by(email=form.email.data.lower().strip()).first()
        if user and user.is_active and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            user.last_login = datetime.utcnow()
            db.session.commit()
            return redirect(request.args.get("next") or url_for("admin.dashboard"))
        flash("E-posta veya şifre hatalı.", "danger")
    return render_template("admin/login.html", form=form)


@admin_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("admin.login"))


# ---------------------------------------------------------------------------
# Dashboard
# ---------------------------------------------------------------------------
@admin_bp.route("/")
@login_required
def dashboard():
    stats = {
        "products": Product.query.count(),
        "categories": ProductCategory.query.count(),
        "pages": Page.query.count(),
        "unread_messages": ContactMessage.query.filter_by(is_read=False).count(),
    }
    recent_messages = (
        ContactMessage.query.order_by(ContactMessage.created_at.desc()).limit(5).all()
    )
    return render_template("admin/dashboard.html", stats=stats, recent_messages=recent_messages)


# ---------------------------------------------------------------------------
# Sayfalar
# ---------------------------------------------------------------------------
@admin_bp.route("/pages")
@login_required
def pages_list():
    pages = Page.query.order_by(Page.order_index.asc(), Page.title.asc()).all()
    return render_template("admin/pages_list.html", pages=pages)


@admin_bp.route("/pages/new", methods=["GET", "POST"])
@login_required
def page_create():
    form = PageForm()
    if form.validate_on_submit():
        page = Page(
            title=form.title.data, content=form.content.data,
            excerpt=form.excerpt.data, meta_title=form.meta_title.data,
            meta_description=form.meta_description.data,
            meta_keywords=form.meta_keywords.data,
            is_published=form.is_published.data, show_in_menu=form.show_in_menu.data,
            order_index=form.order_index.data or 0,
        )
        if form.slug.data:
            page.slug = form.slug.data
        else:
            page.generate_slug()
        if form.cover_image.data:
            page.cover_image = save_upload(form.cover_image.data, "images")
        db.session.add(page)
        db.session.commit()
        flash("Sayfa oluşturuldu.", "success")
        return redirect(url_for("admin.pages_list"))
    return render_template("admin/page_form.html", form=form, page=None)


@admin_bp.route("/pages/<int:page_id>/edit", methods=["GET", "POST"])
@login_required
def page_edit(page_id):
    page = Page.query.get_or_404(page_id)
    form = PageForm(obj=page)
    if form.validate_on_submit():
        page.title = form.title.data
        page.content = form.content.data
        page.excerpt = form.excerpt.data
        page.meta_title = form.meta_title.data
        page.meta_description = form.meta_description.data
        page.meta_keywords = form.meta_keywords.data
        page.is_published = form.is_published.data
        page.show_in_menu = form.show_in_menu.data
        page.order_index = form.order_index.data or 0
        if form.slug.data:
            page.slug = form.slug.data
        else:
            page.generate_slug()
        if form.cover_image.data:
            delete_upload(page.cover_image)
            page.cover_image = save_upload(form.cover_image.data, "images")
        db.session.commit()
        flash("Sayfa güncellendi.", "success")
        return redirect(url_for("admin.pages_list"))
    return render_template("admin/page_form.html", form=form, page=page)


@admin_bp.route("/pages/<int:page_id>/delete", methods=["POST"])
@admin_required
def page_delete(page_id):
    page = Page.query.get_or_404(page_id)
    delete_upload(page.cover_image)
    db.session.delete(page)
    db.session.commit()
    flash("Sayfa silindi.", "info")
    return redirect(url_for("admin.pages_list"))


# ---------------------------------------------------------------------------
# Kategoriler
# ---------------------------------------------------------------------------
@admin_bp.route("/categories")
@login_required
def categories_list():
    cats = ProductCategory.query.order_by(ProductCategory.order_index.asc()).all()
    return render_template("admin/categories_list.html", categories=cats)


@admin_bp.route("/categories/new", methods=["GET", "POST"])
@login_required
def category_create():
    form = CategoryForm()
    if form.validate_on_submit():
        cat = ProductCategory(
            name=form.name.data, short_description=form.short_description.data,
            description=form.description.data, pitch_mm=form.pitch_mm.data,
            icon=form.icon.data, order_index=form.order_index.data or 0,
            is_active=form.is_active.data,
        )
        if form.slug.data:
            cat.slug = form.slug.data
        else:
            cat.generate_slug()
        if form.cover_image.data:
            cat.cover_image = save_upload(form.cover_image.data, "images")
        db.session.add(cat)
        db.session.commit()
        flash("Kategori oluşturuldu.", "success")
        return redirect(url_for("admin.categories_list"))
    return render_template("admin/category_form.html", form=form, category=None)


@admin_bp.route("/categories/<int:cat_id>/edit", methods=["GET", "POST"])
@login_required
def category_edit(cat_id):
    cat = ProductCategory.query.get_or_404(cat_id)
    form = CategoryForm(obj=cat)
    if form.validate_on_submit():
        cat.name = form.name.data
        cat.short_description = form.short_description.data
        cat.description = form.description.data
        cat.pitch_mm = form.pitch_mm.data
        cat.icon = form.icon.data
        cat.order_index = form.order_index.data or 0
        cat.is_active = form.is_active.data
        if form.slug.data:
            cat.slug = form.slug.data
        else:
            cat.generate_slug()
        if form.cover_image.data:
            delete_upload(cat.cover_image)
            cat.cover_image = save_upload(form.cover_image.data, "images")
        db.session.commit()
        flash("Kategori güncellendi.", "success")
        return redirect(url_for("admin.categories_list"))
    return render_template("admin/category_form.html", form=form, category=cat)


@admin_bp.route("/categories/<int:cat_id>/delete", methods=["POST"])
@admin_required
def category_delete(cat_id):
    cat = ProductCategory.query.get_or_404(cat_id)
    delete_upload(cat.cover_image)
    db.session.delete(cat)
    db.session.commit()
    flash("Kategori silindi.", "info")
    return redirect(url_for("admin.categories_list"))


# ---------------------------------------------------------------------------
# Ürünler
# ---------------------------------------------------------------------------
def _populate_category_choices(form: ProductForm) -> None:
    form.category_id.choices = [
        (c.id, c.name) for c in
        ProductCategory.query.order_by(ProductCategory.order_index.asc()).all()
    ]


@admin_bp.route("/products")
@login_required
def products_list():
    products = (
        Product.query.order_by(Product.category_id.asc(), Product.order_index.asc()).all()
    )
    return render_template("admin/products_list.html", products=products)


@admin_bp.route("/products/new", methods=["GET", "POST"])
@login_required
def product_create():
    form = ProductForm()
    _populate_category_choices(form)
    if form.validate_on_submit():
        prod = Product(
            category_id=form.category_id.data, code=form.code.data,
            name=form.name.data, short_description=form.short_description.data,
            description=form.description.data, usage_areas=form.usage_areas.data,
            pitch_mm=form.pitch_mm.data, thickness_mm=form.thickness_mm.data,
            pin_diameter_mm=form.pin_diameter_mm.data,
            open_area_pct=form.open_area_pct.data, surface_type=form.surface_type.data,
            materials=form.materials.data, temp_min=form.temp_min.data,
            temp_max=form.temp_max.data, certifications=form.certifications.data,
            meta_title=form.meta_title.data,
            meta_description=form.meta_description.data,
            is_featured=form.is_featured.data, is_active=form.is_active.data,
            order_index=form.order_index.data or 0,
        )
        if form.slug.data:
            prod.slug = form.slug.data
        else:
            prod.generate_slug()
        if form.cover_image.data:
            prod.cover_image = save_upload(form.cover_image.data, "products")
        if form.datasheet_pdf.data:
            prod.datasheet_pdf = save_upload(form.datasheet_pdf.data, "products")
        db.session.add(prod)
        db.session.commit()
        flash("Ürün oluşturuldu.", "success")
        return redirect(url_for("admin.products_list"))
    return render_template("admin/product_form.html", form=form, product=None)


@admin_bp.route("/products/<int:prod_id>/edit", methods=["GET", "POST"])
@login_required
def product_edit(prod_id):
    prod = Product.query.get_or_404(prod_id)
    form = ProductForm(obj=prod)
    _populate_category_choices(form)
    if form.validate_on_submit():
        for field in (
            "category_id", "code", "name", "short_description", "description",
            "usage_areas", "pitch_mm", "thickness_mm", "pin_diameter_mm",
            "open_area_pct", "surface_type", "materials", "temp_min", "temp_max",
            "certifications", "meta_title", "meta_description",
            "is_featured", "is_active",
        ):
            setattr(prod, field, getattr(form, field).data)
        prod.order_index = form.order_index.data or 0
        if form.slug.data:
            prod.slug = form.slug.data
        else:
            prod.generate_slug()
        if form.cover_image.data:
            delete_upload(prod.cover_image)
            prod.cover_image = save_upload(form.cover_image.data, "products")
        if form.datasheet_pdf.data:
            delete_upload(prod.datasheet_pdf)
            prod.datasheet_pdf = save_upload(form.datasheet_pdf.data, "products")
        db.session.commit()
        flash("Ürün güncellendi.", "success")
        return redirect(url_for("admin.products_list"))
    return render_template("admin/product_form.html", form=form, product=prod)


@admin_bp.route("/products/<int:prod_id>/delete", methods=["POST"])
@admin_required
def product_delete(prod_id):
    prod = Product.query.get_or_404(prod_id)
    delete_upload(prod.cover_image)
    delete_upload(prod.datasheet_pdf)
    db.session.delete(prod)
    db.session.commit()
    flash("Ürün silindi.", "info")
    return redirect(url_for("admin.products_list"))


# ---------------------------------------------------------------------------
# Hero ayarları
# ---------------------------------------------------------------------------
@admin_bp.route("/settings/hero", methods=["GET", "POST"])
@login_required
def settings_hero():
    form = HeroSettingsForm()
    if request.method == "GET":
        form.hero_title.data = SiteSetting.get("hero_title", "")
        form.hero_subtitle.data = SiteSetting.get("hero_subtitle", "")
        form.hero_cta_text.data = SiteSetting.get("hero_cta_text", "")
        form.hero_cta_url.data = SiteSetting.get("hero_cta_url", "")

    if form.validate_on_submit():
        SiteSetting.set("hero_title", form.hero_title.data,
                        value_type="text", label="Hero Başlık", group_name="hero")
        SiteSetting.set("hero_subtitle", form.hero_subtitle.data,
                        value_type="text", label="Hero Alt Metin", group_name="hero")
        SiteSetting.set("hero_cta_text", form.hero_cta_text.data,
                        value_type="text", label="CTA Metni", group_name="hero")
        SiteSetting.set("hero_cta_url", form.hero_cta_url.data,
                        value_type="url", label="CTA Linki", group_name="hero")

        if form.hero_video.data:
            old = SiteSetting.get("hero_video_url")
            if old:
                delete_upload(old)
            new_path = save_upload(form.hero_video.data, "videos")
            SiteSetting.set("hero_video_url", new_path,
                            value_type="video", label="Hero Video", group_name="hero")

        if form.hero_poster.data:
            old = SiteSetting.get("hero_poster_image")
            if old:
                delete_upload(old)
            new_path = save_upload(form.hero_poster.data, "images")
            SiteSetting.set("hero_poster_image", new_path,
                            value_type="image", label="Poster Görsel", group_name="hero")

        db.session.commit()
        flash("Hero ayarları güncellendi.", "success")
        return redirect(url_for("admin.settings_hero"))

    current = {
        "video": SiteSetting.get("hero_video_url"),
        "poster": SiteSetting.get("hero_poster_image"),
    }
    return render_template("admin/settings_hero.html", form=form, current=current)


# ---------------------------------------------------------------------------
# Genel ayarlar
# ---------------------------------------------------------------------------
@admin_bp.route("/settings/general", methods=["GET", "POST"])
@login_required
def settings_general():
    form = GeneralSettingsForm()
    if request.method == "GET":
        for key in ("contact_email", "contact_phone", "contact_address",
                    "contact_map_embed", "social_instagram", "social_linkedin",
                    "footer_about", "certifications"):
            getattr(form, key).data = SiteSetting.get(key, "")

    if form.validate_on_submit():
        for key, group in (
            ("contact_email", "contact"), ("contact_phone", "contact"),
            ("contact_address", "contact"), ("contact_map_embed", "contact"),
            ("social_instagram", "social"), ("social_linkedin", "social"),
            ("footer_about", "general"), ("certifications", "general"),
        ):
            SiteSetting.set(key, getattr(form, key).data or "",
                            value_type="text", label=key, group_name=group)
        db.session.commit()
        flash("Ayarlar güncellendi.", "success")
        return redirect(url_for("admin.settings_general"))

    return render_template("admin/settings_general.html", form=form)


# ---------------------------------------------------------------------------
# Menü
# ---------------------------------------------------------------------------
@admin_bp.route("/menu")
@login_required
def menu_list():
    items = MenuItem.query.order_by(MenuItem.order_index.asc()).all()
    return render_template("admin/menu_list.html", items=items)


@admin_bp.route("/menu/new", methods=["GET", "POST"])
@login_required
def menu_create():
    form = MenuItemForm()
    if form.validate_on_submit():
        item = MenuItem(
            label=form.label.data, url=form.url.data,
            order_index=form.order_index.data or 0,
            is_active=form.is_active.data,
            open_in_new_tab=form.open_in_new_tab.data,
        )
        db.session.add(item)
        db.session.commit()
        flash("Menü öğesi eklendi.", "success")
        return redirect(url_for("admin.menu_list"))
    return render_template("admin/menu_form.html", form=form, item=None)


@admin_bp.route("/menu/<int:item_id>/edit", methods=["GET", "POST"])
@login_required
def menu_edit(item_id):
    item = MenuItem.query.get_or_404(item_id)
    form = MenuItemForm(obj=item)
    if form.validate_on_submit():
        item.label = form.label.data
        item.url = form.url.data
        item.order_index = form.order_index.data or 0
        item.is_active = form.is_active.data
        item.open_in_new_tab = form.open_in_new_tab.data
        db.session.commit()
        flash("Menü güncellendi.", "success")
        return redirect(url_for("admin.menu_list"))
    return render_template("admin/menu_form.html", form=form, item=item)


@admin_bp.route("/menu/<int:item_id>/delete", methods=["POST"])
@admin_required
def menu_delete(item_id):
    item = MenuItem.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for("admin.menu_list"))


# ---------------------------------------------------------------------------
# Mesajlar (iletişim formu kayıtları)
# ---------------------------------------------------------------------------
@admin_bp.route("/messages")
@login_required
def messages_list():
    msgs = ContactMessage.query.order_by(ContactMessage.created_at.desc()).all()
    return render_template("admin/messages_list.html", messages=msgs)


@admin_bp.route("/messages/<int:msg_id>")
@login_required
def message_detail(msg_id):
    msg = ContactMessage.query.get_or_404(msg_id)
    if not msg.is_read:
        msg.is_read = True
        db.session.commit()
    return render_template("admin/message_detail.html", msg=msg)


@admin_bp.route("/messages/<int:msg_id>/delete", methods=["POST"])
@admin_required
def message_delete(msg_id):
    msg = ContactMessage.query.get_or_404(msg_id)
    db.session.delete(msg)
    db.session.commit()
    return redirect(url_for("admin.messages_list"))


# ---------------------------------------------------------------------------
# CKEditor upload
# ---------------------------------------------------------------------------
@admin_bp.route("/ckeditor/upload", methods=["POST"])
@login_required
@csrf.exempt
def ckeditor_upload():
    f = request.files.get("upload")
    if not f:
        return jsonify({"error": {"message": "Dosya yok"}}), 400
    web_path = save_upload(f, "images")
    if not web_path:
        return jsonify({"error": {"message": "Geçersiz dosya tipi"}}), 400
    return jsonify({
        "uploaded": 1,
        "fileName": f.filename,
        "url": web_path,
    })
