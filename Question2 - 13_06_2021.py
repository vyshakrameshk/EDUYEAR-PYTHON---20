# Write a Python program that accepts a string and calculate the
# number of digits and letters.
# Sample Data : Python 3.9
# Expected Output :
# Letters 6
# Digits 2


# print(dir(str))
string = input("Enter a String:\n")
digit_count = 0
letter_count = 0
other_conut = 0

for i in string:
	if i.isalpha()==True:
		letter_count+=1
	elif i.isdigit()==True:
		digit_count+=1
	else:
		other_conut+=1

print("\nLetters: {}\nDigits: {}\nOthers: {}".format(letter_count,digit_count,other_conut) )
