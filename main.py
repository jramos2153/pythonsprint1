"""My Sweet Integration Program"""
__author__ = "Jesus Ramos"
#Jesus Ramos
# In this program, users will be able to solve elementary mathematical equations and graph.
name = input("Please enter your name: ")

print("Welcome", name, "!")

gender = input("Before we start, tell us a bit about your self. Are you male or female? ")

print("It's nice to know that you are a", gender)

age = input("What is your age? ")

print("Wow", age, "is so old!")

number = input("Thanks for sharing all of this information! What's your favorite number?")

print(number, "is a lame number, definitely not my favorite!")

operation = input("Since we're talking about numbers, what is your favorite math operation?")

print("Nice to know that", operation, "is your favorite, why don't we practice a few problems to get warmed up! ")

input("Let's start off with addition, what is 2 + 2?")   # using first numeric operator (addition)

a = 2
b = 2
print("Let's check, smarty pants. Answer:", a + b)

input("How about 2 - 2?")   # using second numeric operator (subtraction)

print("Hmmm, let's see if you got it! Answer:", a - b)

input("Let's kick it up a notch, what's 2 x 2?")   # using third numeric operator (multiplication)

print("Will you get this one right? Answer:", a * b)

input("We're almost done with warm up, what's 2 divided by 2?")

print("Let's see if you got it. Answer:", a / b)

#line above shows fourth numeric operator (division)
input("That was a good warm up, let's step up our game. What is the remainder when you divide 85 by 15?")

c = 85
d = 15
print("Annnnddd the answer is: ", c % d)

#the line above shows the modular operator being used
input("Let's test how good your math skills really are. What is 85 raised to the power of 15?")

print("Let's see if you got it. Answer:", c ** d)

input("How about this, what is 85 divided by 15, to the nearest whole number when rounded down?")

print("The correct answer is:", c // d)

#line above shows the floor division numeric operator being used
input("That was still easy, what about x + 5 if x = 10?")

x = 10
x += 5
print("Let's see, the correct answer is: ", x)

#line above shows assignment and shortcut operator being used
