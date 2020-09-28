# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

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

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    letterDict = {}
    for char in secretWord:
        letterDict[char] = 1
    for x in lettersGuessed:
        if x in letterDict:
            letterDict[x] = 0
    
    if 1 in letterDict.values():
        return False
    else:
        return True    



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    hint = []
    stringHint = ''
    letterDict = {}
    for char in secretWord:
        letterDict[char] = 1
    for x in lettersGuessed:
        if x in letterDict:
            letterDict[x] = 0
    
    for y in secretWord:
        if letterDict[y] == 0:
            hint.append(y)
        else:
            hint.append('_ ')
    for j in hint:
        stringHint += j
    return stringHint
    



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    
    stringAvail = ''
    
    avail = list(string.ascii_lowercase)
    
    for char in lettersGuessed:
        if char in avail:
            avail.remove(char)
    
    for j in avail:
        stringAvail += j
    
    return stringAvail    

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
    # FILL IN YOUR CODE HERE...
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is', len(secretWord), 'letters long.')
    
    lettersGuessed = []
    
    guesses = 8
    guessLetter = ''
    
    while isWordGuessed(secretWord, lettersGuessed) == False:
        if guesses == 0:
            break
        print('-----------')
        print('You have', guesses, 'guesses left.')
        print('Available letters:', getAvailableLetters(lettersGuessed))
        guessLetter = input('Please guess a letter: ')
        gLower = guessLetter.lower()

        if gLower not in getAvailableLetters(lettersGuessed):
            print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
            
        else:
            lettersGuessed.append(gLower)
            if gLower in secretWord:
                print('Good guess:', getGuessedWord(secretWord, lettersGuessed))
            else:
                print("Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed))
                guesses -= 1
        guessLetter = ''
        
    print('-----------')
    if guesses == 0:
        print('Sorry, you ran out of guesses. The word was', secretWord + '.')
    else:
        print('Congratulations, you won!')
        
    


secretWord = chooseWord(wordlist).lower()
#secretWord = 'escort'
hangman(secretWord)
