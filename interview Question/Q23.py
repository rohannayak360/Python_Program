# Q23. Write a program to check whether a given number is palindrom number or not.
i = int(input("Enter a number: "))
rev = 0
x = i
while(i>0):
    rev = (rev*10)+i%10
    i = i//10
if(x==rev):
    print("Number is palindrome")
else:
    print("Number is not palindrome")