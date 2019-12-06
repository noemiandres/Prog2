from flask import Flask
from flask import render_template

app = Flask("Rezepte")

testdaten = {
    "Apfelkuchen": {
        "Beschreibung": "Der schnellste und leckerste Apfelkuchen, denn du je gebacken hast.",
        "Zutaten": {
            "Apfel": 3,
            "Backpulver": (1, "Pk"),
            "Eier": 3,
            "Mehl": (190, "g"),
            "Wasser": (8, "EL"),
            "Zimt": (1, "Prise"),
            "Zitrone": 1,
            "Zucker": (140,"g")
        },
        "Anleitung": "Für den schnellen Apfelkuchen zuerst den Backofen (Ober- und Unterhitze) auf 180 Grad vorheizen.Danach das Eiweiss in einer Schüssel zu steifen Schnee schlagen. In einer anderen Schüssel das Eigelb mit Zucker schaumig schlagen. Wasser und Zitronenschale dazugeben. Das mit Backpulver versiebte Mehl untermischen und den Eischnee vorsichtig unterheben. Danach die Äpfel schälen und das Kerngehäuse entfernen und in Spalten schneiden.Die Teig-Masse in eine gefettete Springform füllen. Apfelspalten auf dem Teig verteilen und mit Zimt und Zucker bestreuen. Den Kuchen im vorgeheizten Backofen bei 170 Grad (Heissluft) etwa 40 Minuten backen. En guete!"
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

@app.route("/apfelkuchen") #Apfelkuchenrezept einzelne Seite
def apfelkuchen():
    return render_template("apfelkuchen.html", rezepte=testdaten['Apfelkuchen'], rezepte2=testdaten2)

@app.route("/apfelkuchen.html", methods=['GET', 'POST'])
def anzahl_personen():
    if request.method == 'POST':
        personen = request.form['anzahl']
        rueckgabe_string = personen
        return rueckgabe_string

        return render_template("apfelkuchen.html")



if __name__ == "__main__":
    app.run(debug=True, port=5000)
