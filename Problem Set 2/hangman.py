# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
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


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    g = True
    for ch in secret_word :
          if ch in letters_guessed:
                continue
          else:
                g = False
    return g
# print (is_word_guessed('apple',['e','a','p','p','l','s']))

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    out = ['_ ']*len(secret_word)
    for i in range (len(secret_word)):
          if secret_word [i] in letters_guessed:
                out [i] = secret_word[i]
    str = ""
    for ch in out:
          str = str + ch
    return (str)
#print(get_guessed_word('apple',['e','i','k','p','r','s']))

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    str = string.ascii_lowercase
    x = ""
    for ch in str:
      if (not (ch in letters_guessed)):
        x = x + ch
    return x
# print (get_available_letters(['e','i','k','p','r','s']))
def hangman(secret_word):
    # '''
    # secret_word: string, the secret word to guess.
    
    # Starts up an interactive game of Hangman.
    
    # * At the start of the game, let the user know how many 
    #   letters the secret_word contains and how many guesses s/he starts with.
      
    # * The user should start with 6 guesses

    # * Before each round, you should display to the user how many guesses
    #   s/he has left and the letters that the user has not yet guessed.
    
    # * Ask the user to supply one guess per round. Remember to make
    #   sure that the user puts in a letter!
    
    # * The user should receive feedback immediately after each guess 
    #   about whether their guess appears in the computer's word.

    # * After each guess, you should display to the user the 
    #   partially guessed word so far.
    
    # Follows the other limitations detailed in the problem write-up.
    # '''
    k = len (secret_word)
    g = 6
    w = 3
    f = False
    guesses = []
    print ('welcome to the game Hangman!')
    print ('I am thinking of a word that is ',k,' letters long.')
    print ('You have ',w,' warnings left.')
    print ('-----------')
    while g > 0:
          print ('You have ',g,' guesses left.')
          print ('Available letters: ',get_available_letters(guesses))
          ch = (input ("Please guess a letter: "))
          if ch.isalpha() :
                if ch in get_available_letters(guesses):
                    guesses.append(ch)
                    if ch in secret_word :
                          print ("Good guess: ",get_guessed_word(secret_word,guesses))
                    else :
                          if isVowel (ch):
                            print ("Oops! That letter is not in my word: ",get_guessed_word(secret_word,guesses))
                            g = g - 2
                          else :
                            print ("Oops! That letter is not in my word: ",get_guessed_word(secret_word,guesses))
                            g = g - 1
                else:
                    print ('Word has already been guessed')
                    if w > 0 :
                          w = w - 1
                          print ("Oops! That is not a valid letter. You have ",w," warnings left:",get_guessed_word(secret_word,guesses))

                    else :
                          g = g - 1
                          print ("Oops! That is not a valid letter. You are out of warnings and have ", g, " guesses left : ",get_guessed_word(secret_word,guesses))
          else :
                if w > 0 :
                      w = w - 1
                      print ("Oops! That is not a valid letter. You have ",w," warnings left:",get_guessed_word(secret_word,guesses))

                else :
                      g = g - 1
                      print ("Oops! That is not a valid letter. You are out of warnings and have ", g," guesses left : ",get_guessed_word(secret_word,guesses))
          print("---------")
          if (get_guessed_word(secret_word,guesses)) == secret_word :
                f = True
                print ("Congratulations, you Won!")
                print ("Your score is ",(g*len(set(list(secret_word)))))
                break
    if not f :
      print ("Sorry! You have run out of guesses, the word was", secret_word)
                

def concat (str):
  '''
  Concatenating words
  '''          
  x = ""
  for ch in str :
        x = x + ch
def isVowel (ch):
  '''
  Checking if the given string is a vowel or not  
  '''
  return (ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u')
# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    word2 = list (other_word.strip())
    g = True
    x = my_word.replace(' ','')
    word = list (x.strip())
    if len (word) != len (word2) :
          return False
    else :
          for i in range (len (word)):
                if word[i].isalpha():
                      g = g and word [i] == word2 [i]
    return g
print (match_with_gaps("a_ ple","apple"))

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
