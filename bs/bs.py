# Code below gets the example.html file and turns it into a beautifulsoup object
import bs4

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile, 'html.parser')
type(exampleSoup)

# ---------------------------------------------------
# Code below shows what one can do with bs by selecting a tag w/ an 'author' id

elems = exampleSoup.select('#author')
type(elems)
# Line above results in: <class 'list'>

len(elems)
# Line above results in: 1

type(elems[0])
# Line above results in: <class 'bs4.element.Tag'>

str(elems[0])
# Line above results in: '<span id="author">Al Sweigart</span>'

elems[0].getText()
# Line above results in: 'Al Sweigart'

elems[0].attrs
# Line above results in: {'id': 'author'}

# ---------------------------------------------------
# Code below shows what one can do w/ bs by selecting all 'p' tags

pElems = exampleSoup.select('p')
str(pElems[0])
# Line above results in: '<p>Download my <strong>Python</strong> book from <a href="https://
# inventwithpython.com">my website</a>.</p>'

pElems[0].getText()
# Line above results in: 'Download my Python book from my website.'

str(pElems[1])
# Line above results in: '<p class="slogan">Learn Python the easy way!</p>'

pElems[1].getText()
# Line above results in: 'Learn Python the easy way!'
