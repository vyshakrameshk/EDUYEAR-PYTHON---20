# Check whether a number is russian prime or not.
# 379 is an example of a russian prime, since 379, 37, and 3 are all
# prime. Other example 73, since 73 , 7 all are prime
# Input: 379
# Expected output: Russian Prime

def isprime(num):
	prime = True
	if num==1 or num==0:
			print("\nEntered number is not Russian Prime")
			exit(0)

	for i in range(2,num):
		
		if num%i==0:
			prime = False
			break
		else:
			str_num = str(num)
			new_num = str_num[0:len(str_num)-1]

			if new_num == "":
				break
			else:
				new_num = int(new_num)
				isprime(new_num)
				break

	if prime == False:
		print("Not Russion Prime\n")
	else:
		print(f"{num} is Russian Prime:") 	


num = int(input("Enter the number to check whether it is russion prime or not:\n"))
isprime(num)