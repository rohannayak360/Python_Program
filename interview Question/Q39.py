# Q39. Program to count total vowel and consonants in a String
a = input("Enter a name: ")
vowel=0
cons=0
for i in range(0,len(a)):
    if(a[i]!=0):
        if(a[i]=='a' or a[i]=='e' or a[i]=='i' or a[i]=='o' 
           or a[i]=='u' or a[i]=='A' or a[i]=='E'or a[i]=='I'
           or a[i]=='O' or a[i]=='U'):
            vowel+=1
    else:
        cons+=1
print("Vowel is: ",vowel)
print("Constant is: ",cons)
 