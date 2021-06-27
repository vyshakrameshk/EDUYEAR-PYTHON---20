# print("om namah shivaya !")
# print("Hello World !")

# convetional way
# class Int:
# 	def __init__(self,num):
# 		self.num = num
# 		print(self.num)

# 	def add(self, other):
# 		return self.num - other.num

# a=Int(50)
# b=Int(25)
# print("Adding andre subtraction:\n")
# print(a.add(b))

# By altering Dunder OR magic methods

class Int:
	def __init__(self,num):
		self.num = num
		print(self.num)

	def __add__(self, other):
		return self.num - other.num

	def __sub__(self,other):
		return self.num + self.num

a=Int(50)
b=Int(25)
print("Adding andre subtraction:\n")
print(a + b)  #same operator + can be used on obj because we are overriding dunder methods
a=Int(50)
b=Int(25)
print("subtraction andre Adding  :\n")
print(a-b)
# print(dir(int))