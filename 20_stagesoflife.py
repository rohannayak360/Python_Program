age = int(input("Enter your age: "))
if age >= 0 and age <= 2:
    print("Infant")
elif age >= 3 and age <= 12:
    print("Child")
elif age >= 13 and age <= 19:
    print("Teenager")
elif age >= 20 and age <= 35:
    print("Young Adult")
elif age >= 36 and age <= 55:
    print("Adult")
elif age >= 56 and age <= 75:
    print("Senior Adult")
else:
    print("Elderly")
