# Q6. Write a program to calculate total marks in 5 subjects (Full marks = 100) as well as percentage Of marks and division as per the following condition:
# percentage>=80 — Grade A
# percentage>=60 — Grade B
# percentage>=40 — Grade C
# percentage<40 —Grade D

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
d = int(input("Enter the fourth number: "))
e = int(input("Enter the fifth number: "))
total = a+b+c+d+e
percentage=(total/500)*100
if percentage>=80:
    print("Grade: A")
elif percentage>=60:
    print("Grade: B")
elif percentage>=40:
    print("Grade: C")
elif percentage<40:
    print("Grade: D")
else:
    print("Invalid input")