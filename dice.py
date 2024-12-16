import random

while True:
    k=input("enter y/n to roll the dice: ").lower()
    if(k=='y'):
        d1=random.randint(1,6)
        d2=random.randint(1,6)
        print(f"({d1},{d2})")
    elif(k=='n'):
        break
    else:
        continue
print("GameOver")
