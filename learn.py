'''
Created on 21 Nov 2013

@author: Elie2
'''

def hello_world():
    return "Hello World"

def hello_you(you):
    return "Hello %s" % you

def beer_on_the_wall_lyrics(n):
    lyrics = ["%d bottles of beer on the wall, %d bottles of beer.\n"
    "Take one down, pass it around, %d bottles of beer on the wall..." % (i, i, i-1) for i in range(n,0,-1)]
    return lyrics

def gematria():
    pass
    
assert hello_world() == "Hello World"

you = "Foo"
assert hello_you(you) == "Hello %s" % you
# assert beer_on_the_wall_lyrics(99) ==
n = 5 
lyrics = beer_on_the_wall_lyrics(n)
for line in lyrics:
    print line
    
assert len(lyrics) == n

print "\n===success==="
