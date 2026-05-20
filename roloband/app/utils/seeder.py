"""Katalog verilerini DB'ye yükleyen seeder."""
from app.extensions import db
from app.models import ProductCategory, Product, SiteSetting, MenuItem, Page


CATEGORIES = [
    {
        "name": '12.7 mm (1/2") Hatveli Bantlar',
        "short_description": "Dar dönüş ve yüksek hız uygulamaları için ideal.",
        "pitch_mm": 12.7,
        "order_index": 1,
    },
    {
        "name": '25.4 mm (1") Hatveli Bantlar',
        "short_description": "Genel taşıma ve süzme uygulamaları için çok yönlü çözüm.",
        "pitch_mm": 25.4,
        "order_index": 2,
    },
    {
        "name": '50.8 mm (2") Hatveli Bantlar',
        "short_description": "Ağır yük ve yüksek dayanım gerektiren hatlar için.",
        "pitch_mm": 50.8,
        "order_index": 3,
    },
    {
        "name": "Dönüşlü (Radius) Bantlar",
        "short_description": "Yatay dönüş gerektiren karmaşık konveyör hatları için.",
        "pitch_mm": None,
        "order_index": 4,
    },
    {
        "name": "Konveyör Aksesuarları",
        "short_description": "Dişliler, profiller ve sürtünme destekleri.",
        "pitch_mm": None,
        "order_index": 5,
    },
]


PRODUCTS = [
    {
        "category_pitch": 12.7,
        "code": "Seri 1270",
        "name": "Kapalı Yüzey Modüler Bant",
        "short_description": "12.7 mm hatve, %0 açıklık. Yüksek hızlı hatlar ve dar dönüş çapı gerektiren geçiş noktaları için.",
        "description": "<p>12.7 mm (0.5\") hatve ve 10 mm kalınlığa sahip bu serimiz, "
                       "özellikle yüksek hızlı konveyör sistemleri ve minimum dönüş çapı "
                       "gerektiren geçiş noktaları için mükemmel bir çözümdür. Kapalı yüzey "
                       "yapısı sayesinde ürünlerin güvenle taşınmasını sağlarken, yüksek çekme "
                       "mukavemeti ile zorlu şartlara dayanır.</p>",
        "usage_areas": "<ul><li>Et, tavuk ve deniz ürünleri: genel taşıma, paketleme, metal detektörü hatları</li>"
                       "<li>Fırıncılık: soğutma hatları</li>"
                       "<li>İçecek ve kutu üretimi: akümülasyon ve dolum hatları</li></ul>",
        "pitch_mm": 12.7, "thickness_mm": 10, "pin_diameter_mm": 5,
        "open_area_pct": 0, "surface_type": "Kapalı", "materials": "POM, PP, PE",
        "temp_min": -70, "temp_max": 105, "is_featured": True, "order_index": 1,
    },
    {
        "category_pitch": 12.7,
        "code": "Seri 1271",
        "name": "Açık Yüzey Modüler Bant",
        "short_description": "12.7 mm hatve, %18 açıklık. Sıvı süzülmesi ve hava sirkülasyonu gereken hatlar.",
        "description": "<p>12.7 mm hatve yapısını koruyan bu modelimiz, %18 açık yüzey oranı ile "
                       "sıvı süzülmesi veya hava sirkülasyonu gerektiren yüksek hızlı hatlar için "
                       "tasarlanmıştır. 10 mm kalınlığındadır ve dar geçiş alanlarında yüksek "
                       "performans gösterir.</p>",
        "usage_areas": "<ul><li>Et ve deniz ürünlerinde boylama ve kontrol</li>"
                       "<li>Fırıncılıkta soğutma</li>"
                       "<li>İçecek sektöründe palet bozma ve biriktirme</li></ul>",
        "pitch_mm": 12.7, "thickness_mm": 10, "pin_diameter_mm": 5,
        "open_area_pct": 18, "surface_type": "Açık", "materials": "POM, PP, PE",
        "temp_min": -70, "temp_max": 105, "order_index": 2,
    },
    {
        "category_pitch": 25.4,
        "code": "Seri 2500",
        "name": "Kolay Temizlenebilir Kapalı Bant",
        "short_description": "25.4 mm hatve, %0 açıklık. Çıplak ürün taşıyan yüksek hijyenli hatlar için.",
        "description": "<p>25.4 mm (1\") hatve ve 11 mm kalınlık sunan bu model, %0 açıklık oranına "
                       "sahip kapalı bir yüzey sunar. Özellikle hijyen standartlarının en üst düzeyde "
                       "tutulması gereken ve çıplak ürün taşınan hatlar için \"Çok İyi\" "
                       "temizlenebilirlik seviyesine sahiptir.</p>",
        "usage_areas": "<ul><li>Kırmızı ve beyaz et sektöründe çıplak ürün taşıma</li>"
                       "<li>Deniz ürünlerinde kontrol ve sınıflandırma</li>"
                       "<li>Salça ve dondurulmuş gıda hatları</li></ul>",
        "pitch_mm": 25.4, "thickness_mm": 11, "pin_diameter_mm": 5,
        "open_area_pct": 0, "surface_type": "Kapalı", "materials": "POM, PP, PE",
        "temp_min": -70, "temp_max": 105, "is_featured": True, "order_index": 1,
    },
    {
        "category_pitch": 25.4,
        "code": "Seri 2535",
        "name": "Süzgeçli Yüzey Modüler Bant",
        "short_description": "25.4 mm hatve, %35 açıklık. Maksimum sıvı ve hava geçişi.",
        "description": "<p>Hava ve sıvı geçişinin maksimum düzeyde arzu edildiği uygulamalar için "
                       "%35 açık yüzey oranıyla tasarlanmıştır. Düşük ürün temas yüzeyi sayesinde "
                       "yapışmayı önler ve temizliği son derece kolaylaştırır.</p>",
        "usage_areas": "<ul><li>Sebze/meyve ve su ürünleri: yıkama, eleme</li>"
                       "<li>Unlu mamullerde soğutma</li>"
                       "<li>Gıda kurutma prosesleri ve blanşör uygulamaları</li></ul>",
        "pitch_mm": 25.4, "thickness_mm": 10, "pin_diameter_mm": 5,
        "open_area_pct": 35, "surface_type": "Süzgeçli", "materials": "POM, PP, PE",
        "temp_min": -70, "temp_max": 105, "order_index": 2,
    },
    {
        "category_pitch": 50.8,
        "code": "Seri 5000",
        "name": "Ağır Hizmet Kapalı Bant",
        "short_description": "50.8 mm hatve, 16 mm kalınlık. Ağır yükler ve büyük ölçekli hatlar.",
        "description": "<p>Yüksek mukavemet gerektiren ağır sanayi ve büyük ölçekli hatlar için "
                       "geliştirilen 50.8 mm (1.97\") hatveli kapalı serimizdir. 16 mm kalınlığı ve "
                       "güçlü yapısı ile zorlu yüklerin üstesinden rahatlıkla gelir.</p>",
        "usage_areas": "<ul><li>Lastik üretimi</li>"
                       "<li>Oluklu mukavva hatları</li>"
                       "<li>Lojistik ürün ayırma/tokatlama konveyörleri</li>"
                       "<li>Şişe dolum tesislerinde ağır paletleme</li></ul>",
        "pitch_mm": 50.8, "thickness_mm": 16, "pin_diameter_mm": 7,
        "open_area_pct": 0, "surface_type": "Kapalı", "materials": "POM, PP, PE",
        "temp_min": -70, "temp_max": 105, "is_featured": True, "order_index": 1,
    },
]


