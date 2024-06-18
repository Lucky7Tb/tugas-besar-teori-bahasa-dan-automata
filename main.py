import json

class PDA():
	stack = []

	def push(self, value):
		self.stack.insert(0, value)

	def pop(self):
		self.stack.pop(0)

	def top(self):
		return self.stack[0];	

def checkWordIs(word, dataset_key):
	with open("dataset.json") as dataset:
	    words_dataset = json.load(dataset)
	    for value in words_dataset[dataset_key]:
	    	if len(value) != len(word):
	    		continue 
	    	index = 0
	    	while True:
	    		if value[index] == word[index]:
	    			index += 1
	    			if index == len(value):
	    				return True
	    		else:
	    			break
	    return False

def checkWordType(pda, words):
	wordType = ''
	for word in words.split(' '):
		if checkWordIs(word.strip(), 'subject'):
			pda.pop()
			pda.push('S')
			wordType += 'S'
		elif checkWordIs(word.strip(), 'predicate'):
			pda.pop()
			pda.push('P')
			wordType += 'P'
		elif checkWordIs(word.strip(), 'object'):
			pda.pop()
			pda.push('O')
			wordType += 'O'
		elif checkWordIs(word.strip(), 'description'):
			if pda.top() == 'P' or pda.top() == 'O':
				pda.pop()
			pda.push('K')
			wordType += 'K'
		else:
			pda.push(' ')

	if (pda.top() == 'P' or pda.top() == 'O' or pda.top() == 'K'):
		pda.pop()

	return (pda.top() == '#', wordType)

def main():
	words = input("Masukan kalimat: ")
	words = words.lower()
	pda = PDA()
	pda.push("#")
	pda.push("$")

	(isCorrectWord, wordType) = checkWordType(pda, words)
	if isCorrectWord:
		print(f"Kalimat adalah kalimat {wordType}")
	else:
		print(f"Kalimat bukanlah kalimat: SPOK, SPK, SPO, SP")

main()