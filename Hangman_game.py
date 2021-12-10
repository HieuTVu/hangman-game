import random

import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


wordlist = loadWords()
print("")


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for i in secretWord:
        if i not in lettersGuessed:
            check = False
            break
        else:
            check = True
    return check



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    result = list(len(secretWord)*'_')
    for i in lettersGuessed:
        char = 0
        while char < len(secretWord):
            if i == secretWord[char]:
                result[char] = i
            char += 1
    return ' '.join(result)              



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    stock=list(string.ascii_lowercase)
    for i in lettersGuessed:
        if i in stock:
            stock.pop(stock.index(i))
    return ''.join(stock)


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secretWord) ,"letters long.")
    num_guess = 8
    lettersGuessed = []
    guessedWord = []
    while isWordGuessed(secretWord, lettersGuessed) == False:
        print("You have",num_guess, "guesses left")
        print("Available letters: ",getAvailableLetters(lettersGuessed))
        guess = input("Please guess a letter: ")
        guess = guess.lower()
        if guess in lettersGuessed:
            print("Oops! You've already guessed that letter: ",guessedWord,"\n----------")
        else:
            lettersGuessed.append(guess)
            guessedWord = getGuessedWord(secretWord, lettersGuessed)
            if guess in secretWord:
                print("Good guess: ",guessedWord,"\n----------")
            else:
                print("Oops! That letter is not in my word: ",guessedWord,"\n----------")
                num_guess -= 1
                if num_guess == 0:
                    break
        continue
    if num_guess > 0:
        print("Congratulations, you won!")
    else:
        print("Sorry, you ran out of guesses. The word was else.")


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
