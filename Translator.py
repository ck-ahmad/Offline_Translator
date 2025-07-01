from flask import Flask, render_template, request
from googletrans import Translator
import os

app = Flask(__name__)
translator = Translator()

# Full language mapping
language_mapping = {
    'English': 'en', 'Spanish': 'es', 'French': 'fr', 'German': 'de', 'Japanese': 'ja', 'Chinese': 'zh-cn',
    'Russian': 'ru', 'Italian': 'it', 'Portuguese': 'pt', 'Arabic': 'ar', 'Hindi': 'hi', 'Bengali': 'bn',
    'Korean': 'ko', 'Vietnamese': 'vi', 'Turkish': 'tr', 'Persian': 'fa', 'Urdu': 'ur', 'Dutch': 'nl',
    'Greek': 'el', 'Hebrew': 'he', 'Polish': 'pl', 'Swedish': 'sv', 'Danish': 'da', 'Norwegian': 'no',
    'Finnish': 'fi', 'Czech': 'cs', 'Hungarian': 'hu', 'Romanian': 'ro', 'Thai': 'th', 'Indonesian': 'id',
    'Malay': 'ms', 'Filipino': 'fil', 'Swahili': 'sw', 'Zulu': 'zu', 'Xhosa': 'xh', 'Yoruba': 'yo',
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

    if request.method == 'POST':
        original_text = request.form['text']
        selected_lang = request.form['language']
        lang_code = language_mapping.get(selected_lang, 'en')

        if original_text.strip():
            try:
                result = translator.translate(original_text, dest=lang_code)
                translated_text = result.text
            except Exception as e:
                translated_text = f"Translation error: {str(e)}"

    return render_template(
        'index.html',
        languages=language_mapping.keys(),
        translated=translated_text,
        original=original_text,
        selected_lang=selected_lang
    )

if __name__ == "__main__":
    app.run(debug=True)
