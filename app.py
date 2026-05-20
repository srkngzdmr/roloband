"""ROLOBAND uygulama giriş noktası."""
from app import create_app
from app.extensions import db
from app.utils.seeder import run_seed
from app.models import AdminUser
from werkzeug.security import generate_password_hash

app = create_app()

# DB tabloları ve seed — gunicorn her worker'da çalıştırmamak için try/except
with app.app_context():
    try:
        db.create_all()
    except Exception as e:
        print(f"DB create_all error: {e}")
    
    try:
        if not AdminUser.query.first():
            admin = AdminUser(
                email="admin@roloband.com",
                password_hash=generate_password_hash("roloband2024"),
                full_name="Site Yöneticisi",
                role="admin"
            )
            db.session.add(admin)
            db.session.commit()
            run_seed()
            print("DB initialized and seeded.")
    except Exception as e:
        print(f"Seed error: {e}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
