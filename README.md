Djurpark
Detta program simulerar en interaktiv djurpark där användaren kan mata, leka med och lägga till djur, samt hantera besökare. Programmet är byggt med Python och använder objektorienterad programmering (OOP) för att definiera djur och deras beteenden.

Funktioner
Visa alla djur: Visa en lista över alla djur i djurparken.
Lägg till ett djur: Användaren kan lägga till nya djur av olika typer som Varg, Lejon eller Lejonunge.
Mata ett djur: Användaren kan välja ett djur att mata och specificera vilken typ av mat djuret ska få.
Leka med ett djur: Användaren kan interagera med djuren genom lek.
Visa alla besökare: Visar en lista över alla besökare i parken.
Lägg till en besökare: Lägg till en ny besökare till djurparken.

Klassöversikt
Animal (Abstrakt klass)
Representerar alla djur i djurparken.
Egenskaper:
name: Djurets namn.
age: Djurets ålder.
hungry: Om djuret är hungrigt.
favourite_food: Djurets favoritmat.
Metoder:
eat(food): Matar djuret med en specifik typ av mat.
hungry(): Gör djuret hungrigt.
interact(ball): Abstrakt metod som implementeras i underklasser.
Wolf, Lion, LionCub (ärver från Animal)
Varje djurtyp har unika beteenden men delar grundläggande funktionalitet.
Exempel: Wolf och Lion leker med en boll och interagerar olika beroende på om de är hungriga.

Zoo
Hanterar en lista över djur och besökare.
Egenskaper:
animal_list: Lista över djur i parken.
visitor_list: Lista över besökare.
opening_hours: Parkens öppettider.
price: Inträdespris för besökare.
Metoder:
add_animal(animal): Lägg till ett djur i parken.
add_visitor(visitor): Lägg till en besökare.
show_animals(): Visa alla djur i parken.
feed_animal(): Mata ett valt djur.
play_with_animal(): Leka med ett valt djur.

Visitor
Representerar en besökare i djurparken.
Egenskaper:
name: Besökarens namn.
