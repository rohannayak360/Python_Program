# Q11. Write a program to find sum of cubes from 1 to n
n  =int(input("Enter a number:"))
i = 1
sum = 0
while i<=n:
    sum = sum+(i*i*i)
    i +=1
print("Sum of cubes: ",sum)