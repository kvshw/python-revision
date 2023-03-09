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


