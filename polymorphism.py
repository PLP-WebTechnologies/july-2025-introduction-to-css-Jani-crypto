class Animal:
    def sound(self):
        pass

class Cat(Animal):
    def sound(self):
        print("Meow 😺")

class Dog(Animal):
    def sound(self):
        print("Woof 🐶")

# Test
for pet in (Cat(), Dog()):
    pet.sound()
