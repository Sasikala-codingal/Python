# function to check whether 
# first and last character of words match
#def match_words(w):
list=['abc', 'cfc','xyz', 'aba', '1221']
charac = 0
lst = []
for word in list:
	if len(word) > 1 and word[0] == word[-1]:
			charac += 1
			lst.append(word)
	
	print("List of words with first and last character same\n", lst)
	#return charac
#count = match_words(['abc', 'cfc','xyz', 'aba', '1221'])
print("Number of words having first and last character same:", charac)