# Q20. Write a program to find product of digits of a given number.
n = int(input("Enter product number: "))
product = 1
while(n>0):
    product = product*(n%10)
    n = n//10

print("Product of digits", product)