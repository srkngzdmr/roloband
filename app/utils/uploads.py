from __future__ import annotations
from typing import Optional
"""Yükleme yardımcıları (görsel/video/pdf)."""
import os
import uuid
from pathlib import Path
from werkzeug.utils import secure_filename
from flask import current_app


def _ext(filename: str) -> str:
    return filename.rsplit(".", 1)[-1].lower() if "." in filename else ""


def allowed_image(filename: str) -> bool:
    return _ext(filename) in current_app.config["ALLOWED_IMAGE_EXTENSIONS"]


def allowed_video(filename: str) -> bool:
    return _ext(filename) in current_app.config["ALLOWED_VIDEO_EXTENSIONS"]


def save_upload(file_storage, subfolder: str = "images") -> Optional[str]:
    """Yüklenen dosyayı kaydeder, web yolu (örn. /static/uploads/images/xxx.jpg) döner."""
    if not file_storage or not file_storage.filename:
        return None

    ext = _ext(file_storage.filename)
    if subfolder in ("images", "products") and ext not in current_app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return None
    if subfolder == "videos" and ext not in current_app.config["ALLOWED_VIDEO_EXTENSIONS"]:
        return None

    safe = secure_filename(file_storage.filename)
    unique = f"{uuid.uuid4().hex[:12]}-{safe}"
    target_dir: Path = current_app.config["UPLOAD_FOLDER"] / subfolder
    target_dir.mkdir(parents=True, exist_ok=True)
    full_path = target_dir / unique
    file_storage.save(str(full_path))

    return f"/static/uploads/{subfolder}/{unique}"


def delete_upload(web_path: Optional[str]) -> None:
    """Web yoluyla verilen dosyayı diskten siler (best-effort)."""
    if not web_path:
        return
    if not web_path.startswith("/static/uploads/"):
        return
    rel = web_path.replace("/static/uploads/", "")
    full = current_app.config["UPLOAD_FOLDER"] / rel
    try:
        if full.exists():
            full.unlink()
    except OSError:
        pass
