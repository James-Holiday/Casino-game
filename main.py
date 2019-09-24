import random 

print ('''Welcome to the Gotham City Slots...
Try your luck with 100 dollars. If you run 
out of money don't worry you my buy back in''')

INIT_STAKE =100
ITEMS = ["Batman", "Robin", "Alfred", "Penguin", "Joker", "Riddler"]

firstWheel = None
secondWheel = None 
thirdWheel = None
state = INIT_STAKE

def reel():
    global stake, firstWheel, secondWheel, thirdWheel
    playQuestion = askPlayer()
    while(stake != 0 and playQuestion == True):
        firstWheel = spinWheel()
        secondWheel = spinWheel()
        thirdWheel = spinWheel()
        printScore()
        playQuestion = askPlayer()

def askPlayer():
    global stake
    while(True):
        answer = input("You have $" + str(stake) + "Would you like to play?")
        if(answer == "y"):
            return True
        elif(answer == "n"):
            print("GAME OVER!!! You cashed out with $" +str(stake))
            return False
        else:
            print("try again")

def spin():
    randomNumber = random.randint(0, 5)
    return ITEMS[randomNumber]

def score():
    global stake, firstWheel, secondWheel, thirdWheel
    if((firstWheel == "Riddler")and (secondWheel == "Riddler")and (thirdWheel == "Riddler"):
        win = 5
    elif((firstWheel == "Joker")and (secondWheel == "Joker")and (thirdWheel == "Joker")):
        win = 10
    elif((firstWheel == "Penguin")and (secondWheel == "Penguin")and (thirdWheel == "Penguin")):
        win = 25
    elif((firstWheel == "Alfred")and (secondWheel == "Alfred")and (thirdWheel == "Alfred")):
        win = 100
    elif((firstWheel == "Robin")and (secondWheel == "Batman")and (thirdWheel == "Batman")):
        win = 250
    elif((firstWheel == "Batman")and (secondWheel == "Joker")and (thirdWheel == "Joker")):
        win = 500
    else:
        win = -1

    

play()