# Djurparken - Interaktiv Zoo Simulator

Ett interaktivt Python-program som simulerar en djurpark där användare kan mata, leka med och hantera djur samt besökare. Programmet är byggt med objektorienterad programmering (OOP) och demonstrerar arv, abstraktion och polymorfism.

## Funktioner

### Huvudfunktioner
- **Visa alla djur** - Se en lista över alla djur i djurparken
-  **Lägg till djur** - Skapa nya djur av olika typer (Varg, Lejon, Lejonunge)
-  **Mata djur** - Mata djuren med olika typer av mat
-  **Leka med djur** - Interagera med djuren genom lek med färgade bollar
-  **Visa besökare** - Se alla registrerade besökare
-  **Lägg till besökare** - Registrera nya besökare i parken

### Specialfunktioner
- Djur har favoritmat och olika reaktioner beroende på vad de får
- Djur kan bli hungriga och vägrar leka när de är hungriga
- Bollar har kvalitet som minskar när djur leker med dem
- Olika djurtyper påverkar bollkvalitet olika mycket

## Teknisk Stack

- **Python 3.x** - Programmeringsspråk
- **ABC (Abstract Base Classes)** - För abstrakt basklass
- **OOP** - Objektorienterad programmering med arv och polymorfism

## Krav

- Python 3.6 eller högre
- Ingen externa bibliotek krävs (använder bara standardbiblioteket)

## Kom igång

### Installation

1. **Klona eller ladda ner projektet**
```bash
# Om du använder git
git clone <repository-url>
cd djurparken

# Eller ladda ner the-zoo.py direkt
```

2. **Kontrollera Python-version**
```bash
python --version
# eller
python3 --version
```

### Köra programmet

```bash
python the-zoo.py
# eller
python3 the-zoo.py
```

## Användning

### Huvudmeny

När du startar programmet möts du av huvudmenyn:

```
--- Välkommen till Djurparken! ---
1. Visa alla djur
2. Lägg till ett djur
3. Mata ett djur
4. Leka med ett djur
5. Visa alla besökare
6. Lägg till en besökare
7. Avsluta
```

### Exempel på användning

#### 1. Visa alla djur
```
Välj alternativ: 1

Djur i parken:
Varg, ålder 5
Lejon, ålder 7
Lejonunge, ålder 2
```

#### 2. Lägg till ett djur
```
Välj alternativ: 2

Ange djurets namn: Simba
Ange djurets ålder: 3
Ange djurets typ (Varg, Lejon, Lejonunge): lejon

Simba, ålder 3 har lagts till i djurparken.
```

#### 3. Mata ett djur
```
Välj alternativ: 3

Vilket djur vill du mata?
1. Varg, ålder 5
2. Lejon, ålder 7

Ange numret på djuret du vill mata: 1
Du valde att mata Varg.
Vad vill du mata Varg med? Kött

Varg njöt verkligen av Kött!
```

#### 4. Leka med ett djur
```
Välj alternativ: 4

Vilket djur vill du leka med?
1. Varg, ålder 5
2. Lejon, ålder 7

Ange numret på djuret du vill leka med: 2
Du valde att leka med Lejon.
Ange bollens färg (röd, blå, grön): röd

Lejon leker med röd boll.
Bollens kvalitet har minskat med 10. Ny kvalitet: 90
```

## Klassöversikt

### Animal (Abstrakt Basklass)

Representerar alla djur i djurparken.

**Egenskaper:**
- `name` (str) - Djurets namn
- `age` (int) - Djurets ålder
- `hungry` (bool) - Om djuret är hungrigt
- `favourite_food` (str) - Djurets favoritmat

**Metoder:**
- `eat(food)` - Matar djuret med specifik mat
- `hungry()` - Gör djuret hungrigt
- `interact(ball)` - Abstrakt metod för interaktion (implementeras i subklasser)
- `__str__()` - Strängrepresentation av djuret

### Wolf (Ärver från Animal)

Representerar en varg.

**Egenskaper:**
- Favoritmat: "Kött"
- Minskar bollkvalitet med 10 när den leker

**Beteende:**
- Leker med bollen om inte hungrig
- Vägrar leka när hungrig

### Lion (Ärver från Animal)

Representerar ett lejon.

**Egenskaper:**
- Favoritmat: "Kött"
- Minskar bollkvalitet med 10 när den leker

**Beteende:**
- Leker med bollen om inte hungrig
- Vägrar leka när hungrig

### LionCub (Ärver från Lion)

Representerar en lejonunge.

**Egenskaper:**
- Favoritmat: "Mjölk" (överskriver Lion)
- Minskar bollkvalitet med 20 när den leker (mer lekfull!)

**Beteende:**
- Mer energisk och sliter mer på leksaker
- Leker med bollen om inte hungrig

### Visitor

Representerar en besökare i djurparken.

**Egenskaper:**
- `name` (str) - Besökarens namn

**Metoder:**
- `feed_animal(animal)` - Mata ett specifikt djur
- `interact_with_animal(animal, ball)` - Leka med ett djur
- `__str__()` - Strängrepresentation av besökaren

### Ball

Representerar en lekboll.

**Egenskaper:**
- `color` (str) - Bollens färg
- `quality` (int) - Bollens kvalitet (0-100)

**Metoder:**
- `lower_quality(amount)` - Minskar bollens kvalitet
- `__str__()` - Strängrepresentation av bollen

