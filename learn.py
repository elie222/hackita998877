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

def multiplication_list(n):
    return [[i*j for j in range(n+1)] for i in range(n+1)]

def letter_count(word):
    counts = {}
    for letter in string.lowercase:
        counts[letter] = word.count(letter) 
    return counts

def palindromes(sentence):
    words = sentence.split()
    return [word for word in words if palindrome(word)]

def most_common_word(sentence):
    words = sentence.split()
    return max(words, key=words.count)
    
    # first attempt. works too
#     count_dict = {}
#     for word in words:
#         if word in count_dict:
#             count_dict[word] += 1
#         else:
#             count_dict[word] = 1
#             
#     return max(count_dict, key=count_dict.get)

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
    
    assert multiplication_list(12)[12][12] == 144
    assert multiplication_list(88)[75][33] == 75*33
    
    assert letter_count('aaaba')['a'] == 4
    assert letter_count('aaaba')['b'] == 1
    assert letter_count('aaaba')['c'] == 0
    
    assert palindromes('qweewq adgsdhfg sdhjfg sfdjhgsfdh sdfhj abbba cdefedc') == ['qweewq', 'abbba', 'cdefedc']
    
    assert most_common_word('abc abc def def ghhh gghh def') == 'def'

    print "\n===success==="



main()