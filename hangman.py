# hangman.py

import random

def get_secret_word(word_file="/usr/share/dict/words"):
    with open(word_file) as f:
        good_words = []
        for i in f:
            i = i.strip()
            if len(i) <= 6:     # No short words
                continue
            if not i.isalpha(): # No punctuation
                continue
            if i[0].isupper():  # No proper nouns
                continue
            good_words.append(i)
    return random.choice(good_words)
        

def get_masked_word(word, guesses):
    ret = []
    for i in word:
        if i in guesses:
            ret.append(i)
        else:
            ret.append("*")
    return ''.join(ret)
        

def get_status(secret_word, guesses, remaining_turns):
    return """Secret word : {}
Guessed letters : {}
Remaining turns : {}
""".format(get_masked_word(secret_word, guesses),
           ' '.join(sorted(guesses)),
           remaining_turns)

    

def main():
    secret_word = get_secret_word()
    guesses = []
    while True:
        letter = input("Enter a letter ")
        remaining_turns, success = play_round(secret_word, guesses, letter, remaining_turns)
        print (get_status(secret_word, guesses, remaining_turns))
        if remaining_turns == 0:
            print ("The secret word was {}".format(secret_word))
            break
        if success:
            print ('You did it!')
            break


if __name__ == "__main__":
    main()

            
        
