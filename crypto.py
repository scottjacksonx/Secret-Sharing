"""
# Algorithm, Mark I #

- User inputs a length `n` they want their password to be and (optionally) how many words they want their password to be based on `l` (default is 3).
- Program chooses `l` random words from the dictionary, ensuring that at least one of them is of length `n`.
- Program "adds" the words together (mod 40). This gives us a secure password and the `l` words that generate it.

# Notes #

- Brute-Force Attack: Assuming the attacker knows `l - 1` words, they only have to test each word in the dictionary to crack the password (41238).
"""

import random



# Dictionary file from http://wordlist.sourceforge.net/

# Global Variables #

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '2', '3', '4', '5', '6', '7', '8', '9', '-', '&', '_', '.', '*', '#']	# '1' is left out for readability's sake (l and 1 can look very similar.)



# Basic Functions #

def compareLength(a, b):
	return cmp(len(a), len(b))	# compare lengths

def add(l1, l2):
	"""
	Adds two letters together and returns the resulting letter (mod 40).
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
	
	
def chooseWords(dictionaryFilename, length, numWords=3):
	"""
	Looks in a dictionary (text file) and chooses `numWords` random words of length `length`.
	"""
	dictionary = open(dictionaryFilename, "r")
	
	allWords = []
	for word in dictionary:
		allWords.append(word.rstrip("\n"))
	dictionary.close()
	
	randomWords = []
	random.seed()
	foundBigWord = False
	bigRandomWord = ""
	while not foundBigWord:
		bigRandomWord = allWords[random.randint(0, len(allWords))]
		if len(bigRandomWord) == length:
			foundBigWord = True
	randomWords.append(bigRandomWord)
	
	for i in range(0, numWords - 1):
		random.seed()
		appropriatelySizedWordFound = False
		randomWord = ""
		while not appropriatelySizedWordFound:
			randomWord = allWords[random.randint(0,len(allWords))]
			if len(randomWord) <= length:
					appropriatelySizedWordFound = True
		randomWords.append(randomWord)
		
	# Sort by length (descending)
	randomWords.sort(compareLength)
	randomWords.reverse()
		
	return randomWords

randomWords = chooseWords("dictionary.txt", 12)
print randomWords,
password = addWords(randomWords)

print "= " + password
	
	

			