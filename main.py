print(
    "Welcome to the Theme Park\n"
    "To ride the Roller Coaster you must meet the age and height requirements."
)

rider_input_height = int(input("Enter Height in CM: "))
rider_input_age = int(input("Enter Age: "))
rider_pics = input("Do you want a picture taken? (yes/no): ").lower()

if rider_input_height >= 120:

    if rider_input_age > 60:
        print("Sorry, you can't ride because you are over 60 years old.")

    elif rider_input_age < 12:
        rider_total = 5
        print("You can ride and your ticket costs $5.")

    elif rider_input_age <= 18:
        rider_total = 7
        print("You can ride and your ticket costs $7.")

    else:
        rider_total = 12
        print("You can ride and your ticket costs $12.")

    
    if rider_input_age <= 60:

        if rider_pics == "yes":
            rider_total += 3
            print("You have opted for a picture. Additional $3 will be charged.")

        print(f"Your total is ${rider_total}")

else:
    print("Sorry, you can't ride. You must be at least 120 CM tall.")