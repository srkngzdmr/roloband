SUPPORTED_LANGS = ['tr', 'en']
DEFAULT_LANG = 'tr'
RTL_LANGS = []

LANG_NAMES = {
    'tr': 'Türkçe',
    'en': 'English',
}

# ─── DB'den gelen sabit metinlerin çevirileri ─────────────────────────────────
DB_TRANSLATIONS = {
    # Menü etiketleri
    'Anasayfa':             {'en': 'Home'},
    'Hakkımızda':           {'en': 'About Us'},
    'Ürünler':              {'en': 'Products'},
    'Sektörler':            {'en': 'Sectors'},
    'Kalite & Sertifikalar':{'en': 'Quality & Certifications'},
    'İletişim':             {'en': 'Contact'},

    # Kategori isimleri
    '12.7 mm (1/2") Hatveli Bantlar': {'en': '12.7 mm (1/2") Pitch Belts'},
    '25.4 mm (1") Hatveli Bantlar':   {'en': '25.4 mm (1") Pitch Belts'},
    '50.8 mm (2") Hatveli Bantlar':   {'en': '50.8 mm (2") Pitch Belts'},
    'Dönüşlü (Radius) Bantlar':       {'en': 'Radius Turn Belts'},
    'Konveyör Aksesuarları':          {'en': 'Conveyor Accessories'},

    # Kategori açıklamaları
    'Dar donus capiyla paketleme, et ve unlu mamul hatlarinin vazgecilmezi.': {
        'en': 'The go-to belt for tight-turn packaging, meat processing and bakery product lines.',
    },
    'Blansor, yikama ve hijyenik tasima gerektiren zeytin, sebze ve firinclik hatlari.': {
        'en': 'Ideal for blanching, washing and hygienic transfer in olive, vegetable and bakery lines.',
    },
    'Agir firinclik tavaları, endustriyel kasalar ve buyuk olcekli lojistik hatlari icin.': {
        'en': 'For heavy bakery pans, industrial crates and large-scale logistics conveyor lines.',
    },
    'Spiral sogutma, fermentasyon ve kompakt yatay donus gerektiren firinclik hatlari.': {
        'en': 'For spiral cooling, fermentation and bakery lines requiring compact horizontal turns.',
    },
    'Guide, bolucue ve disli aksesuarlar — makine tasarimini tamamlayan yerli destek.': {
        'en': 'Guides, dividers and sprockets — local support to complete your machine design.',
    },

    # Ürün isimleri
    'Kapalı Yüzey Modüler Bant':        {'en': 'Closed Surface Modular Belt'},
    'Açık Yüzey Modüler Bant':          {'en': 'Open Surface Modular Belt'},
    'Kolay Temizlenebilir Kapalı Bant': {'en': 'Easy-Clean Closed Belt'},
    'Süzgeçli Yüzey Modüler Bant':      {'en': 'Perforated Surface Modular Belt'},
    'Ağır Hizmet Kapalı Bant':          {'en': 'Heavy Duty Closed Belt'},

    # Ürün kısa açıklamaları
    '12.7 mm hatve, %0 kapali yuzeyli. Dar donus capli paketleme, ekmek ve et isleme hatlarinda yuksek hizli tasima icin.': {
        'en': '12.7 mm pitch, 0% open surface. For high-speed transfer on tight-turn packaging, bread and meat processing lines.',
    },
    '12.7 mm hatve, %18 aciklik. Sivi suzulmesi, hava sirkuelasyonu ve urun secme gerektiren meyve-sebze, zeytin ve firinclik hatlari icin.': {
        'en': '12.7 mm pitch, 18% open area. For fruit-vegetable, olive and bakery lines requiring liquid drainage, air circulation and product sorting.',
    },
    '25.4 mm hatve, %0 aciklik, kolay temizlenebilir kapali yuzeyli. Ciplak gida temas eden yuksek hijyenli paketleme ve et isleme hatlari icin.': {
        'en': '25.4 mm pitch, 0% open area, easy-clean closed surface. For high-hygiene packaging and meat processing lines with direct food contact.',
    },
    '25.4 mm hatve, %35 aciklik. Maksimum sivi ve hava gecisi. Blansor, yikama ve spiral sogutma gerektiren zeytin, sebze ve firinclik hatlari icin.': {
        'en': '25.4 mm pitch, 35% open area. Maximum liquid and air flow. For olive, vegetable and bakery lines requiring blanching, washing and spiral cooling.',
    },
    '50.8 mm hatve, 16 mm kalinlik. Agir tava, kasa ve endustriyel firinclik ekipmaninin tasindigi buyuk olcekli hatlar icin.': {
        'en': '50.8 mm pitch, 16 mm thickness. For large-scale lines carrying heavy pans, crates and industrial bakery equipment.',
    },

    # Yüzey tipleri
    'Kapalı':   {'en': 'Closed'},
    'Açık':     {'en': 'Open'},
    'Süzgeçli': {'en': 'Perforated'},

    # Footer ayarı (DB değeri)
    'ROLOBAND, gıda işleme sektörüne makine üreten imalatçıların güvenilir modüler bant tedarikçisidir. FDA ve EU onaylı, kolay temizlenebilir, uzun ömürlü çözümler.': {
        'en': 'ROLOBAND is the trusted modular belt supplier for food processing machine manufacturers. FDA and EU approved, easy-clean, long-lasting solutions.',
    },

    # Adres (DB settings)
    'Oğlananası Atatürk, 1. Cd. No:54, 35471 Menderes/İzmir': {
        'en': 'Ataturk Blvd, No:54, 35471 Menderes / Izmir, Turkey',
    },
}


