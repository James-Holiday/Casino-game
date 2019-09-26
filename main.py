import random

print('''
$$$$$$$$$$            
$$$$    $$$      $$$$$$$$$$$$$ 
$$$$    $$$    $$$    $$$ $$$$     $$$$    $$$    $$$$   $$$$ 
$$$$$$$$$$$   $$ $$   $$$ $$$$$   $$$$$   $$ $$   $$$$$  $$$$ 
$$$$$$$$$$$ $$     $$ $$$ $$$ $$ $$ $$$ $$     $$ $$$$$$ $$$$ 
$$$$    $$$ $$$$$$$$$ $$$ $$$   $   $$$ $$$$$$$$$ $$$$ $$$$$$
$$$$    $$$ $$     $$ $$$ $$$       $$$ $$     $$ $$$$  $$$$$
$$$$$$$$$$  $$     $$ $$$ $$$       $$$ $$     $$ $$$$   $$$$
welcome's you to The Gotham City Slots...
Try your luck with 1000 dollars. If you run 
out, don't worry you can always buy back in...

To win you must get one of the following combinations:
Batman\tBatman\tBatman\tpays\t$500
Robin\tRobin\tRobin\tpays\t$250
Alfred\tAlfred\tAlfred\tpays\t$100
Batman\tRobin\tAlfred\tpays\t$1000
Penguin\tPenguin\tPenguin\tpays\t$25
Joker\tJoker\tJoker\tpays\t$7
Riddler\tRiddler\tRiddler\tpays\t$5
Penguin\tjoker\tRiddler\tpays\t$-100
''')



INIT_STAKE = 1000
ITEMS = ["Batman", "Robin", "Alfred", "Penguin", "Joker", "Riddler"]

firstWheel = None
secondWheel = None
thirdWheel = None
stake = INIT_STAKE

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
        answer = input("You have $" + str(stake) + ". Would you like to play? ")
        answer = answer.lower()
        if(answer == "yes" or answer == "y"):
            return True
        elif(answer == "no" or answer == "n"):
            print("GAME OVER!!! You cashed out with $" + str(stake) + " in your hand.")
            return False
        else:
            print("KA-POW!!! Try again")

def spinWheel():
    randomNumber = random.randint(0, 3)
  
    return ITEMS[randomNumber]

def printScore():
   
    global stake, firstWheel, secondWheel, thirdWheel
    if((firstWheel == "Riddler")and (secondWheel == "Riddler")and (thirdWheel == "Riddler")):
        win = 5
    elif((firstWheel == "Joker")and (secondWheel == "Joker")and (thirdWheel == "Joker")):
        win = 10
    elif((firstWheel == "Penguin")and (secondWheel == "Penguin")and (thirdWheel == "Penguin")):
        win = 25
    elif((firstWheel == "Penguin")and (secondWheel == "Joker")and (thirdWheel == "Riddler")):
        win = -100
    elif((firstWheel == "Alfred")and (secondWheel == "Alfred")and (thirdWheel == "Alfred")):
        win = 100
    elif((firstWheel == "Robin")and (secondWheel == "Robin")and (thirdWheel == "Robin")):
        win = 250
    elif((firstWheel == "Batman")and (secondWheel == "Batman")and (thirdWheel == "Batman")):
        win = 500
    elif((firstWheel == "Batman")and (secondWheel == "Robin")and (thirdWheel == "Alfred")):
        win = 1000
    else:
        win = -5

    stake += win
    if(win > 0):
        print(firstWheel + '\t' + secondWheel + '\t' + thirdWheel + ' -- You win $' + str(win))
    else:
        print(firstWheel + '\t' + secondWheel + '\t' + thirdWheel + ' -- You lose')



reel()