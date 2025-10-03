from flask import Flask, render_template, request
import langid

app = Flask(__name__)

# Mapping of ISO language codes → full names
LANGUAGE_NAMES = {
    "af": "Afrikaans", "am": "Amharic", "ar": "Arabic", "bg": "Bulgarian",
    "bn": "Bengali", "ca": "Catalan", "cs": "Czech", "cy": "Welsh",
    "da": "Danish", "de": "German", "el": "Greek", "en": "English",
    "es": "Spanish", "et": "Estonian", "fa": "Persian", "fi": "Finnish",
    "fr": "French", "gu": "Gujarati", "he": "Hebrew", "hi": "Hindi",
    "hr": "Croatian", "hu": "Hungarian", "id": "Indonesian", "it": "Italian",
    "ja": "Japanese", "kn": "Kannada", "ko": "Korean", "lt": "Lithuanian",
    "lv": "Latvian", "ml": "Malayalam", "mr": "Marathi", "ne": "Nepali",
    "nl": "Dutch", "no": "Norwegian", "pa": "Punjabi", "pl": "Polish",
    "pt": "Portuguese", "ro": "Romanian", "ru": "Russian", "sk": "Slovak",
    "sl": "Slovenian", "so": "Somali", "sq": "Albanian", "sv": "Swedish",
    "sw": "Swahili", "ta": "Tamil", "te": "Telugu", "th": "Thai",
    "tl": "Tagalog", "tr": "Turkish", "uk": "Ukrainian", "ur": "Urdu",
    "vi": "Vietnamese", "zh": "Chinese"
}

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    full_lang = None
    prob = None
    text = ""

    if request.method == "POST":
        text = request.form["text"]
        try:
            lang, confidence = langid.classify(text)
            result = lang
            full_lang = LANGUAGE_NAMES.get(lang, lang)
            prob = round(confidence * 100, 2)
        except:
            full_lang = "Could not detect"
            prob = None

    return render_template("index.html", text=text, full_lang=full_lang, prob=prob)

if __name__ == "__main__":
    app.run(debug=True)
