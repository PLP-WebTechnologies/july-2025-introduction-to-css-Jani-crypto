class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def meow(self):
        print(f"{self.name} says Meow! 😺")
    
    def info(self):
        print(f"{self.name} is a {self.color} cat.")

# Test
my_cat = Cat("Luna", "black")
my_cat.info()
my_cat.meow()
