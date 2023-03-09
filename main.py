#BMI Counter

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = int(weight)/float(height)**2
bmi = int(bmi)
print(bmi)

#Tip Calculator
#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

bill = input("How much is the bill? ")
people = input("How many people are there? ")
tip = input("What is your tip percentage? 10 / 12 / 15 ? ")

each_pay = (int(bill)/int(people)) * (int(tip)+100)/100
final_amount = "{:.2f}".format(each_pay)

print(f"Each person should pay ${final_amount}")

#Pizza Order
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

if size == "S":
    bill = 15
    if add_pepperoni == "Y":
        bill += 2
    elif add_pepperoni == "N":
        if extra_cheese == "Y":
            bill += 1

    print(f"Your final bill is: ${bill}.")

if size == "M":
    bill = 20
    if add_pepperoni == "Y":
        bill += 3
    elif add_pepperoni == "N":
        if extra_cheese == "Y":
            bill += 1

    print(f"Your final bill is: ${bill}.")

if size == "L":
    bill = 25
    if add_pepperoni == "Y":
        bill += 3
    elif add_pepperoni == "N":
        if extra_cheese == "Y":
            bill += 1

    print(f"Your final bill is: ${bill}.")

#Love Counter

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

full_name = name1+name2
full_name = full_name.lower()
# print(full_name)

#Looking for TRUE
true_count = 0;

t_count = int(full_name.count("t"))
r_count = int(full_name.count("r"))
u_count = int(full_name.count("u"))
e_count = int(full_name.count("e"))

true_count = t_count+r_count+u_count+e_count
true_count = str(true_count)

#Looking for Love

love_count = 0;

l_count = int(full_name.count("l"))
o_count = int(full_name.count("o"))
v_count = int(full_name.count("v"))
e_count2 = int(full_name.count("e"))

love_count = l_count+o_count+v_count+e_count2
love_count = str(love_count)

love_counter = true_count + love_count

# print(love_counter)
love_counter = int(love_counter)

if(love_counter<10 or love_counter>90):
    print(f"Your score is {love_counter}, you go together like coke and mentos.")
elif(love_counter>40 and love_counter<50):
    print(f"Your score is {love_counter}, you are alright together.")
else:
    print(f"Your score is {love_counter}.")


#Tressure Hunt

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇

user_name = input("Write down your name to start the 'HUNT'? ")

side_selection = input(f"{user_name},You\'re at a crossroad. Where do you want to go? Type 'left' or 'right'? ")

if (side_selection == "left"):
    print("you selected left")
    cross_lake = input(
        'You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across? ')
    if (cross_lake == "wait"):
        house_selection = input(
            "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ")
        if (house_selection == "red"):
            print("You Found the Tresure! congratulations")
        elif (house_selection == "Yellow"):
            print("Eaten by beast! Game Over!")
        else:
            print("You were burned alive, Game over!")
    else:
        print("Wrong answer!, You're dead!")
else:
    print("It\'s a room full of fire. Game Over.")

