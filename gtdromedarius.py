#Import library for generating random numbers:
import random;

#Game introduction
print("Welcome to GTDromedarius.")
print("You have stolen a camel from merchants in the desert,")
print("your mission is to survive the mercenaries hired by the")
print("merchants that want you dead. \n \n")

#Main loop control variable
done = False
kilometers = 0 #Distance covered by the main character in its camel
thrist = 0 #Main character's thrist for water
camel = 0 #Status of the camel
mercenaries = -20 #Distance between mercenaries and main character
canteen_drinks = 10 #Number of drinks in the main character's canteen


while done == False:
	print("A. Drink from your canteen")
	print("B. Move ahead at moderate speed")
	print("C. Move ahead at full speed")
	print("D. Stop and rest")
	print("E. Status check")
	print("Q. Quit game \n")
	choice = input("What is your decision? --> ")
	choice = choice.lower()



	#Checking player, mercenaries, status:
	if choice == "e":
		print("Kilometers traveled: " + str(kilometers))
		print("Drinks in your canteen: " + str(canteen_drinks))
		print("The mercenaries are " + str(-mercenaries) + " miles behind you. ")
    
	#Drink from the canteen:
	elif choice == "a":
		if canteen_drinks <= 0:
			print("You have no water in your canteen.")
		else:
			canteen_drinks = canteen_drinks - 1
			thrist = thrist - 1
			print("You drank water from your canteen, your thrist is reduced. ")
    
    #Going ahead at moderate speed:
	elif choice == "b":
		kilometers = kilometers + random.randrange(4,13) #player travels forward at moderate speed
		mercenaries = mercenaries - random.randrange(4,13) #player travels forward at moderate speed
		mercenaries = mercenaries + random.randrange(6,15) #mercenaries travel forward
		camel = camel + 1
		thrist = thrist + 1
		print("You have traveled: " + str(kilometers) + "kilometers.")
		print("The mercenaries are " + str(-mercenaries) + " miles behind you. ")

	#Going ahead at full-speed:
	elif choice == "c":
		kilometers = kilometers + random.randrange(9,21) #player travels forward at Full-speed
		mercenaries = mercenaries - random.randrange(9,21) #player travels forward at Full-speed
		mercenaries = mercenaries + random.randrange(6,15) #mercenaries travel forward
		camel = camel + random.randrange(0,4)
		thrist = thrist + 1
		print("You have traveled: " + str(kilometers) + "kilometers.")
		print("The mercenaries are " + str(-mercenaries) + " miles behind you. ")

	#Stop the night:
	elif choice =="d":
		camel = 0
		mercenaries = mercenaries + random.randrange(6,15)
		print("You stopped to rest the night.")
		print("Your camel is now fully rested and is happy.")
		print("The mercenaries are " + str(-mercenaries) + " miles behind you. ")

	#Game quitting:
	elif choice == "q":
		done = True

	#If the player is too thristy:
	if thrist > 4 and thrist <= 6:
		print("You are thristy! Drink water from your canteen in order to keep from dehydrating!")

	#If the player does not respect his thrist limit
	elif thrist > 6:
		print("You died of thrist!")
		done = True

	#Warning about the mercenary's distance:
	if mercenaries > -15 and mercenaries > -10:
		print("The mercenaries are getting close! Be careful")
	elif mercenaries > -10 and mercenaries > -5:
		print("You can see the mercenaries behind you!")
	elif mercenaries > -1 and mercenaries > -4:
		print("You can hear the mercenaries behind you! Death draws near.")

	if camel >= 5:
			print("Your camel is getting tired!") 
	elif camel >= 8:
			print("Your camel is dead.")
			print("After walking for hours alone in the desert, the mercenaries found you.")

	if kilometers >= 200:
		print("After days of travelling, you were finally able to shake off the mercenaries.")
		print("You live to see another day, at least for now.")
	print("\n \n")

print("Closing game ...")