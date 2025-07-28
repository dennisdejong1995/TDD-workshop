# TDD-workshop
TDD Workshop voor het uitvoeren van de [Mars Rover Kata](https://kata-log.rocks/mars-rover-kata)

## Voorbereiding
- Voor deze workshop heb je een werkende Python-omgeving nodig. Zorg ervoor dat je de volgende tools hebt geïnstalleerd:
   - Python 3.x
   - Een IDE naar keuze (bijvoorbeeld PyCharm, VSCode, etc.)
   - Een testframework zoals `unittest` of `pytest`

## Regels
- Deze Kata wordt uitgevoerd in tweetallen. Persoon A schrijft de tests en persoon B implementeert de functionaliteit en andersom.
- De Kata wordt uitgevoerd op één laptop.
- Implementeer de requirements één voor één. Lees de volgende requirement pas nadat de vorige is geïmplementeerd en de tests slagen.
- De TDD-cycle wordt gevolgd: Red-Green-Refactor.
  - Persoon A schrijft een test die faalt (Red).
  - Persoon B implementeert de minimale code om de test te laten slagen (Green).
  - Persoon A refactort de code indien nodig, zonder dat de tests falen (Refactor).
  - Persoon B schrijft de volgende test die faalt (Red).
  - etc...

## Omschrijving
Je maakt deel uit van het team dat Mars verkent door op afstand bestuurbare voertuigen naar het oppervlak van de planeet te sturen. Ontwikkel een API die de vanaf aarde verzonden commando's vertaalt naar instructies die door de rover worden begrepen.

## Instructies
1. Zorg ervoor dat je de repository hebt gekloond naar je lokale machine.
2. Open de repository in je favoriete IDE.
3. Voer de tests uit om te zien dat ze falen.
4. Implementeer de gegeven requirements stap voor stap volgens de TDD-principes.


## Requirements
- Je krijgt het beginpunt `(x,y)` van een rover en de richting `(N,S,E,W)` waarin deze staat.
- De rover ontvangt een reeks commando's als een karakterarray.
- Implementeer commando's om de rover vooruit/achteruit te laten bewegen `(f,b)`.
- Implementeer commando's om de rover naar links/rechts te laten draaien `(l,r)`.
- Implementeer het omwikkelen aan de randen. Let op, planeten zijn bollen.
- Implementeer obstakeldetectie vóór elke verplaatsing naar een nieuw vakje. Als een reeks commando's een obstakel tegenkomt, beweegt de rover tot het laatste mogelijke punt, stopt de reeks en rapporteert het obstakel.