SETTINGS = [
    # Hero
    ("hero_title", "Modüler Konveyör Sistemlerinde Çözüm Ortağınız", "text", "Hero Başlık", "hero"),
    ("hero_subtitle",
     "İzmir Menderes'ten dünyaya. Gıda işleme makineleri için FDA ve EU onaylı, "
     "uzun ömürlü modüler bant çözümleri.",
     "text", "Hero Alt Metin", "hero"),
    ("hero_cta_text", "Ürünlerimizi İnceleyin", "text", "Hero CTA Metni", "hero"),
    ("hero_cta_url", "/urunler", "url", "Hero CTA Linki", "hero"),
    ("hero_video_url", "", "video", "Hero Video (yüklenmemiş)", "hero"),
    ("hero_poster_image", "", "image", "Hero Video Poster Görseli", "hero"),
    # İletişim
    ("contact_email", "info@roloband.com", "text", "E-posta", "contact"),
    ("contact_phone", "+90 (000) 000 00 00", "text", "Telefon", "contact"),
    ("contact_address",
     "Oğlananası Atatürk, 1. Cd. No:54, 35471 Menderes/İzmir",
     "text", "Adres", "contact"),
    ("contact_map_embed", "", "html", "Google Maps Embed", "contact"),
    # Sosyal
    ("social_instagram", "https://instagram.com/rolobandmoduler", "url", "Instagram", "social"),
    ("social_linkedin", "", "url", "LinkedIn", "social"),
    # Genel
    ("footer_about",
     "ROLOBAND, gıda işleme sektörüne makine üreten imalatçıların güvenilir "
     "modüler bant tedarikçisidir. FDA ve EU onaylı, kolay temizlenebilir, "
     "uzun ömürlü çözümler.",
     "text", "Footer Hakkımızda", "general"),
    ("certifications", "FDA, EU 10/2011", "text", "Sertifikalar", "general"),
]


