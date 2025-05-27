# str=input("enter a strng:")
# sub=input("enter a substring:")
# if sub in str:
#     print(sub+'found in string')
# else:
#     print(sub+"not found in string")

str=input("enter a strng:")
sub=input("enter a substring:")
if sub not in str:
    print(sub+'not found in string')
else:
    print(sub+"found in string")