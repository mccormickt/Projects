import random


class hangman():
    lines = []

    def __init__(self):
        f = open("movielist.txt")
        global lines
        lines = f.readlines()

    def play(self):
        global lines
        index = random.randrange(0, len(lines))
        word = lines[index].strip()

        guesses = []
        guess = []
        aList = []
        lives = 6
        string = ""
        aString = ""

        for j in range(0, len(word)):
            aList.append(word[j].upper())
            if word[j] == " ":
                guess.append(" ")
            else:
                guess.append("_")
        for i in guess:
                string = string + i
        print "Phrase: ", string

        while (guess != aList and lives > 0):
            string = ""
            aString = ""
            letter = raw_input("Guess a letter.\n").upper()
            if (not letter.isalpha() or len(letter) != 1):
                print "Invalid input. Please only enter a single letter."
            elif ((letter + " ") in guesses):
                print "You've already guessed that letter!\n"
            else:
                guesses.append(letter + " ")
                for x in range(0, len(word)):
                    if (aList[x] == letter):
                        guess[x] = letter
                for i in guess:
                    string = string + i
                if (letter not in aList):
                    lives -= 1

            print "\nPhrase so far: ", string
            if lives == 6:
                print "  __"
                print " |  l"
                print "_|_ "
            if lives == 5:
                print "  __"
                print " |  l"
                print "_|_ O"
            if lives == 4:
                print "  __"
                print " |  l"
                print "_|_ O"
                print "    |"
            if lives == 3:
                print "  __"
                print " |  l"
                print "_|_ O"
                print "    |"
                print "   /"
            if lives == 2:
                print "  __"
                print " |  l"
                print "_|_ O"
                print "    |"
                print "   / \ "
            if lives == 1:
                print "  __"
                print " |  l"
                print "_|_ O"
                print "   -|"
                print "   / \ "

            for j in guesses:
                aString = aString + j
            print "Letters Guessed: ", aString

        if (lives <= 0):
            print "  __"
            print " |  l"
            print "_|_ O"
            print "   -|-"
            print "   / \ "
            print "You Lose!"
            print "The phrase was: ", word
        elif (guess == aList):
            print "Correct! You win!\n"
        if raw_input("Play Again? Y/N\n").upper() == "Y":
            self.play()
        else:
            print "Thanks for playing!"


man = hangman()
print "Welcome to Hangman!"
man.play()
