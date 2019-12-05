from flask import Flask
from flask import render_template

app = Flask("Rezepte")

testdaten = {
    "Apfelkuchen": {
        "Zutaten": {
            "Apfel": 2,
            "Zucker": (200, "g")
        },
        "Beschreibung": ["blablabla"],
        "Anleitung": "Äpfel in kleine Stücke schneiden. Alle Zutaten in eine Schüssel geben und vermengen."
    }
}

testdaten2 = {
    "Ravioli": {
        "Zutaten": {
            "Eier": 2,
            "Mehl": (200, "g")
        },
        "Beschreibung": ["mhhhhhm"],
        "Anleitung": "Äpfel in kleine Stücke schneiden. Alle Zutaten in eine Schüssel geben und vermengen."
    }
}

@app.route("/")
@app.route('/home')
def home():
    return render_template("index.html", rezepte=testdaten, rezepte2=testdaten2)

@app.route("/apfelkuchen.html")
def apfelkuchen():
    return render_template("apfelkuchen.html", rezepte=testdaten, rezepte2=testdaten2)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
