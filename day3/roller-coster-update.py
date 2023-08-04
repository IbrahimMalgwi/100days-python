print("Rollercoaster Ticking with pictures options")

height = int(input("What is your height in CM? "))
bill = 0;

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 50
        print("Children's tickets are #50")
    elif age <= 18:
        bill = 75
        print("Teens tickets are #75")
    else:
        bill = 100
        print("Adult tickets are #100")

    wants_photo = input("Do you want a photo taken? Y or N: ")
    if wants_photo == "Y":
        bill += 20
    print(f"Your final bill is #{bill}")
else:
    print("Sorry, you are not tall enough to ride")
