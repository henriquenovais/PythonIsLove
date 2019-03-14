#This code is the solution of the looping problems in:
# http://programarcadegames.com/index.php?lang=pt&chapter=back_to_looping
#Problem 1
#Create loop that prints out the following text:
# * * * * * * * * * *
#Solution 1

for x in range(0,10):
    print("*", end=" ")
print("")

#Problem 2
#Create loop that prints out the following text:
# * * * * * * * * * *
# * * * * *
# * * * * * * * * * * * * * * * * * * * *
#Solution 2
'''
for x in range(0,10):
    print("*",end=" ")
print("")
for x in range(0,5):
    print("*",end=" ")
print("")
for x in range(0,10):
    print("*",end=" ")
print("")
'''
#Problem 3
#Create loop that prints out the following text:
# * * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * *
#Solution 3:
'''
for x in range(0,10):
    print("")

    for y in range(0,10):
        print("*", end=" ")

print("")
'''

#Problem 4
#Print the following text on screen:
'''
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
'''
#Solution 4
'''
for x in range(0,10):
    print("")
    for y in range(0,5):
        print("*", end=" ")
    if x == 9:
        print("")
'''

#Problem 4
#Print the following text on screen:
'''
* * * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * * *
'''