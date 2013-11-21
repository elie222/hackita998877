'''
Created on 21 Nov 2013

@author: Elie2
'''
import string
from bottle import route, run, request

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

def html_list(text, ordered):
    lines = text.split('\n')
    list_tag = 'ol'
    if not ordered:
        list_tag = 'ul'
    return '<%s>\n%s\n</%s>' % (list_tag, "\n".join(["<li>%s</li>" % line for line in lines]), list_tag)

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
    
#     print html_list('asdgjsfhg jsdhfg jhsdgf jhsdfg jsdhf\nsdfsdf\nsfdsg\nsdfsdf', True)
#     print html_list('asdgjsfhg jsdhfg jhsdgf jhsdfg jsdhf\nsdfsdf\nsfdsg\nsdfsdf', False)

    print '===success==='

# main()

@route('/listomator')
def listomator():
    if request.query:
#         print request.query.text
#         print request.query.ordered
        return html_list(request.query.text, (request.query.ordered == 'ordered'))
    
    return """
        <form>
            <textarea name="text">Enter text here...</textarea><br>
            <input type="checkbox" name="ordered" value="ordered">Display as ordered list<br>
            <input type="submit">
        </form>
    """
    
@route('/mult_table')
def mult_table():
    if request.query:
        table = multiplication_list(int(request.query.n))
#         return '<table>%s</table>' % '\n'.join([' '.join([table[row][col] for col in table[row]]) for row in table])
        return '<table border=1>%s</table>' % "\n".join(["<tr>%s</tr>" % "".join(["<td>%d</td>" % cell for cell in row]) for row in table])
    
    return """
        <form>
            <input type="text" name="n" placeholder="Enter a number"><br>
            <input type="submit">
        </form>
    """
    
@route('/countries')
def countries():
    f = open('cow.txt', 'r')
    html = ''
    
    for line in f:
        if not line.strip()[0] == '#' and len(line.split('; ')) > 1:
            country_name = line.split('; ')[4]
            html += '<a href="/country/%s">%s<br>' % (country_name, country_name)
    f.close()
    
    return html

@route('/country/<name>')
def country(name):
    return '<h1>Country page: %s</h1>' % name

run(host='localhost', port=8080, debug=True, reloader=True)

