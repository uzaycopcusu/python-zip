import os
import shutil
from datetime import datetime

# Ayarlar
kaynak_dizin = r"C:\Users\user\Desktop\Deneme"  # Sıkıştırılacak klasör
hedef_dizin = r"C:\Users\user\Desktop"  # .zip dosyasının kaydedileceği yer

# Hedef dizini oluştur (varsa dokunmaz)
os.makedirs(hedef_dizin, exist_ok=True)

# Zaman damgalı arşiv ismi (uzantısız)
zaman = datetime.now().strftime("%d-%m-%Y-%H-%M")
arsiv_adi = os.path.join(hedef_dizin, zaman)

# make_archive otomatik olarak .zip uzantısı ekler
try:
    print("📦 Sıkıştırma başlatılıyor...")
    shutil.make_archive(arsiv_adi, 'zip', root_dir=os.path.dirname(kaynak_dizin), base_dir=os.path.basename(kaynak_dizin))
    print(f"✅ Sıkıştırma tamamlandı: {arsiv_adi}.zip")
except Exception as e:
    print("❌ Hata oluştu:", e)
