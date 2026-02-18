
#Parent/Base/Super Class - lending attributes
class Animal:
    def sound(self):
        print("Animal is making a sound")

#child/Derived/Sub Class - borrowing attributes
class Cat(Animal):
    def climb(self):
        print("Cat is climbing a tree")

class Cow(Animal):
    def chew(self):
        print("Cow is chewing grass")

a=Animal()



mycat=Cat()



mycow=Cow()