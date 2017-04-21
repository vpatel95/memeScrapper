from bs4 import BeautifulSoup
import requests, sys, os
from os.path import basename

BASE_URL = 'http://images.memes.com/meme/'

def getName():
	getDir()
	list = os.listdir(os.getcwd())
	if list:
		name =[]
		for l in list:
			name.append(int(os.path.splitext(l)[0]))
		return max(name)+1
	else:
		return 1
	
def getDir():
	os.getcwd()
	if(basename(os.getcwd()) == 'memes'):
		pass
	else:
		try:
			os.chdir('memes')
		except FileNotFoundError:
			os.mkdir('memes')
			os.chdir('memes')

def makeRequest(name):
	r = requests.get(BASE_URL + str(name))
	return r.content

def getMeme(data):
	name = str(getName())
	f = open(name + '.jpg', 'wb+')
	f.write(data)
	print(name + ' saved successfully')
	f.close()

def checkMeme(content):
	soup = BeautifulSoup(content, 'lxml')
	if(soup.title == None):
		getMeme(content)
	else:
		name = str(getName()) + '.jpg'
		content = makeRequest(name)
		checkMeme(content)

for i in range(3000):
	name = getName()
	content = makeRequest(name)
	checkMeme(content)

