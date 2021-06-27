# print("om namah shivaya !")
# print("Hello World !")

import numpy as np
# import numpy
# from numpy import *
# from numpy import arange

# print(type(np))  #class module

# import sys
# a = [1,2,3,4,5]
# print(sys.getsizeof(1) * 5) #140 -> 140/5=28 Bytes

# b = np.array([1,2,3,4,5])
# print(b.itemsize * b.size)  #20 ->20/5=4 Bytes per int = 32bits =int32 by default

# c = np.array([1,2,3,4,5], dtype='int64' )
# print(c.itemsize * c.size)  #40. similary we can mention int8, int16, int32(default)

# deciding the dtype
# if you want to store age in the array
# maximum age would be 120

# print( len( bin(120)[2:] ) )   #gives 7. so maximum of 8 bits is enough. so dtype='int8' can be used

# if you want to store age in the array
# maximum age would be 9999999999
# print( len( bin(9999999999)[2:] ) )   #gives 34. so maximum of 34 bits is enough. so dtype='int64' can be used

# a = np.array([[1,2,3],[4,5,6]])
# print(a)
# print(a.ndim)
# print(a.shape)


# a = np.random.rand(5,5)
# print(a)
# print(a.ndim)
# print(a.shape)

# a = np.random.randint(10,20, size=(5,6) )
# print(a)
# print(a.ndim)
# print(a.shape)

a = np.random.choice([1,2,3,4,5], size=(5,6) )
# print(a)
# print(a.ndim)
# print(a.shape)

# a = np.array([1,2,3,4,5])
b = np.vstack((a,a*2,a**2))
print(b)



