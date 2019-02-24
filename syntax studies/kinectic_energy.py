print("This program was created in order to \ncalculate the kinectic energy of \na given mass.")
mass_string = input("Enter the object's mass in kilograms: ")
mass = float(mass_string)
vel_string = input("Enter the object's speed in meters per second: ")
vel = float(vel_string)

energy = 0.5 * mass * (vel ** 2)

print("The object has " + str(energy) + " joules of energy.")
