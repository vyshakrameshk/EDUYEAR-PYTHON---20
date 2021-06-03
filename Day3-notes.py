# To get the binary code of any values: bin(10)

''' OPERATORS '''
# Arithmetic Operators
# +, -, *, /, %, // - floor/integer division, ** - Exponentiation
a, b = 5, 2
print("a + b = {}".format(a + b))
print("a - b = {}".format(a - b))
print("a * b = {}".format(a * b))
print("a / b = {}".format(a / b))
print("a % b = {}".format(a % b))
print("a // b = {}".format(a // b))
print("a ** b = {}".format(a ** b))

# Comparison operators
# >, >=, <, <=, ==, !=
a, b = 20, 15
print("a < b : {}".format(a < b))
print("a > b : {}".format(a > b))
print("a <= b : {}".format(a <= b))
print("a >= b : {}".format(a >= b))
print("a = b : {}".format(a == b))
print("a != b : {}".format(a != b))

# Logical operators
# and, or, not

# not -- 
# T -- F
# F -- T

# or -- 
# T T -- T
# T F -- T
# F T -- T
# F F -- F

# and -- 
# T T -- T
# T F -- F
# F T -- F
# F F -- F

a, b = True, False
print("a and b : {}".format(a and b))
print("a and b : {}".format(a or b))
print("Negation of a : {}".format(not a))
print("Negation of b : {}".format(not b))

print("" and "py")
print("py" and "python")

print("" or "py")
print("py" or "python")

# and == 
# if 1st value True --> 2nd value
# if 1st value False --> 1st value

# or == 
# if 1st value True --> 1st value
# if 1st value False --> 2nd value

# Bitwise operators
# &, |, ~, ^, >>, <<
a, b = 2, 4
print("a & b : {}".format(a & b))
print("a | b : {}".format(a | b))
print("~a : {}".format(~a))
print("a ^ b : {}".format(a ^ b))
print("a >> 2 : {}".format(a >> 2))
print("a << 2 : {}".format(a << 2))

# Assignment operators
# +=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, >>=, <<=
num = 10
num += 5	# num = num + 5
print(num)


# Identity operators
# is , is not
a, b = 10, 20
print("a is b : {}".format(a is b))
print("a is not b : {}".format(a is not b))

# Membership operators
# in, not in
city = "hyderabad"
print("y in hyderabad : {}".format('y' in city))
print("y not in hyderabad : {}".format('y' not in city))

####################################################################################
