import random
rand = random.randrange(0,10)
guess = int(input("what is your guess"))
numguesses = 0
while (rand!= guess):
    if(rand > guess):
        print ("guess a higher number")
    else:
        print("guess a lower number")
    guess = int(input("guess again"))
if (rand == guess):
    print ("you got the number, Nice job!")