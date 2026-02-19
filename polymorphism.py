#Poymorphism - Allows usage of same method name but behave differently

class Cars:
    def sound(self):
        return "Sound"

class ferrari(Cars):
    def sound(self):
        return "VROOOOOM... RAAAAAAAHHH... WAAAAAAAHHHH!"

class bugatti(Cars):
    def sound(self):
        return "whummm… whummm…"

for cars in [ferrari(), bugatti()]:
    print(cars.sound())
