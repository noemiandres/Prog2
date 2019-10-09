# Kochrezept Applikation

## Ausgangslage
Viele Leute haben zuhause Kochbücher. Meistens sind die Rezepte für 4 Personen angegeben. Jedoch werden die Haushalte immer kleiner und die Zutatenliste stimmt meist nicht mehr mit der Anzahl Personen überein. Man muss die Zutatenliste im Kopf herunterrechnen (z.B. für 3 Personen), was sehr mühsam ist, vorallem wenn es spezielle Gewichtsangaben hat. Auch gibt es Rezepte im Internet, dessen Zutatenliste für eine Anzahl an Personen bestimmt ist. 

## Funktion/Projektidee
Mithilfe meiner Applikation möchte ich das Kochen vereinfachen, vorallem das Einkaufen der Zutaten je nach Anzahl an Personen, für die man das Gericht kochen möchte. Eine vielzahl an Rezepten steht in der Webapplikation zur Verfügung. Man gibt im Eingabefeld des Rezept einfach die Anzahl an Personen an und die Zutatenliste wird automatisch an die Anzahl Personen angepasst.

Anschliessend soll automatisch ein Einkaufszettel generiert werden. Bei jeder Zutat muss man jedoch ein Hacken setzen, wenn man das Produkt auf dem Einkaufzettel möchte. Es kann ja sein, dass man das Produkt schon zuhause hat, dann hat es auf dem Einkaufszettel nichts zu suchen. Der Einkaufszettel wird inklusive Mengenangaben ausgegeben.

## Workflow

**Dateneingabe**
Die einzelnen Rezepte werden mit Mengenangaben in die Webapplikation eingegeben, damit der Benutzer eine Auswahl an Rezepte hat. Der Benutzer kann dann ein Rezept anwählen und die Personenanzahl manuel eingeben.


**Datenverarbeitung/Speicherung**
Der User hat die Möglichkeit, dass die Daten direkt auf der Webseite neu angezeigt werden, in dem er auf den Button "Zutatenliste anpassen" klickt. Möchte der User, dass ein Einkaufszettel gereriert wird, muss er nun die Artikel anwählen, die er auf dem Einkaufszettel haben möchte. Anschliessend muss der Button "Einkaufslise erstellen" anwählen.

**Datenausgabe**
*Einkaufszettel auf Homepage:*
Wenn der User auf den Button "Zutatenliste anpassen" klickt, wird ihm die Zutatenliste der Personenzahl angepasst angezeigt. 

*Einkaufszettel generieren:*
WEnn der User auf den Button "Einkaufsliste erstellen" klickt, wird ihm ein PDF mit der Einkaufsliste ausgegeben.



