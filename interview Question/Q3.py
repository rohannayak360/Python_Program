# Q3. Write a program to find max between three numbers?
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))
if a>b and a>c:
    print("Max is ",a)
elif b>a and a>c:
    print("Max is ",b)
else:
    print("Max is ",c)