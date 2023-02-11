import random

#Loads saved data from the file "Words"
with open("Words", "r") as file:
    words = [i for i in file.read().split("\n") if i != ""]

#Saves data to the file "Words"
def saveData():
    with open("Words", "w") as file:
        file.truncate(0)
        for i in words:
            file.write(i)
            file.write("\n")

#New words are entered into the possible list of words which can possibly be the words of the hangman.
def enterWords():

    while True:
        try:
            print("\n-----------------------------------------------------")
            choice = int(input("Enter 1. = Enter new word"
                               "\nEnter 2. = Go back to main menu"
                               "\nPlease Enter your choice (1 - 2): "))

            if choice == 1:
                words.append(input("Please enter the new word: ").lower())
            elif choice == 2:
                break
        except:
            print("Please enter a valid number! (1 - 2).")

def playHangman():

    lives = 7
    gameOver = False
    word = random.choice(words)
    answer = ["_" for i in range(0, len(word))]
    incLetters = list()
    while gameOver == False:

        print("\n---------------------------------")

        # Prints the already entered incorrect letters
        print("Incorrect letters entered: ", end="")
        for i in incLetters:
            print(i, end=", ")

        print("\n")
        # Prints the current answer.
        for i in answer:
            print(i, end="")

        print("\n\nLives left: " + str(lives))

        letter = input("\nPlease enter the letter of your choice: ").lower()

        # Gets the user's inputted letter, and checks if it is correct (if it exists in the word).
        wordIndex = 0
        isLetterValid = False
        # The program checks if the inputted letter, matches with ANY of the letters in the word.
        for i in word:
            if i == letter:
                isLetterValid = True
                # If the user already entered the letter, and it's correct anyways, a message is displayed.
                if answer[wordIndex] == "_":
                    answer[wordIndex] = letter
                else:
                    print("\nYou already entered that letter! (correctly)")
                    break
            wordIndex += 1

        # If the letter doesn't seem to match any of the letters in the word, a live is taken (unless the incorrect
        # letter was already entered before)
        if isLetterValid == False:
            if incLetters.__contains__(letter):
                print("\nThis incorrect letter was already entered!")
            else:
                lives -= 1
                incLetters.append(letter)

        if lives <= 0:
            gameOver = True

        #If any of the characters of the answer are still blank, then the game isn't complete. (it isnt won)
        gameWon = True
        for i in answer:
            if i == "_":
                gameWon = False

        if gameWon == True:
            gameOver = True
            print("\n--------------")
            print("You won!")
            print("--------------")
        elif gameWon == False and gameOver == True:
            print("\n--------------")
            print("You lost!")
            print("--------------")

#The menu is displayed.
def menu():
    while True:
        try:
            print("\n--------------------------------------------------------------------------")
            menuChoice = int(input("Enter 1. = Enter new words into the collection of possible words"
                                   "\nEnter 2. = Play Hangman"
                                   "\nEnter 3. = Quit"
                                   "\nPlease enter your choice (1 - 3): "))
            if menuChoice == 1:
                enterWords()
            elif menuChoice == 2:
                playHangman()
            elif menuChoice == 3:
                break
        except:
            print("Please enter a valid number! (1 - 3).")


menu()
saveData()
