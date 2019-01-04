#This a simple quiz about the japanese language created in order to practice Python
print("This is a quiz about the Japanese language. \n \n")
correct = [];

print("FIRST QUESTION")
print("Which are the three main parts of the japanese writing system?")
print("a) Hirukuma, Hiragana and Iori")
print("b) Kanji, Hiragana and Katakana")
print("c) Kanji, Himesama and Oujikana")
print("d) Kareshi, Otoko and Hiragana")

answer = raw_input("Select the correct answer by typing the corresponding letter: ")
#The use of the input() method here would be inadequate 
answer = answer.lower()

if answer == "b":
    print("You answered correctly! \n \n")
    correct.append(1)
else:
    print("Incorrect :( \n \n")
    correct.append(0)

print("SECOND QUESTION")
print("_________ are characters of chinese origin used in order to convey multiple meanings \n according to the situation.")
answer = raw_input("Which group of characters in the japanese writing system matches this description? ")
answer = answer.lower()

if answer == "kanji":
    print("You answered correctly! \n \n")
    correct.append(1)
else:
    print("Incorrect :( \n \n")
    correct.append(0)

print("THIRD QUESTION")
print("_________ are characters used primarily for foreign words and names, loanwords, onomatopoeia\n scientific names and sometimes for emphasis.")
answer = raw_input("Which group of characters in the japanese writing system matches this description? ")
answer = answer.lower()

if answer == "katakana":
    print("You answered correctly! \n \n")
    correct.append(1)
else:
    print("Incorrect :( \n \n")
    correct.append(0)

print("FOURTH QUESTION")
print("_________ are characters used for native or naturalised japanese words and grammatical elements")
answer = raw_input("Which group of characters in the japanese writing system matches this description? ")
answer = answer.lower()

if answer == "hiragana":
    print("You answered correctly! \n \n")
    correct.append(1)
else:
    print("Incorrect :( \n \n")
    correct.append(0)

print("RESULTS")
y = len(correct)
for x in range(0,y):
    if correct[x] == 1:
        print("QUESTION " + str(x+1) + ") CORRECT")
    else:
        print("QUESTION " + str(x+1) + ") WRONG")









