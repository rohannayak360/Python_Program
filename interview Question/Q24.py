# Q24. Write a program to print factors of given number.
i = int(input("Enter a number: "))
fac = 1
while(i>0):
    fac = fac*i
    i = i-1
print("Factorial: ",fac)