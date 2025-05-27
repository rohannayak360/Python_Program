# Q19. Write a program to check whether a given number is armstrong or not.
i = int(input("ENter a number: "))
orig = i
sum = 0
while(i>0):
    sum = sum +(i%10) * (i%10) * (i%10)
    i = i//10
if orig == sum:
    print("Numbals are armstrong")
else:
    print("Numbals are not armstrong")