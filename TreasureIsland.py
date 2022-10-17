# -*- coding: utf-8 -*-
pound = u'\u00A3'

print("Welcome to the rollercoaster")
height = int(input("What is your height in cm? "))

bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print(f"Please pay {pound}5.")
        bill = 5
    elif age <= 18:
        print(f"Please pay {pound}7.")
        bill = 7
    else:
        print(f"Please pay {pound}12.")
        bill = 12

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "y":
        bill += 3

    print(f"Your final bill is {bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")