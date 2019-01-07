#Game introduction
print("Welcome to GTDromedarius.")
print("You have stolen a camel from merchants in the desert,")
print("your mission is to survive the mercenaries hired by the")
print("merchants that want you dead. \n \n")

#Main loop control variable
done = False

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
