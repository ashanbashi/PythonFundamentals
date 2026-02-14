first = int(input("Enter First Number"))
second = int(input("Enter Second Number"))
third = int(input("Enter Third Number"))

if first > second and first > third:
    print(first, "is the largest number")

elif second > first and second > third:
    print(second, "is the largest number")

else:
    print(third, "is the largest number")