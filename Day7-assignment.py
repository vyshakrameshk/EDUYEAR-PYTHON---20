# print("om namah shivaya !")
# print("Hello World !")

# Day 7:

# 1. Give all the index values of vowels.

# Eg. "abed" 
# >> 0 2

# vowel_string = input("enter any string!!!")

# vowel_string = vowel_string.lower()
# num=0

# for i in range (0,len(vowel_string) ):
# 	if ( (vowel_string[i]=='a') or (vowel_string[i]=='e') or (vowel_string[i]=='i') or (vowel_string[i]=='o') or (vowel_string[i]=='u') ):
# 		num += 1
# 		print("Index value of the {} vowel is {}".format( num , i ) )


# 2.
# Reverse the words of a string

# Input... hello world happy birthday
# Output... birthday happy world hello


# og_strng = input("Enter a string to be reversed!!!\n")
# # print(og_strng)
# print(type(og_strng))

# # og_strng = list(og_strng)
# # print(type(og_strng))
# # print(og_strng)

# og_strng = og_strng.split(" ")
# print(og_strng)
# print(type(og_strng))

# og_strng.reverse()
# print(og_strng)
# print(type(og_strng))

# # og_strng=str(og_strng)
# # print(og_strng)
# # print(type(og_strng))

# og_strng = " ".join(og_strng)
# print(og_strng)
# print(type(og_strng))


# # print(og_strng.reverse())  -->this will give None

# # print(og_strng[::-1])  #reverses back to Original string



# 3. Remove duplicate elemnts without using set()
# Ex. 
# [1,2,3,3,2,4]
# >> [1,2,3,4]

print("Taking input as a list")
# Creating an empty list
og_list = []

nums=int(input("Enter the number of elements: "))

for i in range ( 0, nums):
	ele = input("enter the {} element : ".format(i) )
	og_list.append(ele)
	# og_list.insert(i,ele)

print(og_list)

## og_list = list(set(og_list))
## print(og_list)

print(dir(og_list))
create another empty list

final_list=[]

# for ele in og_list:
# 	if ele not in final_list:
# 		final_list.append(ele)

# OR 

[ final_list.append(ele) for ele in og_list if ele not in final_list ]

print(final_list)

print(dir(og_list))