### Zoo

Huvudklass som hanterar djurparken.

**Egenskaper:**
- `opening_hours` (int) - Öppettider
- `price` (int) - Inträdespris
- `animal_list` (list) - Lista över alla djur
- `visitor_list` (list) - Lista över alla besökare
- `balls` (list) - Lista över tillgängliga bollar (röd, blå, grön)

**Metoder:**
- `add_animal(animal)` - Lägg till ett djur
- `add_visitor(visitor)` - Lägg till en besökare
- `show_animals()` - Visa alla djur
- `show_visitors()` - Visa alla besökare
- `feed_animal()` - Interaktiv matning av djur
- `play_with_animal()` - Interaktiv lek med djur

## Spelmekanik

### Matningssystem

1. **Favoritmat**: Om djuret får sin favoritmat blir det mätt och nöjt
   ```python
   Varg njöt verkligen av Kött!
   ```

2. **Annan mat**: Djuret äter men föredrar sin favoritmat
   ```python
   Varg åt Fisk, men föredrar Kött.
   ```

3. **Inte hungrig**: Om djuret inte är hungrigt äter det inte
   ```python
   Varg är inte hungrig just nu.
   ```

### Leksystem

1. **Bollkvalitet**: 
   - Startar på 100
   - Minskar när djur leker
   - Varg/Lejon: -10 per lek
   - Lejonunge: -20 per lek

2. **Hungerstatus**:
   - Hungriga djur vägrar leka
   - Djur måste matas först

3. **Bollfärger**:
   - Röd boll
   - Blå boll
   - Grön boll

# OOP-Koncept Demonstrerade

### 1. Arv (Inheritance)
```python
Wolf -> Animal
Lion -> Animal
LionCub -> Lion -> Animal
```

### 2. Abstraktion
```python
class Animal(ABC):
    @abstractmethod
    def interact(self, ball):
        pass
```

### 3. Polymorfism
Varje djurtyp implementerar `interact()` på sitt eget sätt:
- Varg: Minskar bollkvalitet med 10
- Lejon: Minskar bollkvalitet med 10
- Lejonunge: Minskar bollkvalitet med 20

### 4. Inkapsling (Encapsulation)
Attribut och metoder är organiserade i klasser med tydliga ansvarsområden.

### 5. Komposition
Zoo-klassen "har" djur och besökare (has-a relationship).

## Känd Bugg

**Observera**: Det finns duplicerad kod i slutet av filen `the-zoo.py`:

```python
try:
    choice = int(input("Ange numret på djuret du vill mata: ")) - 1
    # ... resten av koden
```

Denna kod är redan en del av metoden `feed_animal()` och kan tas bort från slutet av filen utan att påverka programmets funktion.

## Inlärningssyfte

Detta projekt demonstrerar:

 **Objektorienterad programmering**
- Klasser och objekt
- Arv och subklasser
- Abstrakta klasser och metoder
- Polymorfism

 **Python-koncept**
- List comprehensions
- Exception handling (try/except)
- String formatting
- User input hantering

 **Designmönster**
- Abstrakt fabrik (för djurskapande)
- Komposition över arv
- Single Responsibility Principle

## Möjliga Förbättringar

### Kortsiktiga förbättringar:
- [ ] Ta bort duplicerad kod i slutet av filen
- [ ] Lägg till felhantering för åldrar (måste vara positiva)
- [ ] Validera djurtyper vid skapande
- [ ] Lägg till möjlighet att ta bort djur/besökare

### Långsiktiga förbättringar:
- [ ] Spara och ladda djurparksdata (JSON/pickle)
- [ ] Lägg till fler djurtyper (Björn, Apa, Zebra, etc.)
- [ ] Implementera ett hungerssystem över tid
- [ ] Lägg till veterinärvård för sjuka djur
- [ ] Statistik över besökare och popularitet
- [ ] Ekonomisystem (intäkter vs kostnader)
- [ ] Grafiskt användargränssnitt (Tkinter/PyGame)
- [ ] Multiplayer-funktionalitet
- [ ] Achievements system
- [ ] Dag/natt-cykel

## Testscenario

### Exempel på en komplett session:

1. **Starta programmet** - Zoo skapas med 3 fördefinierade djur
2. **Visa djur** - Se Varg, Lejon och Lejonunge
3. **Lägg till besökare** - "Anna" registreras
4. **Mata Lejonunge** - Ge mjölk (favoritmat)
5. **Leka med Lejonunge** - Använd röd boll (kvalitet: 100 → 80)
6. **Försök leka igen** - Lejonunge är hungrig, vägrar leka
7. **Mata Lejonunge igen** - Ge mer mjölk
8. **Leka med Lejonunge** - Fungerar nu (kvalitet: 80 → 60)
9. **Avsluta** - Tack för besöket!
    
## Licens

Detta är ett utbildningsprojekt skapat för att demonstrera OOP-koncept i Python.

## Ändamål

Skapad som ett utbildningsprojekt för att lära sig:
- Objektorienterad programmering
- Python class design
- Abstract Base Classes
- Arv och polymorfism
- Interaktiv terminal-applikation

## Snabbstart

```bash
# Klona och kör på 3 sekunder!
git clone <repository-url>
cd djurparken
python the-zoo.py

# Eller bara kopiera koden och kör:
python the-zoo.py
```
