# 📦 Klasör Arşivleme Scripti (Zaman Damgalı .zip Oluşturucu)

Bu Python scripti, belirlenen bir klasörü `.zip` formatında sıkıştırarak masaüstüne kaydeder. Dosya adı, çalıştırıldığı andaki tarih ve saate göre otomatik oluşturulur.

---

## 🚀 Özellikler

- Belirlenen klasörü `.zip` dosyasına dönüştürür
- Zaman damgası kullanarak arşiv ismini dinamik olarak oluşturur
- `.zip` dosyasını belirlenen hedef dizine kaydeder
- Hedef klasör yoksa otomatik olarak oluşturur
- Hataları yakalayarak kullanıcıyı bilgilendirir

---

## 🧱 Kullanılan Python Modülleri

| Modül      | Açıklama                                | Harici Kurulum Gerekir mi |
|------------|------------------------------------------|-----------------------------|
| `os`       | Dizin ve dosya işlemleri                 | ❌ Hayır (yerleşik)         |
| `shutil`   | Arşiv oluşturma işlemleri                | ❌ Hayır (yerleşik)         |
| `datetime` | Zaman damgası oluşturma                  | ❌ Hayır (yerleşik)         |

> 📌 Not: Script, herhangi bir harici kütüphane kullanmaz.

---

## 🔧 Yapılandırma

Kodun başında bulunan şu değişkenleri ihtiyacınıza göre düzenleyin:

```python
kaynak_dizin = r"C:\Users\user\Desktop\Deneme"      # Sıkıştırılacak klasör
hedef_dizin = r"C:\Users\user\Desktop"      # .zip dosyasının kaydedileceği yer
```

---

## 📝 Örnek Çıktı

Script çalıştırıldığında aşağıdaki gibi bir çıktı üretir:

```
📦 Sıkıştırma başlatılıyor...
✅ Sıkıştırma tamamlandı: C:\Users\users\Desktop\08-08-2025-13-28.zip
```


## 📜 Lisans

Bu proje MIT lisansı ile lisanslanmıştır. Detaylar için `LICENSE` dosyasına bakabilirsiniz.

---
