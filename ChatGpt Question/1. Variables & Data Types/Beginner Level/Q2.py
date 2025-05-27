# Swap values of two variables without using a third variable.

# Method-1
var1 = "nayak"
var2 = "Rohan"
var1,var2=var2,var1
print(var1,var2)

# Method-2
num1 = 10
num2 = 15
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2
print("num1=",num1,"num2=",num2)
