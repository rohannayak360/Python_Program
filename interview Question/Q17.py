# Q17. Write a program to find sum of square of digits of a given number.
i = int((input("Enter sum of digits")))
sum = 0
while(i>0):
    sum = sum+(i%10)*(i%10)
    i =i//10
print("Sum of digits", sum)