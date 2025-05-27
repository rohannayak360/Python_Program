# Q30. Write a program to check whether a given number is prime or not.
n = int(input("Enter a number:"))
count = 0
i = 1
while(i<=n):
    if (n%i==0):
        count += 1
    i+=1
if(count==2):
    print("It is Prime Number")
else:
    print("Composite Number")