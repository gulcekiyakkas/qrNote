from flask import Flask, render_template, request
import qrcode
import uuid
import os
import json

app = Flask(__name__)

# Klasör ayarları
QR_FOLDER = "static/qrcodes"
os.makedirs(QR_FOLDER, exist_ok=True)

# JSON dosyası
NOTES_FILE = "notes.json"


# -------- JSON LOAD & SAVE -------- #

def load_notes():
    """JSON dosyasından notları yükle."""
    if not os.path.exists(NOTES_FILE):
        return {}
    with open(NOTES_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except:
            return {}  # dosya bozuksa boş dön


def save_notes(notes):
    """Notları JSON dosyasına kaydet."""
    with open(NOTES_FILE, "w", encoding="utf-8") as f:
        json.dump(notes, f, ensure_ascii=False, indent=4)


# -------- ANA SAYFA -------- #

@app.route("/", methods=["GET", "POST"])
def index():
    qr_path = None
    qr_link = None

    if request.method == "POST":
        note = request.form.get("note")
        password = request.form.get("password") or ""

        if note:
            note_id = str(uuid.uuid4())

            # JSON'a kaydet
            notes = load_notes()
            notes[note_id] = {
                "text": note,
                "password": password
            }
            save_notes(notes)

            # Telefon için IP tabanlı link
            qr_link = f"http://192.168.1.105:5000/note/{note_id}"

            # QR kod oluştur
            img = qrcode.make(qr_link)
            qr_path = os.path.join(QR_FOLDER, f"{note_id}.png")
            img.save(qr_path)

            return render_template("index.html", qr_path=qr_path, qr_link=qr_link)

    return render_template("index.html", qr_path=None)


# -------- NOT GÖRÜNTÜLEME SAYFASI (ŞİFRELİ) -------- #

@app.route("/note/<note_id>", methods=["GET", "POST"])
def show_note(note_id):
    notes = load_notes()

    if note_id not in notes:
        return render_template("note.html", note="Not bulunamadı.")

    note_data = notes[note_id]
    required_password = note_data.get("password", "")

    # Şifre yoksa direkt göster
    if required_password == "":
        return render_template("note.html", note=note_data["text"])

    # POST → şifre kontrolü
    if request.method == "POST":
        entered = request.form.get("password", "")

        if entered == required_password:
            return render_template("note.html", note=note_data["text"])
        else:
            return render_template("password.html", error="Şifre yanlış.")

    # GET → şifre ekranını göster
    return render_template("password.html", error=None)


# -------- SUNUCU ÇALIŞTIR -------- #

if __name__ == "__main__":
    # Telefonun aynı ağdan erişebilmesi için host 0.0.0.0 olmalı
    app.run(host="0.0.0.0", port=5000, debug=True)
