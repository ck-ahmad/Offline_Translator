<h1 align="center">🌐 Offline Translator – Multilingual Voice & Text Translator</h1>

<p align="center">
  A fully offline, speech-enabled translator built using <strong>Flask</strong>, <strong>Python</strong>, and <strong>Googletrans</strong>. <br>
  Translate between 100+ languages using voice commands or text input, with speech output and zero internet dependency.
</p>

---

<p align="center">
  <a href="https://github.com/ck-ahmad/Offline_Translator/blob/main/output(compress-video-online.com)%20(1).mp4" target="_blank">
    <img src="https://img.shields.io/badge/Live-Demo-blueviolet?style=for-the-badge&logo=github" alt="Demo Video">
  </a>
</p>

---

## 🌍 Why Offline Translator?

> Designed for privacy, speed, and portability. This translator runs completely offline with support for text-to-speech (TTS), voice input, and multilingual translation using the `googletrans` and `speech_recognition` libraries.

---

## 🔥 Highlights (July 2025)

- 🎤 **Voice Input** – Speak a sentence and get it translated
- 🧠 **TTS Output** – Translated text is spoken aloud using `pyttsx3`
- 🌐 **100+ Languages** – Powered by Google Translate API (offline wrapper)
- 🔌 **Offline Mode** – No internet required after setup
- 💡 **Flask UI** – Clean and minimal dark-themed web interface

---

## 🧠 Tech Stack

| Feature        | Technology Used                            |
|----------------|---------------------------------------------|
| Backend        | Flask, Flask-WTF                            |
| Translation    | googletrans (offline wrapper)               |
| Voice Input    | speech_recognition, PyAudio                 |
| Voice Output   | pyttsx3 (offline text-to-speech)            |
| Frontend       | HTML, CSS, JavaScript (Bootstrap optional) |

---

## 💬 Supported Languages

- English ↔ Urdu
- English ↔ Arabic
- English ↔ French
- English ↔ Chinese
- And 100+ more! Just set `source` and `destination` language codes in UI.

---

## 📁 Folder Structure

```

Offline-Translator/
│
├── app.py                # Main Flask application
├── templates/            # UI HTML pages
│   └── index.html
├── static/               # Optional: Custom styles, JS
├── voice/                # Voice control modules
│   ├── listener.py       # Handles speech recognition
│   └── speaker.py        # Handles pyttsx3 TTS
├── config.json           # (Optional) Language config
├── requirements.txt      # Python dependencies
└── README.md             # You’re here

````

---

## 🚀 How to Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/Ahmadleo-tech/Offline-Translator.git
cd Offline-Translator

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python app.py

# Visit: http://127.0.0.1:5000/
````

---

## 📦 Example Usage

* Select `From Language`: English
* Select `To Language`: Urdu
* Click **🎤 Speak** or type a sentence
* Click **Translate**
* Hear the output with TTS 🎧

---

## 🌐 Demo

🚧 Hosted version coming soon
🎥 Demo video will be uploaded here...

---

## 🧾 requirements.txt

```
Flask
googletrans==4.0.0-rc1
speechrecognition
pyttsx3
pyaudio
```

> ✅ Compatible with Windows/Linux. May require microphone permissions.

---

## 👨‍💻 Author

**Ahmad Leo**
🔗 [GitHub](https://github.com/ck-ahmad)<br>
📫 Contact details in profile

---

## 📄 License

MIT License — Free to use for personal and educational projects.

---

```

Let me know if you'd like me to generate:

- ✅ `config.json` with language settings  
- ✅ `.gitignore` for Python + Flask  
- ✅ `app.py` starter template for this project  
- ✅ Custom UI (dark with speech icon like Galaxify)

Just say the word and I’ll drop the files.
```
