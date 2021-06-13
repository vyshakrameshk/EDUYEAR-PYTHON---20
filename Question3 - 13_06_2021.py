# Write a Python function that takes a list of words and returns the
# length of the longest one.
# Sample Output:
# Longest word: Exercises are the best
# Length of the longest word: Exercises 9


def longest_word(l1):

	longest_word = l1[0]

	for i in range(1, len(l1)):
		if len(l1[i]) > len(longest_word):
			longest_word=l1[i]

	return longest_word, len(longest_word)


string = input("Enter the sentence\n")
l1 = string.split()
print("\nThe sentence is split as follows:")
print(l1)

word,length = longest_word(l1)

print("\nLongest Word is : {}\nIts Length is: {} ".format(word,length))