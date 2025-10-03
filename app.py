from flask import Flask, request, render_template
from langdetect import detect, detect_langs, DetectorFactory

DetectorFactory.seed = 0

language_names = {
    "en": "English", "fr": "French", "es": "Spanish", "hi": "Hindi",
    "de": "German", "ta": "Tamil", "te": "Telugu"
}

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    text = ""
    result_code = None
    result_name = None
    result_probs = []

    if request.method == "POST":
        text = request.form.get("text")
        if text:
            try:
                langs = detect_langs(text)
                result_code = langs[0].lang
                result_name = language_names.get(result_code, "Unknown")
                result_probs = [(language_names.get(l.lang,"Unknown"), round(l.prob*100,2)) for l in langs[:3]]
            except:
                result_code = "Unknown"
                result_name = "Could not detect"
                result_probs = []

    return render_template("index.html", text=text, result=result_code, full_lang=result_name, probs=result_probs)

if __name__ == "__main__":
    app.run(debug=True)
