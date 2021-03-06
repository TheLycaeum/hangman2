# test_hangman.py

import hangman

# 1. Secret word should have atleast 6 letters
# 2. Secret word should have no punctuation
# 3. Secret word should not be a proper noun

def test_secret_word_6_letters():
    assert all(hangman.get_secret_word("./test_data/1.words") == "policeman" for _ in range(100))

def test_secret_word_no_punctuation():
    assert all(hangman.get_secret_word("./test_data/2.words") == "fireman" for _ in range(100))

def test_secret_word_no_proper_nouns():
    assert all(hangman.get_secret_word("./test_data/3.words") == "policeman" for _ in range(100))


def test_get_masked_word():
    assert hangman.get_masked_word('elephant', ['x', 'e', 'l', 'q']) == 'ele*****'
    assert hangman.get_masked_word('elephant', []) == '********'
    assert hangman.get_masked_word('elephant', ['e', 'l', 'p', 'h', 'a', 'n', 't',]) == 'elephant'

    
def test_get_status():
    actual_status = hangman.get_status('elephant', ['x','e','l'], 7)
    expected_status = """Secret word : ele*****
Guessed letters : e l x
Remaining turns : 7
"""
    assert actual_status == expected_status


def test_play_round_correct_guess():
    guesses = ['e','l','x']
    ret, success = hangman.play_round('elephant', guesses, 'p', 8)
    assert ret == 7 
    assert guesses == ['e', 'l', 'x', 'p'] 
    assert success == False

    
def test_play_round_wrong_guess():
    guesses = ['e','l','x']
    ret, success = hangman.play_round('elephant', guesses, 'j', 8)
    assert ret == 7 
    assert guesses == ['e', 'l', 'x', 'j'] 
    assert success == False

def test_play_round_repeat():
    guesses = ['e','l','x']
    ret, success = hangman.play_round('elephant', guesses, 'x', 8)
    assert ret == 8
    assert guesses == ['e', 'l', 'x'] 
    assert success == False

def test_play_round_complete():
    guesses = ['e','l','p','h','a','n']
    _, success = hangman.play_round('elephant', guesses, 't', 8)
    assert success
    

    
    

    
    
