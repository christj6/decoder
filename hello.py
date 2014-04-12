
# run in cygwin with: python hello.py

encodedMessage = "VH ONE WMEYO YNTX GVBXIK SVWC KYY ONEM CXKMW KBP SVWC XBNEDC UKRRVNB, ONE GKB'W CXYU AEW IKZX K DNNP INTVX"
encodedAuthor = "LEXBWVB WKMKBWVBN"
print(encodedMessage + " -- " + encodedAuthor)

words = encodedMessage.split() + encodedAuthor.split()

# print(words)

characters = list("")

for x in words:
	characters += list(x)

characters = [x for x in characters if x != '\'']
characters = [x for x in characters if x != ',']

print(sorted(characters))

totalLetters = len(characters)

# using: http://en.wikipedia.org/wiki/Letter_frequency#Relative_frequencies_of_letters_in_the_English_language
# e - 12.702 %
# t - 9.056 %
# a - 8.167 %
# o - 7.507 %

for x in set(characters):
	print(x + " occurs " + str(characters.count(x)) + " times.")