MENU = [
    ("Anasayfa", "/", 1),
    ("Hakkımızda", "/hakkimizda", 2),
    ("Ürünler", "/urunler", 3),
    ("Sektörler", "/sektorler", 4),
    ("Kalite & Sertifikalar", "/kalite", 5),
    ("İletişim", "/iletisim", 6),
]


PAGES = [
    {
        "title": "Hakkımızda",
        "slug": "hakkimizda",
        "excerpt": "İzmir Menderes'teki üretim üssümüzden gıda işleme sektörüne hizmet veriyoruz.",
        "content": "<h2>ROLOBAND Hakkında</h2>"
                   "<p>İzmir Menderes'teki tesisimizden, gıda işleme sektörüne ve bu tesislere "
                   "ileri teknoloji makine üreten imalatçılara yüksek kaliteli modüler bant "
                   "çözümleri sunuyoruz.</p>"
                   "<p>Kırmızı et, beyaz et, su ürünleri, unlu mamuller ve meyve-sebze işleme "
                   "hatları başta olmak üzere; zeytin, biber, turşu ve baharat gibi zorlu proses "
                   "koşullarına sahip tesisler için uzun ömürlü, gıdaya uygun (FDA ve EU onaylı) "
                   "ve kolay temizlenebilir konveyör ekipmanları üretiyoruz.</p>"
                   "<p>Amacımız sadece parça tedarik etmek değil; inovatif makine üreticilerinin "
                   "üretim hatlarında kesintisiz verimlilik sağlayan güvenilir çözüm ortağı olmaktır.</p>",
    },
    {
        "title": "Sektörler",
        "slug": "sektorler",
        "excerpt": "Kırmızı et, beyaz et, su ürünleri, unlu mamuller, meyve-sebze ve daha fazlası.",
        "content": "<h2>Hizmet Verdiğimiz Sektörler</h2>"
                   "<ul><li>Kırmızı et işleme tesisleri</li>"
                   "<li>Beyaz et (tavuk) işleme</li>"
                   "<li>Su ürünleri ve balık işleme</li>"
                   "<li>Unlu mamuller ve fırıncılık</li>"
                   "<li>Meyve-sebze işleme</li>"
                   "<li>Zeytin, biber, turşu, baharat</li>"
                   "<li>İçecek ve dolum hatları</li>"
                   "<li>Lojistik ve paketleme</li></ul>",
    },
    {
        "title": "Kalite & Sertifikalar",
        "slug": "kalite",
        "excerpt": "FDA ve EU 10/2011 onaylı, gıda ile temasa uygun malzemeler.",
        "content": "<h2>Kalite Politikamız</h2>"
                   "<p>Tüm bantlarımız <strong>FDA</strong> ve <strong>EU 10/2011</strong> "
                   "standartlarına uygun olarak üretilmektedir. POM, PP ve PE malzeme "
                   "seçenekleriyle her uygulamaya özel çözüm sunarız.</p>",
    },
]


def run_seed() -> None:
    # Site ayarları
    for key, value, vtype, label, group in SETTINGS:
        if not SiteSetting.query.filter_by(key=key).first():
            db.session.add(SiteSetting(
                key=key, value=value, value_type=vtype, label=label, group_name=group
            ))

    # Menü
    for label, url, order in MENU:
        if not MenuItem.query.filter_by(label=label).first():
            db.session.add(MenuItem(label=label, url=url, order_index=order))

    # Statik sayfalar
    for p in PAGES:
        if not Page.query.filter_by(slug=p["slug"]).first():
            page = Page(**p, is_published=True)
            db.session.add(page)

    # Kategoriler
    cat_by_pitch: dict[float | None, ProductCategory] = {}
    for c in CATEGORIES:
        existing = ProductCategory.query.filter_by(name=c["name"]).first()
        if existing:
            cat_by_pitch[c["pitch_mm"]] = existing
            continue
        cat = ProductCategory(**c)
        cat.generate_slug()
        db.session.add(cat)
        db.session.flush()
        cat_by_pitch[c["pitch_mm"]] = cat

    # Ürünler
    for p in PRODUCTS:
        pitch = p.pop("category_pitch")
        cat = cat_by_pitch.get(pitch)
        if not cat:
            continue
        if Product.query.filter_by(code=p["code"]).first():
            continue
        prod = Product(category_id=cat.id, **p)
        prod.generate_slug()
        db.session.add(prod)

    db.session.commit()
