# ROLOBAND — Modüler Konveyör Bant B2B Web Sitesi

İzmir Menderes merkezli **ROLOBAND** için Flask tabanlı kurumsal B2B web sitesi ve içerik yönetim paneli. Gıda işleme makinesi imalatçılarına yönelik ürün kataloğu, video destekli anasayfa ve admin panelden yönetilebilen tüm içerik.

> **Hedef kitle:** Inovpack, Karataşı, Arendi, Günal gibi gıda makinesi imalatçıları  
> **Marka:** Açık mavi (#0ea5e9) + beyaz · Endüstriyel + temiz · Türkçe arayüz  
> **Domain:** www.roloband.com

---

## 🚀 Hızlı Başlangıç

### Gereksinimler
- Python 3.10+
- pip
- (opsiyonel) Node yok — frontend tamamen CSS/JS

### Kurulum (3 dakika)

```bash
# 1) Sanal ortam oluştur ve aktive et
python -m venv venv
source venv/bin/activate           # Windows: venv\Scripts\activate

# 2) Bağımlılıkları kur
pip install -r requirements.txt

# 3) Ortam değişkenlerini kopyala ve düzenle
cp .env.example .env
# .env içindeki SECRET_KEY ve ADMIN_PASSWORD değerlerini değiştir!

# 4) Veritabanını oluştur
export FLASK_APP=run.py            # Windows: set FLASK_APP=run.py
flask init-db

# 5) Admin kullanıcısı oluştur (.env'deki ADMIN_EMAIL/PASSWORD kullanılır)
flask create-admin

# 6) Örnek içerikleri yükle (kategoriler, ürünler, sayfalar)
flask seed

# 7) Çalıştır
flask run
```

Site → **http://127.0.0.1:5000**  
Admin → **http://127.0.0.1:5000/admin/login**

Varsayılan admin (`.env`'den):
- E-posta: `info@roloband.com`
- Parola: `ChangeMe2026` ← üretim öncesi mutlaka değiştir!

---

## 📦 Proje Yapısı

```
roloband/
├── app/
│   ├── __init__.py              # create_app() factory
│   ├── extensions.py            # db, login, csrf, ckeditor, cache, limiter
│   ├── models.py                # 8 SQLAlchemy modeli
│   │
│   ├── blueprints/
│   │   ├── public/              # Halka açık site
│   │   │   ├── routes.py        # /, /urunler, /urun/<slug>, /iletisim, ...
│   │   │   └── forms.py         # ContactForm
│   │   └── admin/               # Yönetim paneli
│   │       ├── routes.py        # /admin/* (CRUD + ayarlar)
│   │       └── forms.py         # 7 form sınıfı (WTForms)
│   │
│   ├── utils/
│   │   ├── uploads.py           # save_upload, delete_upload, MIME kontrolleri
│   │   ├── cli.py               # init-db, create-admin, seed komutları
│   │   └── seeder.py            # Katalog seed verisi (5 kategori, 5 ürün)
│   │
│   ├── static/
│   │   ├── css/
│   │   │   ├── main.css         # Public site (~900 satır)
│   │   │   └── admin.css        # Admin paneli (~900 satır)
│   │   ├── js/
│   │   │   ├── main.js          # Hero video, scroll, sayım animasyonları
│   │   │   └── admin.js         # Slug üretici, flash, dosya preview
│   │   └── uploads/             # Kullanıcı yüklemeleri (video/görsel/PDF)
│   │
│   └── templates/
│       ├── public/              # Anasayfa, ürün, iletişim, dinamik sayfa
│       ├── admin/               # 15 admin sayfası
│       └── errors/              # 404, 500
│
├── instance/                    # SQLite veritabanı buraya
├── config.py                    # 3 ortam (dev/prod/test)
├── run.py                       # Uygulama giriş noktası
├── requirements.txt
└── .env.example
```

---

## 🛠 Özellikler

### Halka Açık Site
- **Hero section** — Tam ekran video arkaplan (admin'den yüklenir), slogan, CTA buton, gradient overlay, fadeUp animasyonları
- **Ürün kataloğu** — Kategori bazlı, hatve göstergesi (12.7 / 25.4 / 50.8 mm + Radius + Aksesuar)
- **Ürün detay** — Teknik tablo (hatve, kalınlık, pim çapı, açık alan %, sıcaklık aralığı, sertifika), kullanım alanları, ilgili ürünler, PDF föy indirme, teklif al CTA
- **Dinamik sayfa sistemi** — Hakkımızda, Sektörler, Kalite gibi sayfalar admin'den yönetilir
- **İletişim formu** — Rate limit'li (10/saat), CSRF korumalı, IP loglu
- **SEO uyumlu** — Her sayfada meta title/description, Open Graph, slug bazlı URL
- **Responsive** — Mobil, tablet, masaüstü breakpoint'leri

### Admin Paneli (/admin)
- 🔐 Flask-Login + bcrypt parola, role tabanlı (admin/editor)
- 📊 Dashboard — ürün/kategori/sayfa/mesaj istatistikleri, son mesajlar, hızlı eylemler
- 📝 **CKEditor 5** — Tüm zengin metin alanlarında, inline görsel yükleme destekli
- 🎬 **Hero video yönetimi** — Yükle, önizle, slogan/CTA düzenle (MP4/WebM, max 200MB)
- 🏷 Ürün CRUD — Tüm teknik özellikler (hatve, kalınlık, pim, açıklık %, malzeme, sıcaklık aralığı, sertifika, PDF föy, kapak görseli)
- 📂 Kategori CRUD — Hatve bazlı gruplandırma, sıralama, kapak görseli
- 📄 Sayfa CRUD — SEO meta'lar, menüde görünüm, taslak/yayında, kapak görseli
- 🧭 Menü yöneticisi — Üst menü ögelerini ekle/sırala/aktif-pasif
- 📧 Mesaj merkezi — Okunmadı badge'i sidebar'da, detay görünümü, e-posta ile yanıt linki
- ⚙ Genel ayarlar — İletişim bilgileri, sosyal medya, footer metni, sertifikalar

### Güvenlik
- ✅ CSRF koruması (Flask-WTF)
- ✅ Rate limiting (Flask-Limiter) — login 20/saat, iletişim 10/saat
- ✅ Parola hash'leme (werkzeug.security)
- ✅ XSS koruması (Jinja2 autoescape)
- ✅ Reserved slug'lar (admin, static, urunler vb. ele geçirilemez)
- ✅ Dosya tipi whitelist (görsel/video/PDF için ayrı extension listeleri)
- ✅ MAX_CONTENT_LENGTH limiti (200MB)

---

## 🔧 CLI Komutları

```bash
flask init-db           # Veritabanı tablolarını oluştur
flask create-admin      # .env'deki ADMIN_EMAIL/PASSWORD ile admin oluştur
flask seed              # Kategoriler, ürünler, sayfalar ve site ayarlarını ekler
flask run               # Geliştirme sunucusu
flask db migrate -m "..."  # Alembic migration (model değişimi sonrası)
flask db upgrade        # Migration'ı uygula
```

---

## 🌐 Üretime Alma (Production)

### 1. Ortam değişkenleri
```bash
# .env
FLASK_ENV=production
SECRET_KEY=<güçlü-rastgele-değer>           # Örn: python -c "import secrets; print(secrets.token_hex(32))"
DATABASE_URL=postgresql://user:pass@host/roloband   # SQLite yerine PostgreSQL önerilir
ADMIN_EMAIL=info@roloband.com
ADMIN_PASSWORD=<güçlü-parola>
```

### 2. Gunicorn ile çalıştır
```bash
pip install gunicorn psycopg2-binary
gunicorn -w 4 -b 0.0.0.0:8000 "run:app"
```

### 3. Nginx reverse proxy (örnek)
```nginx
server {
    listen 80;
    server_name www.roloband.com roloband.com;

    client_max_body_size 200M;     # video yükleme için

    location /static/ {
        alias /var/www/roloband/app/static/;
        expires 30d;
    }

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

### 4. SSL (Let's Encrypt)
```bash
sudo certbot --nginx -d www.roloband.com -d roloband.com
```

### 5. systemd servisi (örnek)
```ini
# /etc/systemd/system/roloband.service
[Unit]
Description=ROLOBAND Web
After=network.target

[Service]
User=www-data
WorkingDirectory=/var/www/roloband
EnvironmentFile=/var/www/roloband/.env
ExecStart=/var/www/roloband/venv/bin/gunicorn -w 4 -b 127.0.0.1:8000 "run:app"
Restart=always

[Install]
WantedBy=multi-user.target
```

---

## 🎬 Hero Video İpuçları

Admin panel → **Hero / Video Ayarları** sayfasından video yükle. Önerilen format:

| Özellik     | Değer                          |
|-------------|--------------------------------|
| Format      | MP4 (H.264) veya WebM          |
| Çözünürlük  | 1920×1080 veya 1280×720        |
| Süre        | 10-30 saniye (seamless loop)   |
| Ses         | **Yok** (autoplay için zorunlu)|
| Boyut       | < 50MB (sıkıştırılmış)         |
| İçerik      | Üretim hattı / hijyenik tesis  |

Yüklemeden önce **HandBrake** ile sıkıştırırsan yükleme süresi ve hosting maliyeti ciddi düşer.  
Mobil cihazlar için **poster görseli** de yüklemeyi unutma — düşük bağlantıda video yerine bu gösterilir.

---

## 📋 İçerik Stratejisi

### Mevcut Seed İçeriği
- **5 Kategori**: 12.7mm, 25.4mm, 50.8mm hatve + Dönüşlü (Radius) + Aksesuar
- **5 Ürün**: Seri 1270, 1271, 2500, 2535, 5000 (tüm teknik specs)
- **3 Sayfa**: Hakkımızda, Sektörler, Kalite & Sertifikalar
- **8 Hedef sektör**: Et-kümes hayvanı, balık, ekmek-pastacılık, meyve-sebze, içecek, hazır gıda, paketleme, lojistik

### Yeni Ürün/Kategori Ekleme
1. Admin → Ürünler/Kategoriler → **+ Yeni**
2. Slug otomatik oluşur (boş bırakırsan başlıktan üretilir)
3. Teknik özellikleri doldur, kapak görseli yükle, PDF föy ekle
4. **Öne Çıkar** işaretliyse anasayfada görünür

---

## 🐛 Sık Karşılaşılan Sorunlar

**Veritabanı bulunamadı hatası:**
```bash
flask init-db
```

**Admin login olamıyorum:**
```bash
flask create-admin   # .env'deki parolayı kullanır
```

**Seed komutu hata veriyor:**
DB temizse tekrar dene; mevcut kayıtlar üzerine yazılmaz, yalnızca eksik olanlar eklenir.

**Hero video gözükmüyor:**
- Admin → Hero ayarları → video yüklendiyse path'in `/static/uploads/videos/...` olduğunu kontrol et
- `app/static/uploads/videos/` klasörü var mı bak
- Tarayıcıda DevTools → Network → mp4 dosyası 200 mü?

**413 Request Entity Too Large:**
`.env` içinde `MAX_CONTENT_LENGTH_MB` değerini artır + Nginx'te `client_max_body_size` ayarla.

---

## 📝 Lisans

Tescilli — © 2026 ROLOBAND. Tüm hakları saklıdır.

---

## 🤝 İletişim

- **Web**: www.roloband.com
- **E-posta**: info@roloband.com
- **Instagram**: [@rolobandmoduler](https://instagram.com/rolobandmoduler)
- **Adres**: Oğlananası Atatürk, 1. Cd. No:54, 35471 Menderes/İzmir
