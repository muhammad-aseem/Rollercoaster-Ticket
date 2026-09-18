print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth Tickets are $7.")
    else:
        bill = 12
        print("Adult Tickets are $12.")


    wants_photo = input("Would you like to see the picture?" "\n" "Type Y for yes and N for no : ").lower()
    if wants_photo == "y":
            bill += 3
            print(f"Your Final Bill is {bill}")
    else :
        print(f"Your total bill is {bill}")
else:
    print("Sorry you have to grow taller before you can ride.")


