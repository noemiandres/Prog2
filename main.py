from flask import Flask
from flask import render_template
from flask import request


app = Flask("Rezepte")

rezepte = {
    "Apfelkuchen": {
        "Name": "Apfelkuchen",
        "Beschreibung": "Der schnellste und leckerste Apfelkuchen, denn du je gebacken hast.",
        "Zutaten": {
            "Apfel": (3, "Stück"),
            "Backpulver": (1, "Pk"),
            "Eier": (3, "Stück"),
            "Mehl": (190, "g"),
            "Wasser": (8, "EL"),
            "Zimt": (1, "Prise"),
            "Zitrone": (1, ""),
            "Zucker": (140,"g")
        },
        "Anleitung": ("Für den schnellen Apfelkuchen zuerst den Backofen Ober- und Unterhitze auf 180 Grad vorheizen."," Danach das Eiweiss in einer Schüssel zu steifen Schnee schlagen.","In einer anderen Schüssel das Eigelb mit Zucker schaumig schlagen.", "Wasser und Zitronenschale dazugeben.","Das mit Backpulver versiebte Mehl untermischen und den Eischnee vorsichtig unterheben.", "Danach die Äpfel schälen und das Kerngehäuse entfernen und in Spalten schneiden.","Die Teig-Masse in eine gefettete Springform füllen.", " Apfelspalten auf dem Teig verteilen und mit Zimt und Zucker bestreuen.", "Den Kuchen im vorgeheizten Backofen bei 170 Grad Heissluft etwa 40 Minuten backen."," En guete!"),
        "Bild": "img/apfelkuchen.jpg"
    },
    "Ravioli": {
        "Name": "Ravioli",
        "Zutaten": {
            "Eier": (2, "Stück"),
            "Mehl": (200, "g")
        },
        "Beschreibung": "Frische Ravioli ganz einfach selbst gemacht.",
        "Anleitung": ("Zutaten mischen 10 Minuten kneten.", "10 Minuten ruhen lassen"),
        "Bild": "img/ravioli.jpg"
    }
}

@app.route("/") #URL für Startseite / Home
@app.route('/home')
def home():
    return render_template("index.html", rezepte=rezepte)

@app.route("/rezept/<name>", methods=['GET', 'POST']) #Apfelkuchenrezept Anzahl Personen anpassen
def rezept(name):
    if request.method == 'POST':
        anzahl = request.form['anzahl']
        return render_template("rezept.html", rezept=rezepte[name], anzahl=anzahl)


    return render_template("rezept.html", rezept=rezepte[name]) #Angpasstes Rezept ausgeben

if __name__ == "__main__":
    app.run(debug=True, port=5000)
