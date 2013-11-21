'''
Created on 21 Nov 2013

@author: Elie2
'''
import string

def hello_world():
    return "Hello World"

def hello_you(you):
    return "Hello %s" % you

def beer_on_the_wall_lyrics(n):
    lyrics = ["%d bottles of beer on the wall, %d bottles of beer.\n"
    "Take one down, pass it around, %d bottles of beer on the wall..." % (i, i, i - 1) for i in range(n, 0, -1)]
    return lyrics

def gematria(letter):
    g = {
         'a': 1,
         'b': 2,
         'c': 3,
         'd': 4,
         'e': 5,
         'f': 6,
         'g': 7,
         'h': 8,
         'i': 9,
         'j': 10,
         'k': 20,
         'l': 30,
         'm': 40,
         'n': 50,
         'o': 60,
         'p': 70,
         'q': 80,
         'r': 90,
         's': 100,
         't': 200,
         'u': 300,
         'v': 400,
         'w': 500,
         'x': 600,
         'y': 700,
         'z': 800
         }
    return g[letter]

def palindrome(word):
    word_without_punc = word.translate(None, string.punctuation)
    reverse = word_without_punc[::-1]
    return reverse == word_without_punc

def main():
    
    assert hello_world() == "Hello World"

    you = "Foo"
    assert hello_you(you) == "Hello %s" % you

    n = 5 
    lyrics = beer_on_the_wall_lyrics(n)
    # for line in lyrics:
    #     print line
    assert len(lyrics) == n

    assert gematria('v') == 400
    
    assert palindrome('abcba')
    assert not palindrome('asdabbcba')
    assert palindrome('ab,c.ba')

    print "\n===success==="



main()