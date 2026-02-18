#OOP(Object oriented Programming)
#Class is a blueprint of an object
#Object is an instance of a class

class Student:
    #Attributes
    name="Daniel"
    age=19
    gender="Male"

    #Behaviour/Functions/Methods
    def study(self):
        print("Student is studying")

    def movement(self):
        print("Student is moving")


#Creating Objects
student1=Student()
print(student1.name)

student2=Student()
print(student2.name)

student3=Student()