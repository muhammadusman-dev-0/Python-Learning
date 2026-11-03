#import random
#def game ():
    #print("you are playing the game....")
    #score=random.randint(1,100)

#with open("hiscore.txt") as f :
    #hiscore=f.read()
    #if (hiscore!=""):
        #hiscore=int(hiscore)
    #
    #else:
        #hiscore==0


    #print(f" your score : {score}")

    #if (score>hiscore):
        #with open("hiscore.txt","w") as f:
            #f.write(hiscore)
    #return score

#game()
    
import random

def game():
    print("You are playing the game....")

    score = random.randint(1, 100)

    with open("hiscore.txt", "r") as f:
        hiscore = f.read()

        if hiscore != "":
            hiscore = int(hiscore)
        else:
            hiscore = 0

    print(f"Your score is: {score}")

    if score > hiscore:
        with open("hiscore.txt", "w") as f:
            f.write(str(score))
        print("New High Score!")

    return score


game()














