#1
a = input("enter the word: ")
if a == a[::-1]:
    print("it's a palindrome")
else:
    print("it's not a palindrome")

#[OR]#

#2
a=input("enter the word: ")
c=""
for i in a[::-1]:
   c+=i   
if a==c:
    print("it's a palindrome")
else:
    print("it's not a palindrome")

#[OR]_#

#3
a=input("enter the word: ")
c=""
for i in range(len(a)-1,-1,-1):
    c+=a[i]
if a==c:
    print("it's a palindrome")
else:
    print("it's not a palindrome")