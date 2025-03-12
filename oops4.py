class dog:
    def __init__(self, name,age):
        self.name = name
        self.age = age
    def info(self):
        print("hi, I am a dog")
        print(f"Name: {self.name}, Age: {self.age}")
    def sound(self):
        print("I Bark")

class cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print("hi, I am a cat")
        print(f"Name: {self.name}, Age: {self.age}")
    def sound(self):
        print("I Meow")

dog1=dog("Leo", 6)
cat1=cat("Panther", 4)
 
for pets in (dog1, cat1):
    pets.info()
    pets.sound()
    
    