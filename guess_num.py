#guessing the number by user(range- 1 to 100). If he guesses a num less than the generated number, then print guessed num is < generated num and vice versa.
import random
target=random.randint(1,100)
while True:
    user_guess=(input("Guess your number bewtween 1 to 100 or quit(Q) : "))
    if user_guess=="Q":
        break
    if(int(user_guess)<target):
        print("The number you guessed is less than the target number. Please try again")
    elif(int(user_guess)>target):
        print("The number you guessed is greater than the target number. Please try again") 
    else:
        print("You guessed correct number ! congratulations")
        break
print("--GAME OVER !")
