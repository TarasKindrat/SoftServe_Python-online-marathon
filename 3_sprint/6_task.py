"""
Generator function randomWord has as an argument list of words. It should return any random word from this list. Each time words are different until the end of the list is reached. Then words are taken from the initial list again.


For example if

list = ['book', 'apple', 'word']

then possible output example

first call of next(random(list)) returns apple

second call of next(random(list)) returns book

third call of next(random(list)) returns word
fourth call of next(random(list)) returns book
"""