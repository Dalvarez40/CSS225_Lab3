#Daniel Alvarez
#10/16/23

#Problem 7 Lab 3

#This program calculates the return day of a vacation

#Asking User to input the starting day
Starting_Day= int(input("Please enter the starting day"))

#Asking User to input the length of stay
Length_of_Day= int(input("Please enter the length of stay"))

#Caculating the remainder by Starting_Day and Length_of_Day divided by 7
Return_Day= (Starting_Day + Length_of_Day) % 7

#Printing the result of Return_Day
print("You will return on day",Return_Day)