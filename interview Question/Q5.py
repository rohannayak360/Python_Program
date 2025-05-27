# Q5. Write a program to find the middle number in a group of three numbers.
a = int(input("Enter a first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if(a>b and a<c) or (a<b and a>c):
    print("The middle number is",a)
elif(b>a and b<c) or (b<a and b>c):
    print("The middle number",b)
else:
    print("The middle number is",c)