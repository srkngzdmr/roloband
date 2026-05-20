"""Admin panel form'ları."""
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_ckeditor import CKEditorField
from wtforms import (
    StringField, TextAreaField, BooleanField, IntegerField, FloatField,
    SelectField, PasswordField, SubmitField, HiddenField
)
from wtforms.validators import DataRequired, Email, Length, Optional, NumberRange

IMAGE_EXT = ["png", "jpg", "jpeg", "webp", "gif", "svg"]
VIDEO_EXT = ["mp4", "webm", "mov"]


class LoginForm(FlaskForm):
    email = StringField("E-posta", validators=[DataRequired(), Email()])
    password = PasswordField("Şifre", validators=[DataRequired()])
    remember = BooleanField("Beni hatırla")
    submit = SubmitField("Giriş Yap")


class PageForm(FlaskForm):
    title = StringField("Başlık", validators=[DataRequired(), Length(max=200)])
    slug = StringField("Slug (boş bırakılırsa otomatik)", validators=[Optional(), Length(max=220)])
    excerpt = TextAreaField("Özet", validators=[Optional(), Length(max=300)])
    content = CKEditorField("İçerik")
    cover_image = FileField("Kapak Görseli", validators=[Optional(), FileAllowed(IMAGE_EXT)])
    meta_title = StringField("Meta Title", validators=[Optional(), Length(max=200)])
    meta_description = StringField("Meta Description", validators=[Optional(), Length(max=300)])
    meta_keywords = StringField("Meta Keywords", validators=[Optional(), Length(max=300)])
    is_published = BooleanField("Yayında", default=True)
    show_in_menu = BooleanField("Menüde göster")
    order_index = IntegerField("Sıra", validators=[Optional()], default=0)
    submit = SubmitField("Kaydet")


class CategoryForm(FlaskForm):
    name = StringField("Kategori Adı", validators=[DataRequired(), Length(max=150)])
    slug = StringField("Slug", validators=[Optional(), Length(max=160)])
    short_description = StringField("Kısa Açıklama", validators=[Optional(), Length(max=300)])
    description = CKEditorField("Detaylı Açıklama")
    pitch_mm = FloatField("Hatve (mm)", validators=[Optional()])
    icon = StringField("İkon (sınıf veya emoji)", validators=[Optional(), Length(max=100)])
    cover_image = FileField("Kapak Görseli", validators=[Optional(), FileAllowed(IMAGE_EXT)])
    order_index = IntegerField("Sıra", validators=[Optional()], default=0)
    is_active = BooleanField("Aktif", default=True)
    submit = SubmitField("Kaydet")


class ProductForm(FlaskForm):
    category_id = SelectField("Kategori", coerce=int, validators=[DataRequired()])
    code = StringField("Ürün Kodu (ör. Seri 1270)", validators=[Optional(), Length(max=80)])
    name = StringField("Ürün Adı", validators=[DataRequired(), Length(max=200)])
    slug = StringField("Slug", validators=[Optional(), Length(max=220)])
    short_description = TextAreaField("Kısa Açıklama", validators=[Optional(), Length(max=400)])
    description = CKEditorField("Detaylı Açıklama")
    usage_areas = CKEditorField("Kullanım Alanları")

    pitch_mm = FloatField("Hatve (mm)", validators=[Optional()])
    thickness_mm = FloatField("Kalınlık (mm)", validators=[Optional()])
    pin_diameter_mm = FloatField("Pim Çapı (mm)", validators=[Optional()])
    open_area_pct = FloatField("Açıklık Oranı (%)",
                               validators=[Optional(), NumberRange(min=0, max=100)])
    surface_type = StringField("Yüzey Tipi (Kapalı/Açık/Süzgeçli)",
                               validators=[Optional(), Length(max=80)])
    materials = StringField("Malzemeler (POM, PP, PE)",
                            validators=[Optional(), Length(max=200)])
    temp_min = FloatField("Min Sıcaklık (°C)", validators=[Optional()])
    temp_max = FloatField("Max Sıcaklık (°C)", validators=[Optional()])
    certifications = StringField("Sertifikalar", validators=[Optional(), Length(max=200)])

    cover_image = FileField("Kapak Görseli", validators=[Optional(), FileAllowed(IMAGE_EXT)])
    datasheet_pdf = FileField("Teknik Föy (PDF)", validators=[Optional(), FileAllowed(["pdf"])])

    meta_title = StringField("Meta Title", validators=[Optional(), Length(max=200)])
    meta_description = StringField("Meta Description", validators=[Optional(), Length(max=300)])

    is_featured = BooleanField("Öne Çıkar")
    is_active = BooleanField("Aktif", default=True)
    order_index = IntegerField("Sıra", validators=[Optional()], default=0)
    submit = SubmitField("Kaydet")


class HeroSettingsForm(FlaskForm):
    hero_title = StringField("Başlık (slogan)", validators=[DataRequired(), Length(max=200)])
    hero_subtitle = TextAreaField("Alt metin", validators=[Optional(), Length(max=500)])
    hero_cta_text = StringField("CTA Buton Metni", validators=[Optional(), Length(max=80)])
    hero_cta_url = StringField("CTA Buton Linki", validators=[Optional(), Length(max=300)])
    hero_video = FileField("Hero Videosu (MP4/WebM/MOV)",
                           validators=[Optional(), FileAllowed(VIDEO_EXT)])
    hero_poster = FileField("Video Poster Görseli",
                            validators=[Optional(), FileAllowed(IMAGE_EXT)])
    submit = SubmitField("Kaydet")


class GeneralSettingsForm(FlaskForm):
    contact_email = StringField("E-posta", validators=[Optional(), Email()])
    contact_phone = StringField("Telefon", validators=[Optional(), Length(max=80)])
    contact_address = TextAreaField("Adres", validators=[Optional(), Length(max=400)])
    contact_map_embed = TextAreaField("Google Maps Embed iframe",
                                      validators=[Optional(), Length(max=2000)])
    social_instagram = StringField("Instagram URL", validators=[Optional(), Length(max=300)])
    social_linkedin = StringField("LinkedIn URL", validators=[Optional(), Length(max=300)])
    footer_about = TextAreaField("Footer Hakkımızda metni",
                                 validators=[Optional(), Length(max=800)])
    certifications = StringField("Sertifikalar", validators=[Optional(), Length(max=200)])
    submit = SubmitField("Kaydet")


class MenuItemForm(FlaskForm):
    label = StringField("Etiket", validators=[DataRequired(), Length(max=120)])
    url = StringField("URL", validators=[DataRequired(), Length(max=300)])
    order_index = IntegerField("Sıra", validators=[Optional()], default=0)
    is_active = BooleanField("Aktif", default=True)
    open_in_new_tab = BooleanField("Yeni sekmede aç")
    submit = SubmitField("Kaydet")
