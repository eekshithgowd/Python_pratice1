a = int(input("insert money: "))
if a == 10:
    print("pls collect the chips")
elif a==20:
    b = input("available drinks:[w,m,c]\n What do you want: ")
    if b=="w":
        print("pls collect the water bottle")
    elif b=="m":
        print("pls collect the MAZA")
    elif b=="c":
        print("pls collect the COKE")
    elif b=="d":
        print("pls collect the COKE")
    else:
        print("sorry not available")
else:
    print("pls insert sufficient money")