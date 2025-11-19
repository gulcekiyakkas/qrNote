

# 🌈 QR Note Generator — Şifreli QR Kodlu Not Paylaşım Uygulaması

Hızlı, güvenli ve şifreli bir QR kod not uygulaması.  
Notunu yaz → İstersen şifre koy → QR kod üret → Telefonda aç! 🔥

Bu proje Python + Flask ile geliştirilmiş olup, **modern arayüz**,  
**şifreli not desteği**, **kalıcı JSON saklama** ve  
**mobil QR ile erişim** gibi özelliklere sahiptir.

---

## 🚀 Özellikler

✔ **Şifreli Not (Password Protected)**  
✔ **QR Kod ile Hızlı Paylaşım**  
✔ **Telefonla Direkt Açılır**  
✔ **Modern UI & Responsive Tasarım**  
✔ **JSON ile Kalıcı Veri Saklama**  
✔ **Aynı WiFi Üzerinden Mobil Erişim**  
✔ **Güvenli Not Paylaşımı**  
✔ **Temiz Flask Yapısı**

---

## 🎥 Demo (Ekran Görüntüleri)

### 🟣 Ana Sayfa
images /fdtNUxb - Imgur.png

### 🟣 QR Kod Oluşturma
images/vbVtrgJ - Imgur.png

### 🟣 Şifre Koruma Ekranı
images/kciYBP0 - Imgur.png

### 🟣 Not Görüntüleme
images/j2vkFSd - Imgur.png

---

## 🛠 Teknolojiler

- **Python (Flask)**
- **HTML / CSS**
- **QR Code Library**
- **JSON Data Storage**
- **Local Network Routing (192.168.x.x)**

---

## 📦 Proje Yapısı

qrNote/
│── appQr.py
│── notes.json
│── requirements.txt
│── README.md
│── static/
│ ├── style.css
│ └── qrcodes/
│── templates/
├── index.html
├── note.html
└── password.html

---

## ⚙️ Kurulum

### 1️⃣ Depoyu Klonla

git clone https://github.com/gulcekiyakkas/qrNote.git
cd qrNote

### 2️⃣ Gereksinimleri Kur

pip install -r requirements.txt

### 3️⃣ Sunucuyu Başlat

python appQr.py

---

## 📱 Telefonda Nasıl Açılır?

> Telefon ve bilgisayar **aynı WiFi’da** olmalı.

Sunucuyu şu şekilde başlat:

```python
app.run(host="0.0.0.0", port=5000)
Bilgisayarının IP’sini öğren:

nginx
Kodu kopyala
ipconfig
Örnek IP:

Kodu kopyala
192.168.1.105
Telefondan aç:

cpp
Kodu kopyala
http://192.168.1.105:5000
QR kodlar da bu IP’yi içerir → telefonda direkt açılır 🎉

🔐 Şifreli Not Özelliği
Not oluştururken şifre girersen, QR taranınca şifre ekranı çıkar

Şifre doğru → not açılır

Yanlış → “Şifre yanlış” uyarısı

Şifre girilmezse, not direkt görüntülenir

🌟 Geliştirmeye Açık Özellikler
Bu projeyi daha da büyütmek istersen ekleyebilirim:

🎨 Renkli QR Kodlar

🕒 24 Saat Sonra Kendini Sıfırlayan Notlar

📤 Paylaş Butonu (WhatsApp, Messenger)

🧹 Admin Paneli (Not yönetimi)

🔒 AES ile Şifreli Not

☁️ Online Deployment (Render / Vercel / PythonAnywhere)

## 👤 Geliştirici
Gülce Kıyakkaş
Makine Mühendisliği Öğrencisi • Yapay Zeka ve Yazılım Geliştirme

##⭐ Destek
Projeyi beğendiysen bir ⭐ bırakabilirsin 🌟
Fork’layıp geliştirmek istersen memnuniyet duyarım!

---

