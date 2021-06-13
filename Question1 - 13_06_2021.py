# Write a Python program to map two lists into a dictionary.
# L1 = [1,2,3,4]
# L2 = ['a', 'b' , 'c', 'd']
# Output should be :- {1: ‘a’ , 2: ‘b’, 3: ‘c’, 4: ‘d’}

L1 = []
L2 = []
count = int( input("Enter the number of elements for 2 lists:\n ") )

print("\nInput the elements of List 1 (Int only):\n")
for i in range(count):
	ele = int ( input("Enter the {} Element: ".format(i+1)) )
	L1.append(ele)

print("\nInput the elements of List 2:\n")
for i in range(count):
	ele = input("Enter the {} Element: ".format(i+1))
	L2.append(ele)

print( "List 1: {} \nList 2: {}".format(L1,L2) )

print("\nMethod 1:\n")
D1 = { L1[i]:L2[i] for i in range(len(L1)) }
print(D1)

print("\nMethod 2: Using Dictionary zipping:\n")
D2 = dict(zip(L1,L2))
print(D2)

print("\nMethod 3: Using map and lambda functions:\n")
D3 = list( map( lambda x,y : {x:y} ,L1,L2 ) )
print(D3)

print("\nMethod 4:")
D4 = {}
for key in L1:
	for ele in L2:
		D4[key] = ele
		L2.remove(ele)
		break
print(D4)