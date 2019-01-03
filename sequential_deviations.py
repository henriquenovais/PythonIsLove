a = float(input("Insert the value of the variable A: "))
b = float(input("Insert the value of the variable B: "))
#In python use = to assign values and == to do comparisons

'''
a = float(input("Insert variable here: "))

is the very same as:

a_string = input("Insert variable here:")
a = float(a_string)
'''
'''
if a >= 500:
    print("Variable A's value is equal or bigger than five hundred.")

if a < 500:
    print("Variable A's value is less than five hundred")

if a == 69 or a == 76:
    print("Variable A's value is equal to sixty-nine or equal to seventy-six")

if b != 100 and b > 50:
    print("Variable B's value is bigger than fifty and not equal to a hundred")
else:
    print("Well, conditions were not met buddy")
'''
if a > 50 and b < 50:
    print("50 is an important number to you dude")
elif a < 0 or b < 0:
    print("You typed at least a negative number, huh...")
else:
    print("You typed numbers, that's nice.")