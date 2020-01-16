# Kochrezept Applikation

## Ausgangslage
Viele Leute haben zuhause Kochbücher. Meistens sind die Rezepte für 4 Personen angegeben. Jedoch werden die Haushalte immer kleiner und die Zutatenliste stimmt meist nicht mehr mit der Anzahl Personen überein. Man muss die Zutatenliste im Kopf herunterrechnen (z.B. für 3 Personen), was sehr mühsam ist, vor allem wenn es Rezepte mit vielen Zutanten sind.

## Funktion/Projektidee
Mithilfe meiner Applikation möchte ich das Kochen vereinfachen, vor allem das Einkaufen der Zutaten je nach Anzahl an Personen, für die man das Gericht kochen möchte. Zwei Rezepten steht in der Webapplikation zur Verfügung. Das Rezept wird für anfangs für eine Person angezeigt. Gibt man im Eingabefeld des Rezepts  die Anzahl an Personen an so wird die Zutatenliste automatisch an die Anzahl Personen umgerechnet und angepasst.

## Workflow

**Dateneingabe**<br>
Die einzelnen Rezepte werden in einem Dictionary in die Webapplikation eingegeben, damit der Benutzer eine Auswahl an Rezepte hat. Der Benutzer kann dann auf der Startseite ein Rezept anwählen.

**Datenverarbeitung/Speicherung**<br>
Auf der Rezeptseite hat der User die Möglichkeit, das Rezept an Anzahl Personen anzupassen, für die der User kochen möchte. Im Feld "Anzahl Personen", kann die Zahl der bekochten Leute eingegeben werden. Mit dem Button "Jetzt berechnen" wird die Zutatenliste and die Anzahl der eingegebenen Personen berechnet.

**Datenausgabe**<br>
Die Zutatenliste wird nun mit den angepassten Mengenangaben ausgegeben.


## Flussdiagramm
![Rezappt flow diagramm](static/rezapptdiagramm.png "Rezappt flow diagram")