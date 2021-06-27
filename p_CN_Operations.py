class ComplexNumber:
	def __init__(self, real, img):
		self.real = real
		self.img = img

	def addCN(self, other):
		self.real += other.real
		self.img += other.img

	def subCN(self, other):
		self.real -= other.real
		self.img -= other.img

	def mulCN(self):
		# (a + bj).(c + dj) == (ac-bd) + (ad+bc)j
		pass

	def divideCN(self):
		pass

	def inverseCN(self):
		pass

def show_menu():
	print("\n-.,__,.-'~'-.,__,.-'~'- Perform operations on Complex Numbers -.,__,.-'~'-.,__,.-'~'-")
	options = ['Add Complex Numbers', 'Substract Complex Numbers', 'Multilpy Complex Numbers', 'Divide Complex Numbers', 'Inverse a Complex Number']
	for ind, option in enumerate(options):
		print(f'{ind+1}. {option}')
	print('0. Exit')
	choice = int(input('Enter your option: '))
	if choice == 0:
		exit(0)
	elif choice == 1:
		# Addition
		complex_numbers = []
		n = int(input('Enter no. of Complex Numbers : '))
		print()
		for i in range(n):
			a = int(input('Enter complex number {} real number: '.format(i+1)))
			b = int(input('Enter complex number {} imaginary number: '.format(i+1)))
			obj = ComplexNumber(a, b)
			complex_numbers.append(obj)
			print()
		res = ComplexNumber(0,0)
		for cn in complex_numbers:
		    res.addCN(cn)

		print('\nAddition of the following complex numbers:')
		for cn in complex_numbers:
			print(f'\t{cn.real} + {cn.img}j')
		print(f'\nResult: {res.real} + {res.img}j')
	
	elif choice == 2:
		# Substraction
		a = int(input('\nEnter complex number 1 real number: '))
		b = int(input('Enter complex number 1 imaginary number: '))
		obj_1 = ComplexNumber(a, b)

		a = int(input('\nEnter complex number 2 real number: '))
		b = int(input('Enter complex number 2 imaginary number: '))
		obj_2 = ComplexNumber(a, b)

		print('\nSubtraction of the following complex numbers:')
		print(f'\t{obj_1.real} + {obj_1.img}j')
		print(f'\t{obj_2.real} + {obj_2.img}j')

		obj_1.subCN(obj_2)
		print(f'\nResult: {obj_1.real} + {obj_1.img}j')

	elif choice == 3:
		pass
	elif choice == 4:
		pass
	elif choice == 5:
		pass

while True:
	show_menu()