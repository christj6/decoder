# coding: utf-8
import unicodedata
import string

# run in cygwin with: python hello.py

# this function takes in a string and two different letters.
# It returns a string where any instance of letter a is replaced with letter b
# and vice versa. For example: letterSwap("lemonade", 'e', 'l') = elmonadl
"""
testing = "lemonade"
testing = letterSwap(testing, 'e', 'l')
print(testing)
"""
def letterSwap (string, a, b):
	letters = list(string)
	newList = ("")
	for x in letters:
		if x == a:
			newList += b
		elif x == b:
			newList += a
		else:
			newList += x
	return newList

# uses text file from http://www.sil.org/linguistics/wordlists/english/wordlist/wordsEn.txt
# to build dictionary of english words
with open("wordsEn.txt") as word_file:
    dictionary = set(word.strip().lower() for word in word_file)

def isWord (word):
	return word.lower() in dictionary


encodedMessage = "VH ONE WMEYO YNTX GVBXIK SVWC KYY ONEM CXKMW KBP SVWC XBNEDC UKRRVNB, ONE GKB'W CXYU AEW IKZX K DNNP INTVX"
encodedAuthor = "LEXBWVB WKMKBWVBN"

encodedMessage = encodedMessage.lower()
encodedAuthor = encodedAuthor.lower()

print(encodedMessage + " -- " + encodedAuthor)

words = encodedMessage.split() + encodedAuthor.split()

characters = list("")

for x in words:
	characters += list(x)

# filter out characters we're not interested in
characters = [x for x in characters if x != '\'']
characters = [x for x in characters if x != ',']
characters = [x for x in characters if x != '.']
characters = [x for x in characters if x != '\"']
characters = [x for x in characters if x != '(']
characters = [x for x in characters if x != ')']
characters = [x for x in characters if x != '-']

totalLetters = len(characters) # pool size used as the denominator

# using: http://en.wikipedia.org/wiki/Letter_frequency#Relative_frequencies_of_letters_in_the_English_language
# e - 12.702 %
# t - 9.056 %
# a - 8.167 %
# o - 7.507 %
# i	- 6.966 %	 
# n	- 6.749 %	 
# s	- 6.327 %	 
# h	- 6.094 %	 
# r	- 5.987 %	 
# d	- 4.253 %	 
# l	- 4.025 %	 
# c	- 2.782 %	 
# u	- 2.758 %	 
# m	- 2.406 %	 
# w	- 2.360 %	 
# f	- 2.228 %	
# g	- 2.015 %	 
# y	- 1.974 %	 
# p	- 1.929 %	 
# b	- 1.492 %	 
# v	- 0.978 %	 
# k	- 0.772 %	 
# j	- 0.153 %	 
# x	- 0.150 %	 
# q	- 0.095 %	 
# z	- 0.074 %
#
# so the relative frequency of letters goes:
# E, T, A, O, I, N, S, H, R, D, L, C, U, M, W, F, G, Y, P, B, V, K, J, X, Q, Z

# common letters that are by themselves:
# a, i
# common two-letter words:
# to, i'm, of, me, in, my, ...

relativeFreq = ['e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l', 'c', 'u', 'm', 'w', 'f', 'g', 'y', 'p', 'b', 'v', 'k', 'j', 'x', 'q', 'z']

tupleList = [] # create tuple where first is letter, second is the # of times that letter appears in the message

for x in set(characters):
	tupleList.append((x, characters.count(x)))

leaderboard = reversed(sorted(tupleList, key = lambda tup: tup[1]))

# plan is to put lines 108-126 in some kind of loop, iterating through letter swaps until the optimal translation is found
# copy into new strings to hold onto original message
messageCopy = encodedMessage
authorCopy = encodedAuthor

# attempt to decode the message
i = 0
for x in leaderboard:
	letter = x[0]
	messageCopy = letterSwap(messageCopy, x[0], relativeFreq[i])
	authorCopy = letterSwap(authorCopy, x[0], relativeFreq[i])
	#print (x[0] + " swapped with " + relativeFreq[i])
	i += 1

# tally up the number of actual words
actualWords = 0

for word in messageCopy.split():
	if isWord(word.lower()):
		actualWords += 1

# display final message
print(messageCopy + " -- " + authorCopy)

# how close were we?
print(str(actualWords) + " actual words.")
