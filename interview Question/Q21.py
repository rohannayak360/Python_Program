# Q21. Write a program to find sum of even digits 
# and product of odd digits of a given number.
n = int(input("Enter a number: "))

sum_even = 0
product_odd = 1


while n > 0:
    digit = n % 10
    if digit % 2 == 0:
        sum_even += digit
    else:
        product_odd *= digit
    n //= 10

print("Sum of even digits:", sum_even)
print("Product of odd digits:", product_odd)    