// ROLOBAND Admin Panel — minimal JS
document.addEventListener('DOMContentLoaded', () => {

  // Slug otomatik üretimi (yalnızca yeni kayıt için)
  const titleInput = document.querySelector('input[name="title"], input[name="name"]');
  const slugInput  = document.querySelector('input[name="slug"]');

  if (titleInput && slugInput && !slugInput.value) {
    titleInput.addEventListener('blur', () => {
      if (!slugInput.value && titleInput.value) {
        slugInput.value = slugify(titleInput.value);
      }
    });
  }

  function slugify(str) {
    const trMap = { 'ç':'c','Ç':'c','ğ':'g','Ğ':'g','ı':'i','İ':'i','ö':'o','Ö':'o','ş':'s','Ş':'s','ü':'u','Ü':'u' };
    return str
      .split('').map(c => trMap[c] || c).join('')
      .toLowerCase()
      .replace(/[^a-z0-9\s-]/g, '')
      .trim()
      .replace(/\s+/g, '-')
      .replace(/-+/g, '-');
  }

  // Flash mesajları 5sn sonra otomatik kapansın
  document.querySelectorAll('.admin-flash').forEach(el => {
    setTimeout(() => {
      el.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
      el.style.opacity = '0';
      el.style.transform = 'translateY(-10px)';
      setTimeout(() => el.remove(), 400);
    }, 5000);
  });

  // Dosya yükleme preview (image)
  document.querySelectorAll('input[type=file][accept*="image"]').forEach(input => {
    input.addEventListener('change', e => {
      const file = e.target.files[0];
      if (!file) return;

      const reader = new FileReader();
      reader.onload = ev => {
        let preview = input.parentElement.querySelector('.file-preview-new');
        if (!preview) {
          preview = document.createElement('div');
          preview.className = 'file-preview-new current-image';
          preview.style.marginTop = '0.75rem';
          input.parentElement.appendChild(preview);
        }
        preview.innerHTML = `<img src="${ev.target.result}" alt="" style="max-height:180px;"><div class="muted">Yeni görsel (henüz kaydedilmedi)</div>`;
      };
      reader.readAsDataURL(file);
    });
  });

});
