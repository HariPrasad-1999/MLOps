# Base Class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound.")

# Derived Class
class Dog(Animal):
    def __init__(self):
        self.behaviour = "Friendly"

    def speak(self):
        print(f"{self.name} barks. He is very {self.behaviour}") # If there's no variable for self.name then it will lead to constructor overloading. 
        #return super().speak()  # super() is used to call methods of a parent class inside a child clas
    

# Instace of an Animal
# animal = Animal("Lion")
# animal.speak()

# Instace of an Dog
dog = Dog()
dog.speak()
