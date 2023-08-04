print("Roller Coaster Ride Application")

height = int(input("Enter your height in CM: "))

if height >= 120:
    print("You can ride the roller coaster")
    age = int(input("Enter your age: "))
    if age < 12:
        print("You are to pay #50: ")
    elif age <= 18:
        print("You are to pay # 75")
    else:
        print("You are to pay #100 ")
else:
    print("You cannot ride the roller coaster")
