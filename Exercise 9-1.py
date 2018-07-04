"The file to be checked is here--https://www.py4e.com/code3/words.txt"


inp=open('words')
words = dict()
ftext = inp.read()
wordlist = ftext.split()
for word in wordlist:
	words[word] = 0
while True:
	check = raw_input('Enter word: ')
	if check == 'I am done' : break
	else:
		print check in words
