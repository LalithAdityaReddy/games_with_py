import random
choices=('r','p','s')
val={'r':'🪨','p':'📃','s':'✂'}
while True:
    k=input("Enter your choice (r/p/s) to play and e to exit:")
    if(k=='e'):
        break
    if(k not in choices):
        print("Invalid choice !")
    c1=random.choice(choices)
    print("you chose",val[k],"and computer chose ",{val[c1]})
    if((k=='r' and c1=='s')or(k=='s' and c1=='p')or(k=='p'and c1=='r')):
        print("you won the game over computer")
    elif(k==c1):
        print("Match Draw")    
    else:
        print("computer won the game")
print("GAME OVER")

