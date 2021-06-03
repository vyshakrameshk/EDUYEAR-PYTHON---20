# print("om namah shivaya !")
# print("Hello World !")

#printing ascii value. expects a string of length 1
# a=10
# print(ord(a)) ->error

# print(ord(A))   ->error
# ascii_val="A"
# print(ascii_val)
# print(ord(ascii_val))

# printing ascii character of a int number
# print(chr(122))

# printing binary values of int . cannot convert float to binary
# a=12
# b=2
# c=-2
# d=2.02
# print( a, b, c, d )
# print( bin(a), bin(b), bin(c) )

# converting binary to int, hexadecimal and octal
# a=0b0101011   -->interpreter cant identify the datatype. so feed it as string
# a='0b0101011'
# # b=int(a) #->error. by default int is base 10
# print( int(a,base=2) )  #OR
# print( int(a,2) )

# # print( int(a,base=8) )  -->error coz b is not identified by octal
# # print( int(a,base=10) )	-->error coz b is not identified by octal
# print( int(a,base=16) )	#-->since hexadecimal is from 0-9 + a to f, it recognises b
# #OR
# print( int(a,16) )

#using user input. It takes all input as in str datatype
#taking user input and giving an OP
# name=input("Hey! Enter your name: ")
# age =input("Enter your age")
# print("Datatype of name: {}, Datatype of age: {}".format(type(name), type(age)) )
# print("Adding 5 years to your age..!!!")
# # age += 5	-->cannot add age ie., string to 5 ie., int
# age=int(age)+5
# print("Name:{} Age:{}".format(name,age))

# using operators on string
# arithmatic operator
# a="vyshak"
# b=" ramesh k"
# print(a+b)	#only + arithmatic operator can be used on string
# print(a-b) ->error
# print(a*b)	->error
# print(a/b)	->error

# Comparison operators
# print(a==b)
# print(a<b)
# print(a>b)
# print(a>=b)
# print(a<=b)
# print(a!=b)

# Logical Operators - and, or, not -takes only bool datatype to give bool datatype.
# If string is taken asa operand, then prints operands depending on the operator

# and == 
# if 1st value True --> 2nd value
# if 1st value False --> 1st value

# or == 
# if 1st value True --> 1st value
# if 1st value False --> 2nd value


# print(a and b)	#-->ramesh k
# a=""
# print(a and b)	#-->EMPTY.NO OP
# b=""
# print(a and b)	#-->EMPTY.NO OP


# a="vyshak"
# b=" ramesh k"

# # z = a or b
# # print(z)

# print(a or b)	#-->vyshak
# a=""
# print(a or b)	#-->ramesh k

# a="vyshak"
# b=" ramesh k"
# print(a or b)	#-->vyshak
# a, b="",""
# print(a or b)	#-->EMPTY.NO OP

# print(not("")	->True
# print(not("Vyshak")	->False


# Membership operator - in, not in

# a="Hello"
# print('e' in a)	#-->True
# print('ello' in a)	#-->True

# Identity Operators - is, is not
# is operator is same as == with primitive datatypes
# is not operator is same as != with primitive datatypes
#both is , is not works different with list 

# a,b=10,20
# print(a==b)	 #->False
# print(a is b)	#->False

# print(a!=b)	 #->True
# print(a is not b)	#->True

# print(not(a is not b))	#->False

# Logical Operators (==,!=,<,>,<=,>=) compare the values
# Identity Operators compare address
# a=10
# b=10
# print(id(a),"\n",id(b))

# print(a==b)	 #->True
# print(a is b)	#->True

# print(a!=b)	 #->False
# print(a is not b)	#->False

# a=[1,2,3]
# b=[1,2,3]	#b is not assigned with same address as a in lists

# print(id(a),"\n",id(b))
# print(a==b)	 #->True
# print(a is b)	#->False

# print(a!=b)	 #->False
# print(a is not b)	#->True



#Bitwise Operator &,|,~,>>,<<