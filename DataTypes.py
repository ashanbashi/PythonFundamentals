age = 70 #interger
temperature = 34.89 #float
greeting =  "Hello" #string
isMaried = True #boolean

print("I am", age, "years old")
print("The current body temperature of the patient is", temperature, "degrees Celsius")
print("Are you maried ?", isMaried)


#Data Structures - Multiple values stored in a single variable
cars = ["Toyota", "Audi", "BMW", "Mercedes"] #List- it's ordered and changeable
fruits = ("apple", "banana", "cherry") #Tuple - it's ordered and unchangeable
countries = {"Italy", "Germany", "France"} #Set - it's unordered and unchangeable
language = ["english", "french", "spanish"] #Array
student = {
    "firstname" : "John",
    "lastname" : "Doe",
    "age" : 19,
    "course" : "FullStack",
    "gender" : "Male",
}#Dictionary
print(cars)
print(fruits)
print(countries)
print(student)
print(student["firstname"])

#Typecasting