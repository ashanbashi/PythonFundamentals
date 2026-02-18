class Dog:

    def __init__(self,breed,age,color):
        self.breed=breed
        self.age=age
        self.color=color

    def speak(self):
        print("Dog is barking")

dog1=Dog("German Shepherd","3","White")
print(dog1.breed,dog1.age,dog1.color)

dog2=Dog("Chihuahua","5","Brown")
print(dog2.breed,dog2.age,dog2.color)

dog3=Dog("Siberian Husky","7","White")
print(dog3.breed,dog3.age,dog3.color)