# from flask import Flask, render_template, request
# from deep_translator import GoogleTranslator

# app = Flask(__name__)

# # Full language mapping
# language_mapping = {
#     'English': 'en', 'Spanish': 'es', 'French': 'fr', 'German': 'de', 'Japanese': 'ja', 'Chinese': 'zh-cn',
#     'Russian': 'ru', 'Italian': 'it', 'Portuguese': 'pt', 'Arabic': 'ar', 'Hindi': 'hi', 'Bengali': 'bn',
#     'Korean': 'ko', 'Vietnamese': 'vi', 'Turkish': 'tr', 'Persian': 'fa', 'Urdu': 'ur', 'Dutch': 'nl',
#     'Greek': 'el', 'Hebrew': 'he', 'Polish': 'pl', 'Swedish': 'sv', 'Danish': 'da', 'Norwegian': 'no',
#     'Finnish': 'fi', 'Czech': 'cs', 'Hungarian': 'hu', 'Romanian': 'ro', 'Thai': 'th', 'Indonesian': 'id',
#     'Malay': 'ms', 'Filipino': 'tl', 'Swahili': 'sw', 'Zulu': 'zu', 'Xhosa': 'xh', 'Yoruba': 'yo',
#     'Igbo': 'ig', 'Amharic': 'am', 'Hausa': 'ha', 'Punjabi': 'pa', 'Tamil': 'ta', 'Telugu': 'te',
#     'Gujarati': 'gu', 'Marathi': 'mr', 'Kannada': 'kn', 'Malayalam': 'ml', 'Sinhala': 'si', 'Burmese': 'my',
#     'Khmer': 'km', 'Lao': 'lo', 'Mongolian': 'mn', 'Nepali': 'ne', 'Pashto': 'ps', 'Somali': 'so',
#     'Tigrinya': 'ti', 'Uzbek': 'uz', 'Kazakh': 'kk', 'Georgian': 'ka', 'Armenian': 'hy', 'Azerbaijani': 'az',
#     'Albanian': 'sq', 'Bosnian': 'bs', 'Serbian': 'sr', 'Croatian': 'hr', 'Slovak': 'sk', 'Slovenian': 'sl',
#     'Latvian': 'lv', 'Lithuanian': 'lt', 'Estonian': 'et', 'Icelandic': 'is', 'Macedonian': 'mk',
#     'Bulgarian': 'bg', 'Maltese': 'mt', 'Welsh': 'cy', 'Irish': 'ga', 'Gaelic': 'gd'
# }

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     translated_text = ""
#     original_text = ""
#     selected_lang = "English"

#     if request.method == 'POST':
#         original_text = request.form['text']
#         selected_lang = request.form['language']
#         lang_code = language_mapping.get(selected_lang, 'en')

#         if original_text.strip():
#             try:
#                 translated_text = GoogleTranslator(source='auto', target=lang_code).translate(original_text)
#             except Exception as e:
#                 translated_text = f"Translation error: {str(e)}"

#     return render_template(
#         'index.html',
#         languages=language_mapping.keys(),
#         translated=translated_text,
#         original=original_text,
#         selected_lang=selected_lang
#     )

# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, render_template, request
from deep_translator import GoogleTranslator
from gtts import gTTS
import os
import uuid

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/audio'

# Create the audio folder if it doesn't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

language_mapping = {
    'English': 'en', 'Spanish': 'es', 'French': 'fr', 'German': 'de', 'Japanese': 'ja', 'Chinese': 'zh-cn',
    'Russian': 'ru', 'Italian': 'it', 'Portuguese': 'pt', 'Arabic': 'ar', 'Hindi': 'hi', 'Bengali': 'bn',
    'Korean': 'ko', 'Vietnamese': 'vi', 'Turkish': 'tr', 'Persian': 'fa', 'Urdu': 'ur', 'Dutch': 'nl',
    'Greek': 'el', 'Hebrew': 'he', 'Polish': 'pl', 'Swedish': 'sv', 'Danish': 'da', 'Norwegian': 'no',
    'Finnish': 'fi', 'Czech': 'cs', 'Hungarian': 'hu', 'Romanian': 'ro', 'Thai': 'th', 'Indonesian': 'id',
    'Malay': 'ms', 'Filipino': 'tl', 'Swahili': 'sw', 'Zulu': 'zu', 'Xhosa': 'xh', 'Yoruba': 'yo',
    'Igbo': 'ig', 'Amharic': 'am', 'Hausa': 'ha', 'Punjabi': 'pa', 'Tamil': 'ta', 'Telugu': 'te',
    'Gujarati': 'gu', 'Marathi': 'mr', 'Kannada': 'kn', 'Malayalam': 'ml', 'Sinhala': 'si', 'Burmese': 'my',
    'Khmer': 'km', 'Lao': 'lo', 'Mongolian': 'mn', 'Nepali': 'ne', 'Pashto': 'ps', 'Somali': 'so',
    'Tigrinya': 'ti', 'Uzbek': 'uz', 'Kazakh': 'kk', 'Georgian': 'ka', 'Armenian': 'hy', 'Azerbaijani': 'az',
    'Albanian': 'sq', 'Bosnian': 'bs', 'Serbian': 'sr', 'Croatian': 'hr', 'Slovak': 'sk', 'Slovenian': 'sl',
    'Latvian': 'lv', 'Lithuanian': 'lt', 'Estonian': 'et', 'Icelandic': 'is', 'Macedonian': 'mk',
    'Bulgarian': 'bg', 'Maltese': 'mt', 'Welsh': 'cy', 'Irish': 'ga', 'Gaelic': 'gd'
}

@app.route('/', methods=['GET', 'POST'])
def index():
    translated_text = ""
    original_text = ""
    selected_lang = "English"
    audio_file = ""

    if request.method == 'POST':
        original_text = request.form['text']
        selected_lang = request.form['language']
        lang_code = language_mapping.get(selected_lang, 'en')

        if original_text.strip():
            try:
                translated_text = GoogleTranslator(source='auto', target=lang_code).translate(original_text)

                # Generate TTS
                tts = gTTS(text=translated_text, lang=lang_code)
                filename = f"{uuid.uuid4()}.mp3"
                audio_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                tts.save(audio_path)
                audio_file = f"/static/audio/{filename}"

            except Exception as e:
                translated_text = f"Translation error: {str(e)}"

    return render_template(
        'index.html',
        languages=language_mapping.keys(),
        translated=translated_text,
        original=original_text,
        selected_lang=selected_lang,
        audio_file=audio_file
    )

if __name__ == "__main__":
    app.run(debug=True)