TRANSLATIONS = {
    # Genel
    'site_tagline': {'tr': 'Modüler Konveyör Bantları', 'en': 'Modular Conveyor Belts'},
    'meta_description': {
        'tr': 'ROLOBAND — İzmir Menderes merkezli, FDA ve EU onaylı modüler konveyör bant üreticisi. Gıda işleme makine imalatçıları için profesyonel B2B çözümler.',
        'en': 'ROLOBAND — Based in Izmir Menderes, FDA and EU approved modular conveyor belt manufacturer. Professional B2B solutions for food processing machine manufacturers.',
    },
    'splash_tagline': {
        'tr': 'Modüler Konveyör Sistemlerinde Çözüm Ortağınız',
        'en': 'Your Partner in Modular Conveyor Systems',
    },
    'splash_fda':      {'tr': 'FDA Onaylı',      'en': 'FDA Approved'},
    'splash_eu':       {'tr': 'EU 10/2011',      'en': 'EU 10/2011'},
    'splash_location': {'tr': 'İzmir / Türkiye', 'en': 'Izmir / Turkey'},
    'loading':         {'tr': 'Yükleniyor',      'en': 'Loading'},
    'nav_cta':         {'tr': 'Teklif Al',       'en': 'Get a Quote'},
    'nav_menu_label':  {'tr': 'Menü',            'en': 'Menu'},
    'breadcrumb_home':     {'tr': 'Anasayfa', 'en': 'Home'},
    'breadcrumb_products': {'tr': 'Ürünler',  'en': 'Products'},
    'breadcrumb_contact':  {'tr': 'İletişim', 'en': 'Contact'},

    # Footer
    'footer_about_default': {
        'tr': 'Gıda işleme sektörüne makine üreten imalatçıların güvenilir modüler bant tedarikçisi.',
        'en': 'Trusted modular belt supplier for food processing machine manufacturers.',
    },
    'footer_products':      {'tr': 'Ürünler',               'en': 'Products'},
    'footer_all_products':  {'tr': 'Tüm Ürünler',           'en': 'All Products'},
    'footer_hatve_suffix':  {'tr': 'mm Hatve',              'en': 'mm Pitch'},
    'footer_radius_belts':  {'tr': 'Radius Bantlar',        'en': 'Radius Belts'},
    'footer_corporate':     {'tr': 'Kurumsal',              'en': 'Corporate'},
    'footer_about_link':    {'tr': 'Hakkımızda',            'en': 'About Us'},
    'footer_sectors_link':  {'tr': 'Sektörler',             'en': 'Sectors'},
    'footer_quality_link':  {'tr': 'Kalite & Sertifikalar', 'en': 'Quality & Certifications'},
    'footer_contact_link':  {'tr': 'İletişim',              'en': 'Contact'},
    'footer_contact_title': {'tr': 'İletişim',              'en': 'Contact'},
    'footer_rights':        {'tr': 'Tüm hakları saklıdır.', 'en': 'All rights reserved.'},
    'footer_cert_suffix':   {'tr': 'Onaylı Üretim',         'en': 'Certified Manufacturing'},

    # Hero — sadece t() ile kullanılır, settings değerleri atlantır
    'hero_eyebrow': {
        'tr': 'İzmir / Türkiye &nbsp;•&nbsp; FDA &amp; EU Onaylı Üretici',
        'en': 'Izmir / Turkey &nbsp;•&nbsp; FDA &amp; EU Certified Manufacturer',
    },
    'hero_h1_line1':  {'tr': 'Modüler Taşıma', 'en': 'Modular Conveyor'},
    'hero_h1_accent': {'tr': 'Bantları',        'en': 'Belts'},
    'hero_subtitle': {
        'tr': 'Ağır sanayiden gıdaya her sektörün ihtiyacına özel, yüksek dayanımlı modüler taşıma bantları üretiyoruz. İşletmenizin yükünü paylaşıyor, kesintisiz üretim hattı için en sağlam çözümleri sunuyoruz.',
        'en': 'We manufacture high-durability modular conveyor belts tailored to every industry — from heavy industry to food processing. Reliable supply, fast shipping, engineering support.',
    },
    'hero_cta_catalog': {'tr': 'Ürün Kataloğu', 'en': 'Product Catalog'},
    'hero_cta_quote':   {'tr': 'Teklif İste',   'en': 'Request a Quote'},

    # Stats
    'stat_experience': {'tr': 'Yıllık Tecrübe', 'en': 'Years Experience'},
    'stat_models':     {'tr': 'Ürün Modeli',    'en': 'Product Models'},
    'stat_clients':    {'tr': 'B2B Müşteri',    'en': 'B2B Clients'},
    'stat_certified':  {'tr': 'EU Onaylı',      'en': 'EU Certified'},

    # Cert strip
    'cert_fda':         {'tr': 'FDA Onaylı Malzeme',        'en': 'FDA Approved Material'},
    'cert_eu':          {'tr': 'EU 10/2011 Sertifikalı',    'en': 'EU 10/2011 Certified'},
    'cert_stock':       {'tr': 'Stoktan Hızlı Sevkiyat',    'en': 'Fast Delivery from Stock'},
    'cert_materials':   {'tr': 'POM / PP / PE Seçenekleri', 'en': 'POM / PP / PE Options'},
    'cert_engineering': {'tr': 'Mühendislik Desteği',       'en': 'Engineering Support'},

    # B2B Value
    'b2b_eyebrow': {'tr': 'Neden Makine Üreticileri?',         'en': 'Why Machine Manufacturers?'},
    'b2b_title':   {'tr': 'Tekrar Eden İş, Güvenilir Ortaklık', 'en': 'Repeat Business, Reliable Partnership'},
    'b2b_desc': {
        'tr': 'Gıda işleme makinesi üreten firmalara satış yapmak, son kullanıcıya satıştan çok daha değerlidir. Bir makine üreticisi yılda onlarca makine üretir — her makineye bant gerekir. Doğru ortaklık kurulduğunda bu <strong>sürekli ve öngörülebilir bir iş hacmine</strong> dönüşür.',
        'en': 'Selling to food processing machine manufacturers is far more valuable than selling to end users. A machine manufacturer produces dozens of machines per year — each machine needs belts. With the right partnership, this becomes <strong>a continuous and predictable volume of business</strong>.',
    },
    'b2b_item1_title': {'tr': 'Sürekli Sipariş',        'en': 'Recurring Orders'},
    'b2b_item1_desc':  {
        'tr': 'Her üretim serisinde bant ihtiyacı doğar. Tek seferlik değil, yıllık tedarik ilişkisi.',
        'en': 'Every production run creates a belt demand. Not a one-time sale, but a yearly supply relationship.',
    },
    'b2b_item2_title': {'tr': 'Hızlı Prototip Desteği', 'en': 'Fast Prototyping Support'},
    'b2b_item2_desc':  {
        'tr': 'Yeni makine tasarımlarında doğru hatve ve bant tipini birlikte seçeriz.',
        'en': 'We help select the right pitch and belt type for new machine designs together.',
    },
    'b2b_item3_title': {'tr': 'Esnek Lot Miktarları',   'en': 'Flexible Lot Quantities'},
    'b2b_item3_desc':  {
        'tr': 'Küçük seri üretimden büyük siparişlere kadar stoklu teslimat garantisi.',
        'en': 'Guaranteed stock delivery from small-batch production to large orders.',
    },
    'b2b_cta': {
        'tr': 'Makine Üreticisi Olarak Görüşelim →',
        'en': "Let's Talk as a Machine Manufacturer →",
    },
    'b2b_market_title':    {'tr': 'Hedef Pazarımız',                                'en': 'Our Target Market'},
    'b2b_market_subtitle': {'tr': 'Gıda makinesi üreten firmalar — İzmir ve tüm Türkiye', 'en': 'Food machine manufacturers — Izmir and all of Turkey'},
    'b2b_sector_packaging':   {'tr': '📦 Paketleme Makineleri',            'en': '📦 Packaging Machines'},
    'b2b_sector_bread':       {'tr': '🥖 Ekmek & Tortilla Üretim Hatları', 'en': '🥖 Bread & Tortilla Production Lines'},
    'b2b_sector_olive':       {'tr': '🫒 Zeytin & Meyve İşleme Hatları',  'en': '🫒 Olive & Fruit Processing Lines'},
    'b2b_sector_spiral':      {'tr': '🌀 Spiral Soğutma & Fermentasyon',  'en': '🌀 Spiral Cooling & Fermentation'},
    'b2b_sector_meat':        {'tr': '🥩 Kırmızı Et & Tavukçuluk',        'en': '🥩 Red Meat & Poultry'},
    'b2b_sector_blancher':    {'tr': '🚿 Blanşör & Yıkama Sistemleri',    'en': '🚿 Blancher & Washing Systems'},
    'b2b_sector_thermoform':  {'tr': '📦 Thermoform & Tray Sealer Hatları', 'en': '📦 Thermoform & Tray Sealer Lines'},
    'b2b_sector_integration': {'tr': '🔧 Konveyör Sistem Entegrasyonu',   'en': '🔧 Conveyor System Integration'},
    'b2b_intralox_note': {
        'tr': 'Intralox ve Habasit alternatifi, yerli mühendislik desteği ile',
        'en': 'Intralox and Habasit alternative, with local engineering support',
    },

    # Categories
    'categories_eyebrow': {'tr': 'Ürün Yelpazemiz',                     'en': 'Our Product Range'},
    'categories_title':   {'tr': 'Hatve Ölçüsüne Göre Modüler Bantlar', 'en': 'Modular Belts by Pitch Size'},
    'categories_desc': {
        'tr': 'Her uygulama için doğru hatve — 12.7 mm dar dönüşten 50.8 mm ağır yüke kadar tam ürün ailesi.',
        'en': 'The right pitch for every application — a complete product family from 12.7 mm tight turns to 50.8 mm heavy loads.',
    },
    'btn_explore':         {'tr': 'İncele',    'en': 'Explore'},
    'pitch_special':       {'tr': 'Özel Seri', 'en': 'Special Series'},
    'pitch_special_short': {'tr': 'Özel',      'en': 'Special'},

    # Featured
    'featured_eyebrow': {'tr': 'Öne Çıkan Modeller',                'en': 'Featured Models'},
    'featured_title':   {'tr': 'En Çok Tercih Edilen Bant Serileri', 'en': 'Most Preferred Belt Series'},
    'featured_desc': {
        'tr': 'Makine üreticilerinin projelerde en sık kullandığı, kanıtlanmış modüler bant modelleri.',
        'en': 'Proven modular belt models most frequently used by machine manufacturers in their projects.',
    },

    # Compare
    'compare_eyebrow': {'tr': 'Habasit & Intralox Alternatifi',                      'en': 'Habasit & Intralox Alternative'},
    'compare_title':   {'tr': "Neden Makine Üreticileri ROLOBAND'ı Tercih Eder?", 'en': 'Why Do Machine Manufacturers Prefer ROLOBAND?'},
    'compare_desc': {
        'tr': 'Uluslararası markaların kalitesi, yerli firmanın hızı ve esnekliği.',
        'en': 'The quality of international brands, with the speed and flexibility of a local company.',
    },
    'compare1_title': {'tr': 'Stoktan Anında Teslimat',      'en': 'Immediate Delivery from Stock'},
    'compare1_desc':  {
        'tr': "Habasit veya Intralox'tan sipariş verdiğinizde haftalar bekleyebilirsiniz. Biz stoklu ürünle aynı gün sevk ederiz.",
        'en': 'Ordering from Habasit or Intralox can mean waiting weeks. We ship same-day with in-stock products.',
    },
    'compare2_title': {'tr': 'Direkt Mühendislik Desteği',   'en': 'Direct Engineering Support'},
    'compare2_desc':  {
        'tr': 'Makine tasarım aşamasında yanınızdayız. Hatve seçimi, bant tipi, aksesuar — her adımda teknik destek.',
        'en': 'We are with you during the machine design phase. Pitch selection, belt type, accessories — technical support at every step.',
    },
    'compare3_title': {'tr': 'Rekabetçi Fiyat',              'en': 'Competitive Pricing'},
    'compare3_desc':  {
        'tr': 'Uluslararası marka fiyatlarının çok altında, aynı FDA & EU sertifikalı malzemelerle üretim.',
        'en': 'Far below international brand prices, manufactured with the same FDA & EU certified materials.',
    },
    'compare4_title': {'tr': 'Özel Lot & Boyut',             'en': 'Custom Lots & Sizes'},
    'compare4_desc':  {
        'tr': 'Küçük seri projeleriniz için minimum sipariş baskısı yok. İhtiyacınız kadar, istediğiniz boyutta.',
        'en': 'No minimum order pressure for small-batch projects. As much as you need, in any size you want.',
    },
    'compare5_title': {'tr': 'İzmir Merkezli, Hızlı Ulaşım', 'en': 'Izmir-Based, Fast Reach'},
    'compare5_desc':  {
        'tr': "İzmir'deki makine üreticilerine ertesi gün teslimat. Tüm Türkiye'ye hızlı kargo ağı.",
        'en': 'Next-day delivery to Izmir machine manufacturers. Fast cargo network throughout Turkey.',
    },
    'compare6_title': {'tr': 'Sürekli Tedarik Güvencesi',    'en': 'Continuous Supply Guarantee'},
    'compare6_desc':  {
        'tr': 'Proje bazlı değil, yıllık tedarikçi olarak çalışırız. Üretim takviminize göre planlama yaparız.',
        'en': 'We work as an annual supplier, not project-by-project. We plan according to your production schedule.',
    },

    # Industries
    'industries_eyebrow': {'tr': 'Hizmet Verdiğimiz Sektörler',             'en': 'Industries We Serve'},
    'industries_title':   {'tr': 'Makine Üreticilerinin Ürettiği Her Sistemde', 'en': 'In Every System Machine Manufacturers Produce'},
    'industries_desc': {
        'tr': 'Paketleme makinelerinden spiral soğutuculara, zeytin işleme hatlarından fırıncılık konveyörlerine kadar doğru bant ve aksesuar desteği.',
        'en': 'From packaging machines to spiral coolers, from olive processing lines to bakery conveyors — the right belt and accessory support.',
    },
    'ind_packaging_title': {'tr': 'Paketleme Makineleri',      'en': 'Packaging Machines'},
    'ind_packaging_sub':   {'tr': 'Thermoform · Tray Sealer · Dikey Paketleme', 'en': 'Thermoform · Tray Sealer · Vertical Packaging'},
    'ind_bread_title':     {'tr': 'Ekmek & Tortilla Hatları',  'en': 'Bread & Tortilla Lines'},
    'ind_bread_sub':       {'tr': 'Laminasyon · Soğutma · Paketleme Besleme', 'en': 'Lamination · Cooling · Packaging Feed'},
    'ind_spiral_title':    {'tr': 'Spiral Soğutma',             'en': 'Spiral Cooling'},
    'ind_spiral_sub':      {'tr': 'Fermentasyon · Soğutma · Mayalama Bantları', 'en': 'Fermentation · Cooling · Proofing Belts'},
    'ind_olive_title':     {'tr': 'Zeytin & Meyve İşleme',     'en': 'Olive & Fruit Processing'},
    'ind_olive_sub':       {'tr': 'Kalibrasyon · Seçme · Blanşör · Yıkama', 'en': 'Grading · Sorting · Blanching · Washing'},
    'ind_blancher_title':  {'tr': 'Blanşör & Yıkama',           'en': 'Blancher & Washing'},
    'ind_blancher_sub':    {'tr': 'Turşu · Konserve · Sebze-Meyve Hatları', 'en': 'Pickling · Canning · Fruit-Vegetable Lines'},
    'ind_meat_title':      {'tr': 'Et & Tavukçuluk',            'en': 'Meat & Poultry'},
    'ind_meat_sub':        {'tr': 'Kesimhane · Fileto · Vakum Paketleme', 'en': 'Slaughterhouse · Fillet · Vacuum Packaging'},
    'ind_seafood_title':   {'tr': 'Su Ürünleri',                'en': 'Seafood'},
    'ind_seafood_sub':     {'tr': 'Boyutlandırma · İşleme · Soğutma Hatları', 'en': 'Sizing · Processing · Cooling Lines'},
    'ind_conveyor_title':  {'tr': 'Konveyör Entegrasyonu',      'en': 'Conveyor Integration'},
    'ind_conveyor_sub':    {'tr': 'Komple Hat Tasarımı · Aksesuar Desteği', 'en': 'Complete Line Design · Accessory Support'},

    # CTA
    'cta_title': {
        'tr': 'Projeniz için doğru bandı birlikte seçelim',
        'en': "Let's choose the right belt for your project together",
    },
    'cta_desc': {
        'tr': 'Makine tasarımı aşamasında veya seri üretim tedariki için mühendislik ekibimizle iletişime geçin. Ücretsiz teknik danışmanlık.',
        'en': 'Contact our engineering team during the machine design phase or for mass production supply. Free technical consultation.',
    },
    'cta_quote':   {'tr': 'Teklif İste', 'en': 'Request a Quote'},
    'cta_catalog': {'tr': 'Katalog',     'en': 'Catalog'},

    # Products index
    'products_page_title': {'tr': 'Modüler Bant Ürün Ailesi', 'en': 'Modular Belt Product Family'},
    'products_page_desc':  {
        'tr': 'Hatve ölçüsüne ve uygulamaya göre kategorize edilmiş geniş ürün yelpazemizi keşfedin.',
        'en': 'Explore our wide product range, categorized by pitch size and application.',
    },
    'products_see_models':  {'tr': 'Modelleri gör', 'en': 'See Models'},
    'products_model_count': {'tr': 'ürün modeli',   'en': 'product models'},

    # Product detail
    'product_description':    {'tr': 'Ürün Tanımı',        'en': 'Product Description'},
    'product_specs_title':    {'tr': 'Teknik Özellikler',  'en': 'Technical Specifications'},
    'spec_pitch':             {'tr': 'Hatve',               'en': 'Pitch'},
    'spec_thickness':         {'tr': 'Kalınlık',            'en': 'Thickness'},
    'spec_pin':               {'tr': 'Pim Çapı',            'en': 'Pin Diameter'},
    'spec_pin_suffix':        {'tr': 'Kendinden Kilitli',   'en': 'Self-Locking'},
    'spec_open_area':         {'tr': 'Açıklık Oranı',       'en': 'Open Area'},
    'spec_surface':           {'tr': 'Yüzey Tipi',          'en': 'Surface Type'},
    'spec_materials':         {'tr': 'Malzemeler',          'en': 'Materials'},
    'spec_temp':              {'tr': 'Sıcaklık Dayanımı',   'en': 'Temperature Resistance'},
    'spec_certs':             {'tr': 'Sertifikalar',        'en': 'Certifications'},
    'btn_get_quote_product':  {'tr': 'Bu Ürün İçin Teklif Al', 'en': 'Get a Quote for This Product'},
    'btn_datasheet':          {'tr': 'Teknik Föy (PDF)',    'en': 'Technical Data Sheet (PDF)'},
    'product_usage_title':    {'tr': 'Kullanım Alanları',   'en': 'Usage Areas'},
    'related_products_title': {'tr': 'Benzer Ürünler',      'en': 'Related Products'},
    'open_pct_suffix':        {'tr': 'açık alan',           'en': 'open area'},
    'pitch_suffix':           {'tr': 'hatve',               'en': 'pitch'},
    'open_short':             {'tr': 'açık',                'en': 'open'},
    'no_products_msg': {
        'tr': 'Bu kategoride henüz ürün bulunmuyor.',
        'en': 'No products available in this category yet.',
    },

    # Contact
    'contact_page_title': {'tr': 'İletişim', 'en': 'Contact'},
    'contact_meta_desc':  {
        'tr': "ROLOBAND ile iletişime geçin. Modüler konveyör bantları için teklif alın. İzmir Menderes'teki tesisimizden Türkiye geneline hizmet veriyoruz.",
        'en': 'Contact ROLOBAND. Get a quote for modular conveyor belts. We serve all of Turkey from our facility in Izmir Menderes.',
    },
    'contact_h1':       {'tr': 'Bize Ulaşın', 'en': 'Get in Touch'},
    'contact_subtitle': {
        'tr': 'Projeniz için uygun çözümü birlikte belirleyelim. Teknik ekibimiz 24 saat içinde size dönüş yapar.',
        'en': "Let's determine the right solution for your project together. Our technical team will get back to you within 24 hours.",
    },
    'contact_info_title':      {'tr': 'İletişim Bilgileri', 'en': 'Contact Information'},
    'contact_address_label':   {'tr': 'Adres',     'en': 'Address'},
    'contact_email_label':     {'tr': 'E-posta',   'en': 'Email'},
    'contact_phone_label':     {'tr': 'Telefon',   'en': 'Phone'},
    'contact_instagram_label': {'tr': 'Instagram', 'en': 'Instagram'},
    'contact_hours_title':     {'tr': 'Çalışma Saatleri', 'en': 'Working Hours'},
    'contact_hours_text': {
        'tr': 'Pazartesi - Cuma: 08:30 - 18:00<br>Cumartesi: 09:00 - 14:00',
        'en': 'Monday - Friday: 08:30 - 18:00<br>Saturday: 09:00 - 14:00',
    },
    'contact_form_title': {'tr': 'Teklif Formu', 'en': 'Quote Form'},
    'label_full_name': {'tr': 'Adınız Soyadınız', 'en': 'Full Name'},
    'label_company':   {'tr': 'Firma',             'en': 'Company'},
    'label_email':     {'tr': 'E-posta',           'en': 'Email'},
    'label_phone':     {'tr': 'Telefon',           'en': 'Phone'},
    'label_subject':   {'tr': 'Konu',              'en': 'Subject'},
    'label_message':   {'tr': 'Mesajınız',         'en': 'Message'},
    'form_submit': {'tr': 'Gönder', 'en': 'Send'},
    'form_note': {
        'tr': 'Mesajınız işleme alındıktan sonra teknik ekibimiz en geç 24 saat içinde size geri dönüş yapacaktır.',
        'en': 'After your message is processed, our technical team will get back to you within 24 hours.',
    },
    'placeholder_name':    {'tr': 'Adınız Soyadınız',   'en': 'Your Full Name'},
    'placeholder_company': {'tr': 'Firma adı',           'en': 'Company name'},
    'placeholder_email':   {'tr': 'ornek@firma.com',     'en': 'example@company.com'},
    'placeholder_phone':   {'tr': '+90 555 555 55 55',   'en': '+90 555 555 55 55'},
    'placeholder_subject': {'tr': 'Talebinizin konusu',  'en': 'Subject of your request'},
    'placeholder_message': {
        'tr': 'Uygulamanız, hatve tercihi, bant ölçüsü, malzeme isteği gibi detayları yazabilirsiniz.',
        'en': 'You can write details such as your application, pitch preference, belt size, and material requirements.',
    },
}


def t(key, lang='tr'):
    return TRANSLATIONS.get(key, {}).get(lang) or TRANSLATIONS.get(key, {}).get('tr', key)


def tdb(text, lang='tr'):
    """DB'den gelen sabit metinleri çevirir. Çeviri yoksa orijinal metni döner."""
    if not text or lang == DEFAULT_LANG:
        return text
    return DB_TRANSLATIONS.get(text, {}).get(lang, text)
