class Dog:
    species = "Canine" # Class variable

    def __init__(self, name, age):
        self.name = name # Instance variable
        self.age = age # Instance variable

    def bark(self):
        return f"{self.name} says Woof!"
    
    def get_age(self):
        return self.age
        
dog1 = Dog("hen", 4)
print(dog1)
print(dog1.species) # Accessing class variable
print(dog1.name) # Accessing instance variable
print(dog1.age) # Accessing instance variable
print(dog1.bark()) # Calling instance method
print(dog1.get_age()) # Calling instance method

        
