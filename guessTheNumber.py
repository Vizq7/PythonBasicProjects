import random

userInput = ""
rndNumber = random.randint(1, 10)

print("Type 0 to exit")

while userInput != 0:
    print("Enter one number:")
    try:
        userInput = int(input())
        if userInput != 0:
            if userInput == rndNumber:
                print("Correct number!")
                userInput = "q"
            elif userInput > rndNumber:
                print("Number too high")
            else:
                print("Number too low")
    except ValueError:
        pass
    pass