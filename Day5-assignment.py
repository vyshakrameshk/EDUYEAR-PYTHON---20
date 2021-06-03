# print("om namah shivaya !")
# print("Hello World !")

# Assignment for For Loops

# 1. From range n to m, print all the numbers divisible by 5 and 7 both

# start , end = int( input("Input starting number of the range:") ) , int( input("Input ending number of the range:") )
# for i in range (start , end+1):
# 	if (i%5==0) and (i%7==0):
# 		print(i)
# 	else:
# 		continue

# 2. Find the sum of the series 2 +22 + 222 + 2222 + .. n terms
# Given:

# number_of_terms = 5

# So series will become 2 + 22 + 222 + 2222 + 22222

# Expected output:

# 24690

# Hint: 'a'*2 = 'aa'


# terms=int(input("Enter the number of terms to add the number 2 to itself: "))
# sum_terms=0
# two='2'

# for i in range ( 1, terms+1):
# 	print("Value in {} Iteration : {} ".format( i,two*i ) )
# 	sum_terms = sum_terms + int(two*i)
# 	print("Sum in {} Iteration : {} ".format( i,sum_terms ) )

# print("Total sum = " , sum_terms)




# Assignment for While Loops

# 3. Take integer inputs from user until he/she presses q ( Ask to press q to quit after every integer input ). Print the sum of all numbers. (Use while loop)

# sum_nums = 0

# while True:
# 	ip_var = input("Enter an Integer value to add continuosly. Press q to exit")

# 	if ip_var == 'q':
# 		break
# 	elif ip_var.isdigit():
# 		sum_nums = sum_nums + int(ip_var)
# 	else:
# 		print("Enter Integer OR q to quit. Nothing else !!!")
# 		continue	#not necessary

# print("Final sum is {}".format(sum_nums))

# print(dir(str))



# 4.  Write a loop to find the factorial of any number
# The factorial (symbol: !) means to multiply all whole numbers from our chosen number down to 1.

# For example: calculate the factorial of 5

# 5! = 5 × 4 × 3 × 2 × 1 = 120
# Expected output:

# 120

# facto = int(input("Enter the number to find factorial:"))
# print(dir(facto))

# num = int(input("Enter the number to find factorial:"))

# factorial = 1

# # check if the number is negative, positive or zero
# if num < 0:
#    print("Sorry, factorial does not exist for negative numbers")
# elif num == 0:
#    print("The factorial of 0 is 1")
# else:
#    for i in range(1,num + 1):
#        factorial = factorial*i
#    print("The factorial of",num,"is",factorial)

# 5. input: python language is best programming language
# output: P-y-T-h-O-n l-A-n-G-u-A-g-E I-s b-E-s-T P-r-O-g-R-a-M-m-I-n-G L-a-N-g-U-a-G-e

# str_ip= "python language is best programming language"
# print(str_ip)

# str_ip=list(str_ip)
# print(str_ip,"\n")

# length=len(str_ip)
# print(length,"\n")

# for i in range (0,length):
# 	if i%2==0:
# 		str_ip[i]=str_ip[i].swapcase()
# 	else:
# 		continue

# print(str_ip,end="\n")

# str_ip = "-".join(str_ip)
# print(str_ip)
# print(type(str_ip))

# str_ip = str_ip.replace("- -"," ")
# print(str_ip)

# print(dir(str_ip))

print( type('50000.5'))