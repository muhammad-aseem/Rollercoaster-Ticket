print("Welcome to the rollercoaster ticket booth you will only be able to ride if you meet the height requirements")

height = int(input("what is your height in cm? "))

if height >= 120:
    print("You are tall enough to ride the rollercoaster!")
else: 
    print("Sorry, you do not meet the height requirements to ride the rollercoaster.")
