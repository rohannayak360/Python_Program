# Q38. Python Program to Reverse a String Using For Loop 

# a = "rohan nayak"
# print(a[-1: :-1])

# Using for loop
a = input("Enter a string: ")
for i in range((len(a)-1),-1,-1):
    print(a[i],end="")