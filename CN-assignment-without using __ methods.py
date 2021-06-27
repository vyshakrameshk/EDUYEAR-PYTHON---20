class ComplexNumber:
	def __init__(self, real, img):
		self.real = real
		self.img = img

	def add_cn(self,c_num):
		self.real = self.real+c_num.real
		self.img = self.img+c_num.img

	def sub_cn(self,c_num,first_iteration):
		if first_iteration==1:
			self.real=c_num.real
			self.img=c_num.img
		else:
			self.real = self.real-c_num.real
			self.img = self.img-c_num.img

	def mul_cn(self,c_num):
			# self.real=c_num.real
			# self.img=c_num.img
			# self.real = (self.real*c_num.real) - (self.img*c_num.img) 
			# self.img = (self.real*c_num.img) + (self.img*c_num.real)
			res = c_num[0]
			for i in range(1, len(c_num)):
				res = res * c_num[i]

			return res

	def div_cn(self,c_num):
		res = c_num[0]
		for i in range(1, len(c_num)):
			res = res / c_num[i]

		return res

def operate(choice,num_of_cn):
	complex_numbers = []

	if choice ==1:
		for i in range(num_of_cn):
			real = int(input("Enter the Real part of {} Complex number below\n".format(i+1)))
			img = int(input("Enter the Imaginary part of {} Complex number below\n".format(i+1)))
			print(f"Entered Number is:{real} + {img}i")
			c_num = ComplexNumber(real,img)
			complex_numbers.append(c_num)

		obj = ComplexNumber(0,0)
		for i in range(len(complex_numbers)):
			obj.add_cn(complex_numbers[i])

		print( f"Added number is {obj.real} + {obj.img}i" )

	elif choice==2:
		for i in range(num_of_cn):
			real = int(input("Enter the Real part of {} Complex number below\n".format(i+1)))
			img = int(input("Enter the Imaginary part of {} Complex number below\n".format(i+1)))
			print(f"Entered Number is:{real} + {img}i")
			c_num = ComplexNumber(real,img)
			complex_numbers.append(c_num)

		obj = ComplexNumber(0,0)
		first_iteration=1	#to avoid going to negative numbers.

		for i in range(len(complex_numbers)):
			obj.sub_cn(complex_numbers[i],first_iteration)
			first_iteration+=1

		print( f"Subtracted number is {obj.real} + {obj.img}i" )

	elif choice==3:
		c_num = []
		for i in range(num_of_cn):
			real = int(input("Enter the Real part of {} Complex number below\n".format(i+1)))
			img = int(input("Enter the Imaginary part of {} Complex number below\n".format(i+1)))
			print(f"Entered Number is:{real} + {img}i")
			converted_cn = complex(real,img)
			c_num.append(converted_cn)


		obj = ComplexNumber(0,0)
		res = obj.mul_cn(c_num)

		print( f"Multiplied number is {res}" )	
		
	elif choice==4:
		c_num = []
		for i in range(num_of_cn):
			real = int(input("Enter the Real part of {} Complex number below\n".format(i+1)))
			img = int(input("Enter the Imaginary part of {} Complex number below\n".format(i+1)))
			print(f"Entered Number is:{real} + {img}i")
			converted_cn = complex(real,img)
			c_num.append(converted_cn)


		obj = ComplexNumber(0,0)
		res = obj.div_cn(c_num)

		print( f"Divided number is {res}" )
		

	elif choice==0:
		exit(0)

	else:
		main()
		


def main():
	print("Welcome to the world of Complex Numbers!!! \n")
	operations = ["Addition","Subtraction","Multiplication","Division"]
	print("Choose from below options")
	for i, operation in enumerate(operations,1):
		print(f' {i}. {operation} ')

	print(" 0. Exit\n")

	choice = int(input("What is your choice?"))

	num_of_cn = int(input("Enter the number of Complex Numbers you want to operate on:"))
	operate(choice,num_of_cn)

main()