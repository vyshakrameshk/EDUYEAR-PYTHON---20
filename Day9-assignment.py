# print("om namah shivaya !")
# print("Hello World !")

# Day 9 :

# 1. Take a number from user and check whether it is prime or not. 
# Use parameters to send the number to function.

# Eg. Enter a number 3
#        3 is prime

# def prime_num( num ):

# 	if num>=2:
# 		for i in range(2,num):
# 			if num%i==0:
# 				print("Not Prime")
# 				return

# 		print("Prime Number")
# 		return

# 	elif num==0 or num==1:
# 		print("\nNot Prime")

# num=int( input("Enter a number:") )
# prime_num(num)


# OR


# def prime_num( num ):

# 	if num>2:
# 		for i in range(2,num):
# 			if num%i==0:
# 				print("Not Prime")
# 				return
# 		print("Prime Number")
# 		return

# 	elif num==2:
# 		print("Prime Number")
# 		return

# 	elif num==0 or num==1:
# 		print("\nNot Prime")

# num=int( input("Enter a number:") )
# prime_num(num)

# 2. Write a function to print n factorial. Take n value as user input and pass as a parameter
# Eg. Enter a number 5
#       120


def fact(num):
	if num==0:
		print("factorial of 0 is 1 ")
	elif num<0:
		print("No Factorial for negative numbers !")
	else:
		res=1
		for i in range(1,num+1):
			res=res*i
		print(f"Factorial of {num} is {res}")

num=int( input("Enter a number:") )
fact(num)


# # Factorial of a number using recursion

# def recur_factorial(n):
#    if n == 1:
#        return n
#    else:
#        return n*recur_factorial(n-1)

# num=int( input("Enter a number:") )

# # check if the number is negative
# if num < 0:
#    print("Sorry, factorial does not exist for negative numbers")
# elif num == 0:
#    print("The factorial of 0 is 1")
# else:
#    print("The factorial of", num, "is", recur_factorial(num))