import random

def CheckIfInputCorrect(wordToGuess, letter, userWords):
    letterCorrect = False

    for x in wordToGuess:
        if x == letter:
            userWords.append(x)
            letterCorrect = True
    pass
    return letterCorrect

def PrintUnderlines(wordToGuess, userWords):
    for x in wordToGuess:
        if x not in userWords:
            print("_", end=" ")
        else:
            print(x, end=" ")
    print("\n")

def GetRandomWordToGuess(words):
    return words[random.randint(0, len(words) - 1)]

#hangman ascii art from https://github.com/chrishorton
hangmanAscii = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

words = ["python", "programming", "barcelona"]
userWords = []
userInput = ""
wordToGuess = GetRandomWordToGuess(words)
userFails = 0

while userInput != "q" and userFails < 7:
    PrintUnderlines(wordToGuess, userWords)

    if len(wordToGuess) == len(userWords):
        print("You win!")
        wordToGuess = GetRandomWordToGuess(words)
        userWords = []
        userFails = 0
    else:    
        print("Write a letter:", end=" ")
        userInput = input()

        if not CheckIfInputCorrect(wordToGuess, userInput, userWords) and userInput != "q":
            print(hangmanAscii[userFails])
            userFails += 1

            if userFails == 7:
                print("You lost :(")
    pass

print("Exiting the game...")