# class Animal:      # Base Class
#     def __init__(self, name):
#         self.name = name
    
#     def speak(self):
#         print(f"{self.name} makes a sound.")

# class Dog(Animal):  # Derived Class
#     # def __init__(self):
#     #     self.behaviour = "friendly."

#     def speak(self):
#         print(f"The {self.name} barks")  # return super().speak()  # super() is used to call methods of a parent class inside a child clas
    
# # Instace of an Animal
# animal = Animal("Generic Animal")
# animal.speak()

# # Instace of an Dog
# dog = Dog("buddy")
# dog.speak()



# Super Keyword 

# Base Class 
class Animal:
    def __init__(self):
        self.name = "buddy"

    def speak(self):
        print(f"{self.name} makes a sound!")

# Derived Class    
class Dog(Animal):   
    def __init__(self, breed): # New attributes -> Breed
        super().__init__() # Super keyword is used to inherit all methods from parent class.
        self.breed = breed
    
    def speak1(self):
        super().speak() # Super keyword is used to inherit all methods from parent class.
        print(f"{self.name} barks. it is a {self.breed}")
    
dog = Dog("Golden Retriever")
dog.speak()
