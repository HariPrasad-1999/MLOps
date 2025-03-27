# Single Inheritance
# Base Class
"""
class Parent:
    def __init__(self, name):
        self.name = name 

    def greet(self):
        print(f"Hello, my name is {self.name}")
    
# Derived/Child Class
class Child(Parent):
    def play(self):
        print(f"{self.name} is playing.")

# Child Instance 
child = Child("Alice")
child.greet() # Hello, my name is Alice
child.play()  # Alice is playing.
"""

# Multilevel Inheritance
# Base Class
"""
class Grandparent:
    def __init__(self, name):
        self.name = name
    
    def tell_story(self):
        print(f"{self.name} tells a story!")

# Intermediate class
class Parent(Grandparent):
    def work(self):
        print(f"{self.name} is working.")

# Derived class
class Child(Parent):
    def play(self):
        print(f"{self.name} is playing")

# create instance
child = Child("Charlie")
child.tell_story()  # Charlie tells a story!
child.work()        # Charlie is working.
child.play()        # Charlie is playing
"""


# Hierarchical Inheritance
# Base Class
"""class Parent:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        print(f"Hello, my name is {self.name}")

# Derived Class 1
class Child1(Parent):
    def play(self):
        print(f"{self.name} is playing.")

# Derived Class 2
class Child2(Parent):
    def study(self):
        print(f"{self.name} is studying.")

child1 = Child1("Dave")
child2 = Child2("Eve")

child1.greet()
child1.play()

child2.greet()
child2.study()
"""


# Multiple Inheritance / Diamond problem
# Base Class
"""
class A:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        print(f"Hello from A, {self.name}")

class B(A):
    def greet(self):
        print(f"Hello from B, {self.name}")
        super().greet()

class C(A):
    def greet(self):
        print(f"Hello from C, {self.name}")
        super().greet()

class D(B, C):
    def greet(self):
        print(f"Hello from D, {self.name}")
        super().greet()

d = D("HP")
d.greet() 
# Output 
# Hello from D, HP
# Hello from B, HP
# Hello from C, HP
# Hello from A, HP
"""


# Hybrid Inheritance 
"""
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes a sound.")
    
class Mammal(Animal):
    def feed(self):
        print(f"{self.name} is feeding milk.")

class Bird(Animal):
    def fly(self):
        print(f"{self.name} is flying.")

class Bat(Mammal, Bird):
    def __init__(self, name):
        Mammal.__init__(self, name)

    def nocturnal(self):
        print(f"{self.name} is nocturnal.")

bat = Bat("Baddie bat")
bat.sound()
bat.feed()
bat.fly()
bat.nocturnal()"""