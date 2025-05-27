str=[]
n=int(input("How many strings to input: "))
for i in range(n):
    print("enter a string: ",end='')
    str.append(input())
str.sort()
for i in str:
    print(i)

# str=[]
# s=[]
# n=int(input("How many strings to input: "))
# for i in range(n):
#     print("enter a string: ",end='')
#     str.append(input())
# s=sorted(str)
# for i in s:
#     print(i)

str=[]
n=int(input("How many strings to input: "))
for i in range(n):
    print("enter a string: ",end='')
    str.append(input())
str.sort()
str.reverse()
for i in str:
    print(i)