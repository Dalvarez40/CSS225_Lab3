#Daniel Alvarez
#10/10/23

#Problem 3 Lab 3

#This program greets the user in differnt ways based on what they input as their name

#Asks the User their Name
user_name = input("What is your name? ")

#If User inputs "Daniel" then it will print "How is your day going"
if user_name == "Daniel":
    print("Hello", user_name + ",", "Nice to meet you")

#If User inputs "Robyn" then it will input "It's a pleasure to meet you"
elif user_name == "Robyn":
    print("Hi there", user_name + ",", "It's a pleasure to meet you")

#If User inputs any other name that is not "Daniel" or "Robyn" then it will print "I'm happy to see you"
else:
    print("Whats up", user_name + ",", "I'm Happy to see you")


