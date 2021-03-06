# Usage:
# crypto.py [-l length] [-n numWords] [-w baseWord]

import random
import sys

# Original dictionary file from http://wordlist.sourceforge.net/
# Dictionary file has been modified slightly (words containing "I" and "O" have been removed, and newline characters have been changed from DOS-style to Unix-style.

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '2', '3', '4', '5', '6', '7', '8', '9', '-', '&', '_', '.', '*', '#', '\'']	# '1' is left out for readability's sake ('l' and '1' can look very similar.)


# Basic Functions #

def compareLength(a, b):
	return cmp(len(a), len(b))	# compare lengths

def add(l1, l2):
	"""
	Adds two letters together and returns the resulting letter (mod len(alphabet)).
	"""
	return alphabet[(alphabet.index(l1) + alphabet.index(l2)) % len(alphabet)]
	
def addWords(words):
	"""
	Adds words in a list together letter-wise and returns the resulting string.
	"""
	result = list(words[0])
	words.remove(words[0])

	for word in words:
		for i in range(0, len(word)):
			result[i] = add(result[i], word[i])
	sumWord = ""
	for n in result:
		sumWord += n
	return sumWord
	
	
def chooseWords(dictionaryFilename, length, numWords=3, baseWord=""):
	"""
	Looks in a dictionary (text file) and chooses `numWords` random words, two of which are length `length` and the rest of length <= `length`.
	"""
	dictionary = open(dictionaryFilename, "r")
	
	allWords = []
	for word in dictionary:
		allWords.append(word.rstrip("\n"))
	dictionary.close()
	
	randomWords = []
	random.seed()
	alreadyAdded = 2
	
	if baseWord is not "":
		randomWords.append(baseWord)
		alreadyAdded = 3
		
	
	# Get two random words of length `length`.
	for i in range(0,2):
		foundBigWord = False
		bigRandomWord = ""
		while not foundBigWord:
			bigRandomWord = allWords[random.randint(0, len(allWords)-1)]
			if len(bigRandomWord) == length:
				foundBigWord = True
		randomWords.append(bigRandomWord)
	
	
	
	
	for i in range(0, numWords - alreadyAdded):
		random.seed()
		appropriatelySizedWordFound = False
		randomWord = ""
		while not appropriatelySizedWordFound:
			randomWord = allWords[random.randint(0,len(allWords)-1)]
			if len(randomWord) <= length:
					appropriatelySizedWordFound = True
		randomWords.append(randomWord)
		
	# Sort by length (descending)
	randomWords.sort(compareLength)
	randomWords.reverse()
		
	return randomWords

numWords = 3
length = 10
baseWord = ""


if len(sys.argv) > 2:
	if len(sys.argv) == 3:
		if sys.argv[1] == "-l":
			length = int(sys.argv[2])
		elif sys.argv[1] == "-n":
			numWords = int(sys.argv[2])
		elif sys.argv[1] == "-w":
			baseWord = str(sys.argv[2])
	elif len(sys.argv) == 5:
		# first arg
		if sys.argv[1] == "-l":
			length = int(sys.argv[2])
		elif sys.argv[1] == "-n":
			numWords = int(sys.argv[2])
			
		# second arg
		if sys.argv[3] == "-n":
			numWords = int(sys.argv[4])
		elif sys.argv[3] == "-w":
			baseWord = str(sys.argv[4])
	elif len(sys.argv) == 7:
		length = int(sys.argv[2])
		numWords = int(sys.argv[4])
		baseWord = str(sys.argv[6])

randomWords = chooseWords("dictionary.txt", length, numWords, baseWord)
print randomWords,
password = addWords(randomWords)
print "= " + password










	
	

			