# Variables,DataTypes and Type conversions

# print("om namah shivaya !")
# print("Hello World !")

# print options
# name='vyshak'
# age=27
# print(name,age)
# print(name,age,end="@@@@") 
# print(name,age,sep="")
# print('Age:',age,'Name:',name)
# print('Age:{} Name:{}'.format(age,name))
# print(f'Age:{age} Name:{name}')
# stmt1=f'Age:{age} Name:{name}'
# stmt2='Age:{} Name:{}'.format(age,name)
# stmt3='Age:',age,'Name:',name
# print(stmt1)
# print(stmt2)
# print(stmt3)

#assigning texts to a value. 
# Note the triple quotes act as commenting if you have to comment multiple lines. 
# When it is assigned to a variable, we can print the information inside the triple quotes as it is

# value = """ My name is vyshak
# I live in bangalore
# I am from Coorg
# you can contact me on vyshakrameshk@gmail.com"""
# print(value)


# assigning values to variables
a=10
b=20.1
c='string'
d=True

# Printing the values of the variables

# print('The value of a is {}'.format(a))
# print('The value of a is {}'.format(b))
# print('The value of a is {}'.format(c))
# print('The value of a is {}'.format(d))

# Printing the type of the variables
# print('The type of a is {}'.format(type(a)))
# print('The type of b is {}'.format(type(b)))
# print('The type of c is {}'.format(type(c)))
# print('The type of d is {}'.format(type(d)))

#printing id ie., address; OP gives us integer value after converting hexadecimal value to int value. different everytime
# print("a value is:{}".format(a))
# print('address of a {}'.format(id(a)))
# y=a
# print("y value is:{}".format(y))
# print('address of a {}'.format(id(y)))
# z=10
# print("z value is:{}".format(z))
# print('address of z {}'.format(id(z)))
# print(id(5+5))
#id ie., address of a,y and z will be same.

# type conversion of individual variables

print("\nOriginal value of a is: {}".format(a))
print("Original value of b is: {}".format(b))
print("Original value of c is: {}".format(c))
print("Original value of d is: {}".format(d))

#converting everything into int
print("\nInteger conversion of a,b,c,d")
new_var=int(a)
print(new_var)
new_var=int(b)
print(new_var)
# new_var=int(c)	-->error
# print(new_var)
print("Integer conversion of String is not possible")
new_var=int(d)
print(new_var)		
#gives 1

#converting everything into float
print("\nFloat conversion of a,b,c,d")
new_var=float(a)
print(new_var)
new_var=float(b)
print(new_var)
# new_var=float(c) 
# print(new_var)    -->error
print("Float conversion of String is not possible")
new_var=float(d)
print(new_var)
#gives 1.0

# converting everything into string. No error
print("\nString conversion of a,b,c,d")
new_var=str(a)
print(new_var)
new_var=str(b)
print(new_var)
new_var=str(c) 
print(new_var)
new_var=str(d)
print(new_var)

# converting everything into bool. everything gives True
print("\nBool conversion of a,b,c,d")
new_var=bool(a)
print(new_var)
new_var=bool(b)
print(new_var)
new_var=bool(c) 
print(new_var)
new_var=bool(d)
print(new_var)

print(bool(0))
print(bool(1))
print(bool(-1))
# print(bool(xyz))
print(bool("xyz"))


new_str="1.20"
# print(int(new_str)) --> cannot convert it into int coz int doesn't understand "."
print(float(new_str))
print(str(new_str))
print(bool(new_str))

new_str="1"
print(int(new_str))
print(float(new_str))
print(str(new_str))
print(bool(new_str))