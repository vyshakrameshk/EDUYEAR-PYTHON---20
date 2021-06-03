# print("om namah shivaya !")
# print("Hello World !")

# Day 4:

# 1) use string functions to count the occurrence of 'y' in a word given by user.

# new_string=input("Enter a String, preferable with multiple occurences of 'y': ")
# print( new_string.count('y') )


# 2) take input of a string and print it's even indexed characters

# new_string=input("Enter a String: ")
# print("The string is: {}" , format(new_string) )
# for i in range ( 0 , len(new_string) ):
# 	if(i%2==0):
# 		print("The value of i is ", i , " - even index" )
# 		print(new_string[i])
# 	else:
# 		print("The value of i is ", i , "doesn't print any letter for odd index" )
	

# 3)create a program to swap case. Using string functions
# Input : EdUyEaR
# Output :.  eDuYeAr

# one way using swapcase
# str_var=input("Enter a string to swap cases")
# # print(dir(str_var))
# print(str_var.swapcase())
# print(str_var)	#didn't change the original string

# 2nd way using ascii value. But since strings are immutable, I have used List
# iterate on each item. If the ascii value is 65 to 90---add 32
# iterate on each item. If the ascii value is 97 to 122---subtract 32

# str_var=input("Enter a string to swap cases")
# str_len=len(str_var)

str_var=['A','b','C','d','@']
str_len=len(str_var)
print("Original string is : ", str_var)

for i in range (str_len):
	if ( ord( str_var[i] ) >= 65 ) and ( ord( str_var[i] ) <= 90 ):
		str_var[i] = chr ( ord(str_var[i]) + 32 )
	elif ( ord( str_var[i] ) >= 97 ) and ( ord( str_var[i] ) <= 122 ):
		str_var[i] = chr ( ord(str_var[i]) - 32 )
	else:
		str_var[i]=str_var[i]

print("Swapped string is : ", str_var)
