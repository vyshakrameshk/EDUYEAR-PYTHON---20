# print("om namah shivaya !")
# print("Hello World !")
# Day 6.


# Common part ->  Create a list of n numbers

num = int(input("What is the list size you want?"))
user_list = [ ]

# print(dir(user_list))

for i in range(num):
	user_list.insert( i , int( input("enter the {} element of the list:".format(i+1) ) ) )

print(user_list)

# Q1. Count even numbers and odd numbers

# even_count = 0
# odd_count = 0

# for i in range(num):
# 	if user_list[i] % 2 ==0:
# 		even_count += 1
# 	else:
# 		odd_count += 1

# print("Even count is {} \nOdd count is {}".format(even_count,odd_count))

# Q2. Tell max and min of the list ( without using any inbuilt function like max(),min())

# print("max:",max(user_list))

# print("min:",min(user_list))

max_ele=user_list[0]
min_ele=user_list[0]

# for i in range(num):
# 	if user_list[i] > max_ele:
# 		max_ele=user_list[i]
# 	else:
# 		pass  #cannot use continue as it will give control back to the for loop without executing below statements

# 	if user_list[i] < min_ele:
# 		min_ele=user_list[i]
# 	else:
# 		continue #you can use continue or pass here as there are no statements below

# OR

	# if user_list[i] > max_ele:
	# 	max_ele=user_list[i]
	# elif user_list[i] < min_ele:
	# 	min_ele=user_list[i]
	# else:
	# 	continue #you can use continue or pass here as there are no statements below

# print("max:",max_ele)

# print("min:",min_ele)



# Q3. Check whether the whole list is palindrome or not( eg. [1,2,1] gives yes for palindrome while [1,2,2] doesn't

# print(dir(user_list))
# print(len(user_list))

# rev_user_list = user_list.copy()

# rev_user_list.reverse()

# print(type(rev_user_list))
# print(rev_user_list)

# if rev_user_list==user_list:
# 	print("Palindrome!!!")
# else:
# 	print("Not a palindrome")

# OR

# rev_user_list = user_list[::-1]

# print(type(rev_user_list))
# print(rev_user_list)

# if rev_user_list==user_list:
# 	print("Palindrome!!!")
# else:
# 	print("Not a palindrome")


# Q4. Print the numbers which are palindrome inside the list
