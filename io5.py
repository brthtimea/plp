
from bs4 import BeautifulSoup
#BeautifulSoup4 is used for finding specific elements present in the HTML code.
#It allows us to isolate any specific tag like 'a' or 'div' or any other tag.
#It also lets us play around with its contents.
import urllib2
#used for sending GET requests to the server where the website resides.
#This will allow us to locally save the HTML code of the webpage on our own machine.



url = 'http://www.geeksforgeeks.org/'
htmlCode = urllib2.urlopen(url).read() # the HTML code of the webpage, 
htmlParsed = BeautifulSoup(htmlCode, 'html.parser') #parse the HTML code ,BeautifulSoup function
#print(soup)

links = []

for anchors in htmlParsed.find_all('a'):
	links.append(anchors.get('href')) #it will fetch all the URLs from their respective tags, BeautifulSoup function

for link in links:
	print link
