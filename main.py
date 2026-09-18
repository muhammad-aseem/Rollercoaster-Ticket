# print("Welcome to the rollercoaster ticket booth you will only be able to ride if you meet the height requirements")

# height = int(input("what is your height in cm? "))

# if height >= 120:
#     print("You are tall enough to ride the rollercoaster!")
# else: 
#     print("Sorry, you do not meet the height requirements to ride the rollercoaster.")


print(
    "Welcome to the Theme Park\n"
    "To ride the Roller Coaster you must meet the age and height requirements."
)

rider_input_height = int(input("Enter Height in CM: "))
rider_input_age = int(input("Enter Age: "))

if rider_input_height >= 120:

    if rider_input_age > 60:
        print("Sorry, you can't ride because you are over 60 years old.")

    elif rider_input_age < 12:
        print("You can ride and you must pay $5.")

    elif rider_input_age <= 18:
        print("You can ride and you must pay $7.")

    else:
        print("You can ride and you must pay $12.")

else:
    print("Sorry, you can't ride. You must be at least 120 CM tall.")

    