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
	print("Q. Quit game")
	choice = input("What is your decision? --> ")
	choice = choice.lower()

	if choice == "q":
		done = True
		print("Closing game ...")
	elif choice == "e":
		print("Kilometers traveled: " + str(kilometers))
		print("Drinks in your canteen: " + str(canteen_drinks))
		print("The mercenaries are " + str(-mercenaries) + " miles behind you. \n \n")

