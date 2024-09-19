from abc import ABC, abstractmethod

# Grundklass för alla djur
class Animal(ABC):
    def __init__(self, name, age, favourite_food):
        self.name = name
        self.age = age
        self.hungry = False
        self.favourite_food = favourite_food

    # Metod för att mata djuret
    def eat(self, food):
        if not self.hungry:
            print(f"{self.name} är inte hungrig just nu.")
            return
        
        if food == self.favourite_food:
            self.hungry = False
            print(f"{self.name} njöt verkligen av {food}!")
        else:
            print(f"{self.name} åt {food}, men föredrar {self.favourite_food}.")

    # Metod för att göra djuret hungrigt
    def hungry(self):
        self.hungry = True
        print(f"{self.name} är nu hungrig.")

    # Abstrakt metod för interaktion med djuret
    @abstractmethod
    def interact(self, ball):
        pass

    def __str__(self):
        return f"{self.name}, ålder {self.age}"

# Klass för Varg som ärver från Animal
class Wolf(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Kött")

    # Implementering av interaktionsmetoden för Varg
    def interact(self, ball):
        if self.hungry:
            print(f"{self.name} är hungrig och vill inte leka.")
        else:
            print(f"{self.name} leker med {ball.color} boll.")
            ball.lower_quality(10)

# Klass för Lejon som ärver från Animal
class Lion(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Kött")

    # Implementering av interaktionsmetoden för Lejon
    def interact(self, ball):
        if self.hungry:
            print(f"{self.name} är hungrig och vill inte leka.")
        else:
            print(f"{self.name} leker med {ball.color} boll.")
            ball.lower_quality(10)

# Klass för Lejonunge som ärver från Lejon
class LionCub(Lion):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.favourite_food = "Mjölk"

    # Implementering av interaktionsmetoden för Lejonunge
    def interact(self, ball):
        if self.hungry:
            print(f"{self.name} är hungrig och vill inte leka.")
        else:
            print(f"{self.name} leker med {ball.color} boll.")
            ball.lower_quality(20)

# Klass för besökare
class Visitor:
    def __init__(self, name):
        self.name = name

    # Metod för att mata ett djur
    def feed_animal(self, animal):
        print(f"{self.name} matar {animal.name}.")
        animal.eat(animal.favourite_food)

    # Metod för att leka med ett djur
    def interact_with_animal(self, animal, ball):
        print(f"{self.name} leker med {animal.name} med en {ball.color} boll.")
        animal.interact(ball)

    def __str__(self):
        return self.name

# Klass för boll
class Ball:
    def __init__(self, color, quality):
        self.color = color
        self.quality = quality

    # Metod för att minska bollens kvalitet
    def lower_quality(self, amount):
        self.quality -= amount
        print(f"Bollens kvalitet har minskat med {amount}. Ny kvalitet: {self.quality}")

    def __str__(self):
        return f"{self.color} boll med kvalitet {self.quality}"

# Klass för Zoo
class Zoo:
    def __init__(self, opening_hours, price):
        self.opening_hours = opening_hours
        self.price = price
        self.animal_list = []
        self.visitor_list = []
        self.balls = [Ball("röd", 100), Ball("blå", 100), Ball("grön", 100)]
        # Lägg till några djur som standard
        self.add_animal(Wolf("Varg", 5))
        self.add_animal(Lion("Lejon", 7))
        self.add_animal(LionCub("Lejonunge", 2))

    # Metod för att lägga till ett djur
    def add_animal(self, animal):
        self.animal_list.append(animal)
        print(f"{animal} har lagts till i djurparken.")

    # Metod för att lägga till en besökare
    def add_visitor(self, visitor):
        self.visitor_list.append(visitor)
        print(f"{visitor} har lagts till som besökare.")

    # Metod för att visa alla djur
    def show_animals(self):
        if not self.animal_list:
            print("Inga djur finns i parken.")
        else:
            print("Djur i parken:")
            for animal in self.animal_list:
                print(animal)

    # Metod för att visa alla besökare
    def show_visitors(self):
        if not self.visitor_list:
            print("Inga besökare finns i parken.")
        else:
            print("Besökare i parken:")
            for visitor in self.visitor_list:
                print(visitor)

    # Metod för att mata ett djur
    def feed_animal(self):
        if not self.animal_list:
            print("Inga djur finns att mata.")
            return

        print("Vilket djur vill du mata?")
        for index, animal in enumerate(self.animal_list, start=1):
            print(f"{index}. {animal}")

        try:
            choice = int(input("Ange numret på djuret du vill mata: ")) - 1
            if 0 <= choice < len(self.animal_list):
                selected_animal = self.animal_list[choice]
                print(f"Du valde att mata {selected_animal.name}.")
                food = input(f"Vad vill du mata {selected_animal.name} med? ")
                selected_animal.eat(food)
            else:
                print("Ogiltigt nummer.")
        except ValueError:
            print("Ange ett giltigt nummer.")

    # Metod för att leka med ett djur
    def play_with_animal(self):
        if not self.animal_list:
            print("Inga djur finns att leka med.")
            return

        print("Vilket djur vill du leka med?")
        for index, animal in enumerate(self.animal_list, start=1):
            print(f"{index}. {animal}")

        try:
            choice = int(input("Ange numret på djuret du vill leka med: ")) - 1
            if 0 <= choice < len(self.animal_list):
                selected_animal = self.animal_list[choice]
                print(f"Du valde att leka med {selected_animal.name}.")
                ball_color = input("Ange bollens färg (röd, blå, grön): ")
                ball = next((b for b in self.balls if b.color == ball_color), None)
                if ball:
                    selected_animal.interact(ball)
                else:
                    print("Ogiltig färg!")
            else:
                print("Ogiltigt nummer.")
        except ValueError:
            print("Ange ett giltigt nummer.")

# Huvudmeny för programmet
def main_menu(zoo):
    while True:
        print("\n--- Välkommen till Djurparken! ---")
        print("1. Visa alla djur")
        print("2. Lägg till ett djur")
        print("3. Mata ett djur")
        print("4. Leka med ett djur")
        print("5. Visa alla besökare")
        print("6. Lägg till en besökare")
        print("7. Avsluta")

        choice = input("Välj ett alternativ (1-7): ")

        if choice == '1':
            zoo.show_animals()
        elif choice == '2':
            name = input("Ange djurets namn: ")
            age = int(input("Ange djurets ålder: "))
            animal_type = input("Ange djurets typ (Varg, Lejon, Lejonunge): ").lower()
            if animal_type == "varg":
                zoo.add_animal(Wolf(name, age))
            elif animal_type == "lejon":
                zoo.add_animal(Lion(name, age))
            elif animal_type == "lejonunge":
                zoo.add_animal(LionCub(name, age))
            else:
                print("Ogiltig djurtyp.")
        elif choice == '3':
            zoo.feed_animal()
        elif choice == '4':
            zoo.play_with_animal()
        elif choice == '5':
            zoo.show_visitors()
        elif choice == '6':
            name = input("Ange besökarens namn: ")
            zoo.add_visitor(Visitor(name))
        elif choice == '7':
            print("Tack för att du besökte Djurparken. Välkommen åter!")
            break
        else:
            print("Ogiltigt val, försök igen.")

# Starta programmet
if __name__ == "__main__":
    zoo = Zoo(opening_hours=9, price=100)
    main_menu(zoo)










try:
    choice = int(input("Ange numret på djuret du vill mata: ")) - 1
    if 0 <= choice < len(self.animal_list):
        selected_animal = self.animal_list[choice]
        print(f"Du valde att mata {selected_animal.name}.")
        food = input(f"Vad vill du mata {selected_animal.name} med? ")
        selected_animal.eat(food)
    else:
        print("Ogiltigt nummer.")
except ValueError:
    print("Ange ett giltigt nummer.")

