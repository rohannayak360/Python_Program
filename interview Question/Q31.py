# Q31. Write a program to print febonacci series upto a given number.
n = int(input("Enter  a number: "))
x = 0
y = 1
z = 0
while(z<=n):
    print(z)
    x = y
    y = z
    z = x+y