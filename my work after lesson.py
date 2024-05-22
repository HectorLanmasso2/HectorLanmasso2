# type conversion
# type conversion (implicit and explicit)
# explicit conversion
num_str = ("123")
num_int = int(num_str)
print(num_int)
num_float = float(num_int)
print(num_float)

number = 9
print(type(number))

float_number = 9.0
print(type(float_number))

converted_float_number = int(float_number)
print(type(converted_float_number))
print(converted_float_number)

# variable
a = 1  # a is a variable
print("a = " + str(a)) # it's the printing of variable "a"
greetings = "greetings2"   # assignment of new variable
print("greetings = " + str(greetings))  # printing the variable
greetings = 7   # reassignment of a new value of variable
print("greetings = " + str(greetings))

height = 5.9
print("Type:", type(height))

c = d = 4 # chained assignment
print("c = " + str(c))
print("d = " + str(d))
print("c = " + str(c), "d = " + str(d)) # printing of chained assignment

numbers = [1, 2, 3, 4, 5]
print("Type:", type(numbers))

# Bolean
# logical statement
is_student = True
is_teacher = False
print("result_and = is_student and is_teacher")
print("result_or = is_student or is_teacher")
print("result_not = not is_student")

# dict
my_dict = {"name": "alexia", "age": "32", "city": "porto", "job": "lawyer", "email": "lanmassohector@gmail.com", "color": "white"}
print("my_dict:", type(my_dict))
print("city:", my_dict["city"])
my_dict["size"] = "40"
print("updated dictionary:", my_dict)
del my_dict["age"]
print("dictionary after removing 'age':", my_dict)
print("iterating over the dictionary:")
for key, value in my_dict.items():
    print(key + ":", value)

monty_python = "Monty Python" # assignment of string
print(monty_python)

print(monty_python.lower()) # used to print the string value in lower characters
print(monty_python.upper())  # used to print the string value in upper characters
print(monty_python.split(" "))  # used to separate the string value one at one
print("_".join(monty_python.split(" ")))  # used to insert a value after every value into the string

# string
string = " hello, boy! " # assignment of string
print(string.strip())

string = "Hello friend!"  # new assignment of string
new_string = string.replace("friend", "world") # assignment of new_string = replace friend by world into the old string
print(new_string)

types_of_people = 10  # values of types of people
x = f'There are {types_of_people} types of people.'  # value of x

binary = 'binary'  # value for binary
do_not = "don't"   # value for do not
y = f'Those who know {binary} and those who {do_not}.'  # stings for string binary and do not

print(x)  # show 'x' value
print(y)  # show 'y' value

print(f'I said: {x}')  # show string in string
print(f"I also said: '{y}'")  # show string in string

hilarious = False # value of hilarious
joke_evaluation = "Isn't that joke so funny?! {}"  # value of joke evaluation

print(joke_evaluation.format(hilarious))  # show string joke evaluation * format of hilarious

w = "This is the left side of..."  # define value of w
e = "a string with a right side."  # define value of e

print(w + e)  # show w + e

# index
string = "Hello beninese people" # assignment value of string
index = string.find("people") # define the word for who we find index
print("index of people:", index)

# count
string = "I'm alive! I'm alive"
count = string.count("alive") # define the world what we count into the string
print("count:", count)

string = "Hello guy, i'm there" # assignment of string
print(string.startswith("Hello")) # define the world who let or no the condition
print("String_startswith_Hello=", string.startswith("Hello"))

# conatination
first_name = "Mahugnon Hector"
last_name = "Lanmasso"
full_name = first_name + " " + last_name
print("Full Name:", full_name)


# calculator
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,"in each car.")

my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

#
print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")

#
import re
text = "We are doing today session of Zeleus learning"
pattern = r'doing'
match = re.search(pattern, text, re.IGNORECASE)
if match:
    print("pattern found:", match.group())

text = "We are doing today session of Zeleus learning"
pattern1 = r'doing.*session'  # .* Signifie les mots compris entre "doing" et "session" y compris
match = re.search(pattern1, text, re.IGNORECASE)
if match :
    print("pattern found:", match.group())
else :
    print("pattern not found")

text = "We are doing today session of Zeleus learning"
pattern2 = r"\bdoing\b.*\bsession\b"  #
match = re.search(pattern2, text, re.IGNORECASE)
if match :
    print("pattern found:", match.group())
else :
    print("pattern not found")








