# Q14. Write a program to find sum of even numbers from 1 to n.
n = int(input("Enter a Number: "))
sum =0;
i = 2
while(i<=n):
    sum = sum + i;
    i+=2
print("Sum of even numbers:",sum)