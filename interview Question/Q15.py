# Q15. Write a program to find sum of first n even numbers.
n = int(input("Enter a number:"))
sum = 0
i = 1
count = 0
while(count<3):
    if(i%2==0):
        sum += i;
        count += 1;
    i +=1
print("Sum of first n:",sum)