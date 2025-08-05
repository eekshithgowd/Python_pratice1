# for checking first and last letters of a name are same or not
name = input("enter your name: ")
n = name.lower()
if n[0] == n[-1]:
    print("unique name")
else:
    print("common name")

#eligibility test and assiging floors
a = int(input("enter your age: "))
if a >= 18:
    if a > 50:
        print("eligible and go to ground floor")
    else:
        print("eligible and go to 1st floor")
else:
    print("enter valid age or not eligible")