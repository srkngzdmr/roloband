# ROLOBAND — Modüler Bant Web Sitesi

B2B odaklı Flask tabanlı kurumsal web sitesi. Admin paneli üzerinden tüm içerikler yönetilebilir.

## Hızlı Başlangıç

```bash
# 1. Bağımlılıkları kur
pip install -r requirements.txt

# 2. Ortam dosyasını oluştur
cp .env.example .env
# .env dosyasını düzenle (SECRET_KEY, vb.)

# 3. Veritabanını başlat
flask --app run init-db

# 4. Admin kullanıcısı oluştur
flask --app run create-admin

# 5. Demo verileri yükle (opsiyonel)
flask --app run seed

# 6. Sunucuyu başlat
python run.py
```

Tarayıcıda: http://localhost:5000  
Admin paneli: http://localhost:5000/admin/login

## Admin Giriş Bilgileri (geliştirme)

- **E-posta:** admin@roloband.com  
- **Şifre:** roloband2024  
> ⚠️ Production'a almadan önce mutlaka değiştir!

## Klasör Yapısı

```
roloband/
├── app/
│   ├── __init__.py          # Application factory
│   ├── models.py            # Veritabanı modelleri
│   ├── extensions.py        # Flask uzantıları
│   ├── blueprints/
│   │   ├── public/          # Ön yüz route + form
│   │   └── admin/           # Admin panel route + form
│   ├── utils/
│   │   ├── uploads.py       # Dosya yükleme yardımcıları
│   │   ├── cli.py           # Flask CLI komutları
│   │   └── seeder.py        # Demo veri seeder
│   ├── static/
│   │   ├── css/             # main.css + admin.css
│   │   ├── js/              # main.js + admin.js
│   │   └── uploads/         # Yüklenen medya dosyaları
│   └── templates/
│       ├── public/          # Ön yüz şablonları
│       ├── admin/           # Admin panel şablonları
│       └── errors/          # 404 + 500 hata sayfaları
├── instance/                # SQLite DB (otomatik oluşur)
├── config.py
├── run.py
├── requirements.txt
└── .env.example
```

## Admin Panel Özellikleri

- 📄 **Sayfalar** — Dinamik sayfa oluştur/düzenle (CKEditor ile)
- 📦 **Ürünler & Kategoriler** — Modüler bant modelleri yönetimi
- 🎬 **Hero Ayarları** — Video yükleme, slogan, CTA butonu
- ⚙️ **Genel Ayarlar** — Site adı, iletişim bilgileri, SEO
- 📋 **Menü Yönetimi** — Navigasyon linkleri
- 📩 **Mesajlar** — İletişim formu gelen kutusu

## Production Notları

- `SECRET_KEY` .env dosyasında güçlü bir değere set edilmeli
- `FLASK_ENV=production` olmalı
- Nginx + Gunicorn ile deploy edilmesi önerilir
- SQLite yerine PostgreSQL kullanmak için `DATABASE_URL` güncelle
