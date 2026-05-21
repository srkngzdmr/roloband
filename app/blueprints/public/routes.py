from __future__ import annotations
"""Public (ön yüz) route'ları."""
from flask import (
    Blueprint, render_template, request, flash, redirect, url_for, abort, current_app
)
from app.extensions import db, limiter
from app.models import (
    Product, ProductCategory, Page, ContactMessage, SiteSetting
)
from app.blueprints.public.forms import ContactForm

public_bp = Blueprint("public", __name__)


# ---------------------------------------------------------------------------
# Anasayfa
# ---------------------------------------------------------------------------
@public_bp.route("/")
def index():
    featured_products = (
        Product.query.filter_by(is_active=True, is_featured=True)
        .order_by(Product.order_index.asc())
        .limit(6).all()
    )
    categories = (
        ProductCategory.query.filter_by(is_active=True)
        .order_by(ProductCategory.order_index.asc())
        .all()
    )
    return render_template(
        "public/index.html",
        featured_products=featured_products,
        categories=categories,
    )


# ---------------------------------------------------------------------------
# Ürün listeleme & kategori
# ---------------------------------------------------------------------------
@public_bp.route("/urunler")
def products_index():
    categories = (
        ProductCategory.query.filter_by(is_active=True)
        .order_by(ProductCategory.order_index.asc())
        .all()
    )
    return render_template("public/products_index.html", categories=categories)


@public_bp.route("/urunler/<slug>")
def category_detail(slug):
    category = ProductCategory.query.filter_by(slug=slug, is_active=True).first_or_404()
    products = (
        category.products.filter_by(is_active=True)
        .order_by(Product.order_index.asc(), Product.name.asc())
        .all()
    )
    return render_template("public/category_detail.html",
                           category=category, products=products)


@public_bp.route("/urun/<slug>")
def product_detail(slug):
    product = Product.query.filter_by(slug=slug, is_active=True).first_or_404()
    related = (
        Product.query
        .filter(Product.category_id == product.category_id,
                Product.id != product.id,
                Product.is_active == True)  # noqa: E712
        .limit(4).all()
    )
    return render_template("public/product_detail.html",
                           product=product, related=related)


# ---------------------------------------------------------------------------
# Dinamik sayfalar (Hakkımızda, Kalite, vb.)
# ---------------------------------------------------------------------------
@public_bp.route("/<slug>")
def dynamic_page(slug):
    # Çakışmaları önle
    reserved = {
        "urunler", "urun", "iletisim", "admin", "static",
        "robots.txt", "sitemap.xml",
    }
    if slug in reserved:
        abort(404)
    page = Page.query.filter_by(slug=slug, is_published=True).first_or_404()
    return render_template("public/page.html", page=page)


# ---------------------------------------------------------------------------
# İletişim
# ---------------------------------------------------------------------------
@public_bp.route("/iletisim", methods=["GET", "POST"])
@limiter.limit("10 per hour", methods=["POST"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        msg = ContactMessage(
            full_name=form.full_name.data.strip(),
            company=(form.company.data or "").strip() or None,
            email=form.email.data.strip().lower(),
            phone=(form.phone.data or "").strip() or None,
            subject=(form.subject.data or "").strip() or None,
            message=form.message.data.strip(),
            ip_address=request.remote_addr,
        )
        db.session.add(msg)
        db.session.commit()
        flash("Mesajınız iletildi. En kısa sürede dönüş yapacağız.", "success")
        return redirect(url_for("public.contact"))
    return render_template("public/contact.html", form=form)


# ---------------------------------------------------------------------------
# robots.txt & sitemap (basit)
# ---------------------------------------------------------------------------
@public_bp.route("/robots.txt")
def robots():
    site_url = current_app.config["SITE_URL"]
    body = (
        "User-agent: *\n"
        "Disallow: /admin/\n"
        f"Sitemap: {site_url}/sitemap.xml\n"
    )
    return body, 200, {"Content-Type": "text/plain"}
