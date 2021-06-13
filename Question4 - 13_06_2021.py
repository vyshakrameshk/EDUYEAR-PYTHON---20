# Write a Python program to construct the following pattern, using a
# nested loop number.
# INPUT - 5
# Expected Output:
# 1
# 22
# 333
# 4444
# 55555


num = int(input("Enter the number for which you want to see the pattern:\n"))

print("\nNormal way:")
for i in range(1 ,num+1):
	print(str(i)*i)

print("\nUsing Nested loop")
for i in range(1 ,num+1):
	string = ""
	for j in range(1,i+1):
		string = string+str(i)
	print(string)


