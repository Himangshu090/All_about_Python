import random
target=random.randint(1,100)

while True:
    user_input = (input("Guess a number between 1 to 100. If you want to quit press Q: "))
    if(user_input=='Q'):
        print("What a loser you are!:v Just Kidding better luck next time")
        break
    user_input= int(user_input)
    if(user_input==target):
        print("You guessed it correct. GAME OVER!")
        break
    elif(user_input<target):
        print("Guessed number is too small. Guess a bigger number")
    elif(user_input>target):
        print("Guessed number is too big. Guess a smaller number")
    else:
        ("Guessed out of range")


