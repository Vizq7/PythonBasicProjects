import random, urllib

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

def GetWordFromDictionary():
    print(urllib.request.urlopen("https://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"))

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

userWords = []
userInput = ""
wordToGuess = ""
userFails = 0
GetWordFromDictionary()

while userInput != "q" and userFails < 7:
    PrintUnderlines(wordToGuess, userWords)

    if len(wordToGuess) == len(userWords):
        print("You win!")
        #wordToGuess = GetWordFromDictionary()
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