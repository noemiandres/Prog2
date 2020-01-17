from flask import Flask
from flask import render_template
from flask import request
from datetime import datetime
import json


app = Flask("Rezepte")

#Datenstruktur der Rezepte
rezepte = {
    "Apfelkuchen": { #Daten für Apfelkuchen
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
        "Anleitung": ("Der Apfelkuchen ist für 4 Leute gedacht.", "Für den schnellen Apfelkuchen zuerst den Backofen Ober- und Unterhitze auf 180 Grad vorheizen."," Danach das Eiweiss in einer Schüssel zu steifen Schnee schlagen.","In einer anderen Schüssel das Eigelb mit Zucker schaumig schlagen.", "Wasser und Zitronenschale dazugeben.","Das mit Backpulver versiebte Mehl untermischen und den Eischnee vorsichtig unterheben.", "Danach die Äpfel schälen und das Kerngehäuse entfernen und in Spalten schneiden.","Die Teig-Masse in eine gefettete Springform füllen.", " Apfelspalten auf dem Teig verteilen und mit Zimt und Zucker bestreuen.", "Den Kuchen im vorgeheizten Backofen bei 180 Grad etwa 40 Minuten backen."," En guete!"),
        "Bild": "img/apfelkuchen.jpg"
    },
    "Kartoffelstock": { #Daten für Kartoffelstock
        "Name": "Kartoffelstock",
        "Zutaten": {
            "Kartoffeln, mehlig kochende": (300, "g"),
            "Milch": (0.5, "dl"),
            "Butter": (10, "g"),
            "Muskat, Salz": ("", "wenig"),
        },
        "Beschreibung": "Frischer Kartoffelstock ganz einfach selbst gemacht.",
        "Anleitung": ("Kartoffeln im Salzwasser offen bei mittlerer Hitze ca. 20 Min. sehr weich kochen.", "Kartoffeln durchs Passvite treiben oder mit dem Kartoffelstampfer zerstossen.","Milch und Butter unter Rühren mit der Kelle nach und nach zu den Kartoffeln geben.", "Kurz und kräftig rühren, bis die Kartoffelmasse luftig ist und locker von der Kelle fällt.", "Mit Muskatnuss und Salz würzen."),
        "Bild": "img/kartoffelstock.png"
    }
}
#URL für Startseite / Home
@app.route("/") #nur Serveradresse
@app.route('/home') #Serveradresse + Zusatz in "URL" /home
def home():
    return render_template("index.html", rezepte=rezepte) #Es wird index.html aufgerufen/ausgegeben sowie die Daten von rezepte (Rezeptdaten)

#Rezeptseite, Anzahl Personen anpassen
@app.route("/rezept/<name>", methods=['GET', 'POST']) #GET, POST für Eingabefeld
def rezept(name):
    if request.method == 'POST': #wenn Post (Eingabe) dann Code "anzahl" aus HTML ausgeben
        anzahl = request.form['anzahl']
        return render_template("rezept.html", rezept=rezepte[name], anzahl=anzahl)


    return render_template("rezept.html", rezept=rezepte[name]) #Angpasstes Rezept ausgeben

#json Datei erstellen 
#bei Rezpetberechnung soll json erstellt werden, wenn Button geklickt  
@app.route("/rezept/<name>", methods=['GET', 'POST']) 
def speichern(datei, key, value):
    try:
        with open(rezepte) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    datei_inhalt[str(key)] = value

    print(datei_inhalt)

    with open(rezepte, "w") as open_file:
        json.dump(datei_inhalt, open_file)

@app.route("/rezept/<name>", methods=['GET', 'POST']) 
def aktivitaet_speichern(aktivitaet):
    datei_name = "aktivitaeten.json"
    zeitpunkt = datetime.now()
    speichern(datei_name, zeitpunkt, aktivitaet)
    return zeitpunkt, aktivitaet

@app.route("/rezept/<name>", methods=['GET', 'POST']) 
def aktivitaeten_laden():
    datei_name = "aktivitaeten.json"

    try:
        with open(datei_name) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    return datei_inhalt

if __name__ == "__main__":
    app.run(debug=True, port=5000)
