# Python Pattern Programs - Printing Stars '*' in Reverse Right Angle Triangle Shape | Star Pattern 
i = 1
while i<=5:
    b = 1
    while b<=5-i:
        print(" ",end=" ")
        b+=1
    j = 1
    while j<=i:
        print("*",end = " ")
        j+=1
    print()
    i+=1