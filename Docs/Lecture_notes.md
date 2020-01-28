Programmeertheorie
Week 1

Maandag 0900 Introductiecollege
AKA Heuristieken
Project van 4 weken. Er zijn 6 cases, kies er 1. Groepen van 3.
Dagelijks van 0900 tot 1700 werken 
6 cases van ‘onoplosbare’ problemen
Techassistent,
Persoonlijke assistentie en presentatie sessies

Heuristiek = kunst van het zoeken.
De meest efficiente route, rustig en gefocust op je probleem een oplossing vinden.

6 cases: Amstelhaege, Chips & Circuits, Protein Pow(d)er, RailNL, Rush Hour, SmartGrid
Welke datastructuren maak ik. Dictionairies, Tuples etc. In Python.

Dinsdag 1500: Soorten problemen


Woensdag 1500: Random Oplossingen

Week 2
Maandag 1500: Depth-First en Breath-first

Dinsdag 1500: Hill climbing en meer

Woensdag 1500: Toepassen van Heuristieken

Week 3
Exploratie en verfijning
Geen HC’s, mogelijke uitvalsweek

Week 4
Deadline maandag: Repo, Docu en Code

Regels: Dagelijks 0900-1700
HC’s
Algemene techassistentie
- Op inschrijving
- 

Met assistentie (persoonlijk)
- 1X per week 30 minuten.
- Hulp bij het nadenken over je case.

Presentatie sessie: tweemaal per week, 1 uur lang. 
Presentatie 10 min, Discussie 10 min. Je moet minimaal 2X presenteren voor de eindpresentaties.

BEOORDELING
Exploratie van de case, techassistentie/confirmatie dmv presentatie

Uitleg van inzicht: in de presentaties

Eindproduct: Code
Alles weegt even zwaar.

CODE
README + Inhoud
Duidelijke en inzichtelijke repo structuur
Geen crashes
requirements.txt of equivalent

In de readme
Inleiding, installatie
Waar kan je wat vinden
Tests/hoe run ik dit programma
Auteurs

Zie voorbeeld.

Hoorcollege Dinsdag 1500
Heuristieken

Probleemtypes: (Naar Eiben)
1. Constraint satisfaction problems (CSP)
    1. Invulling vinden van de variabele (Sudoku). Er zijn constraints, en daar moet je aan voldoen. Cijfer 1-9, in blok, kolom en rij.
    2. Er is maar één oplossing!
2. Free optimization problem
    1. Zo goed mogelijke oplossing.
    2. Er zijn veel oplossingen, maar 1 is de zo goed mogelijkste.
    3. Binnen constraints meerdere oplossingen.
3. Constrained optimization problem (COP)
    1. Combo van beiden


Toestandsruimte: State Space, of all exist able number plates
- Alle mogelijkheden

Pidgeon hole principle - google dit even. Schaken met koninginnen die elkaar niet mogen raken.

N boven K.

Pruning. Verklein je State Space. Moeilijkheid instantie: Toestandsruimtegrootte.
Machtsrelatie is het enige wat telt. Machten naar beneden duwen is goed.

Upper/lower bound. Constraint relaxation.
10 Faculteit aan mogelijke routes. Kansberekening. 
Grootte van toestandsruimte: 10 faculteit
Upper bound: Score functie: 10 keer kortste 
Lower bound: 

Zorg ervoor dat je dingen WEET over je probleem.

Oplossingsdictheid: 1 / 8!
Oplossingsdichtheid: Alle mogelijkheden / alle juiste legitieme oplossingen
Zegt niet veel over de probleemmoeilijkheid


Toestandsruimte groot
Oplossingsdichtheid laag
Er zijn geen leads
Oplossingen zijn ongerelqteerd
Objective function is niet convex.

Hoorcollege Woensdag 1500
Grafen, en de bolletjes heten Vertices, en de verbindingen tussen bolletjes zijn degens.
Bolletjes met verbindingen ertussen.

Verwijzing naar een ander object.

Greedy algoritme:
Heuristiek: Constructief algoritme —> Stap voor stap oplossing opbouwen.
Lokaal de beste keuze mogelijk.
Geen garanties maar wel redelijke resultaten.

Kan je vastlopen?


Shallow Copy vs Deep copy
Python module
Python’s copy:

Import copy
Kopie = copy.deep(iets)

Shallow copy
Lijsten laten verwijzen naar iets.


Greedy algoritme.
1 lijst van batterijen of 1 lijst van huizen.

PPP
Introductie
Methode
Resultaat
Discussie met future work

Presenteersessie 2

Smart-grid. 
Elk huis verbonden aan een batterij. Batterij heeft een maximumcapaciteit.
