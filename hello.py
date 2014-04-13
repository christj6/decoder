
# run in cygwin with: python hello.py

encodedMessage = "VH ONE WMEYO YNTX GVBXIK SVWC KYY ONEM CXKMW KBP SVWC XBNEDC UKRRVNB, ONE GKB'W CXYU AEW IKZX K DNNP INTVX"
encodedAuthor = "LEXBWVB WKMKBWVBN"
print(encodedMessage + " -- " + encodedAuthor)

words = encodedMessage.split() + encodedAuthor.split()

characters = list("")

for x in words:
	characters += list(x)

characters = [x for x in characters if x != '\'']
characters = [x for x in characters if x != ',']

totalLetters = len(characters)

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

tupleList = []

for x in set(characters):
	tupleList.append((x, characters.count(x)))

leaderboard = reversed(sorted(tupleList, key = lambda tup: tup[1]))

for x in leaderboard:
	letter = x[0]
	occurrences = x[1]
	print (letter + " occurs " + str(x[1]) + " times.")
