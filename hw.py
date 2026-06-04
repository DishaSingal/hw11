class Pet:
    def __init__(self, name):
        self.name = name

    def show_info(self):
     print(f"Pet Name: {self.name}")


def show_info(self):
    print(f"Pet Name: {self.name}")
    
def care_action(self):
    print(f"{self.name} needs general care.")


class Dog(Pet):
    def care_action(self):
        print(f"{self.name} needs a walk and some playtime.")

class Cat(Pet):
    def care_action(self):
        print(f"{self.name} needs grooming and quiet rest.")

dog = Dog("Buddy")
cat = Cat("Doug")

pets = [dog,cat]

for pet in pets:
 pet.show_info
 pet.care_action()
 print()




    