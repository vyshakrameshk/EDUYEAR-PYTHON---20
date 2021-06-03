# print("om namah shivaya !")
# print("Hello World !")

# Day 8:


# all_courses = ['Python', 'Java', 'Machine Learning', 'Big data', 'C programming', 'Oracle SQL', 'Power Bi', 'Go lang', 'C++ Graphics', 'React JS', 'Ruby Rails', 'Flask', 'HTML & CSS', 'Salesforce', 'Javascript', 'Django']

# Take user input:
#   - name, email

# Create user dictionary with the keys:
#   - name, email, courses
#   user = {
#     'name': 'Harsh',
#     'email': 'harsh@gmail.com',
#     'courses': []
#   }

# Show menu
#   1. All courses
#     -- show all courses
#     -- user will select one course
#     -- add the selected course to user profile
#   2. My courses
#     -- show enrolled courses
#   3. Edit courses
#     -- delete the already added user courses
#   4. Show profile
#     -- display name and email of user
#   0. Exit

# while True:
#   print -- show the menu
#   choice = input('Enter your choice : ')
#   if choice == 0:
#     exit(1)
#   elif choice == 1:
#     show all courses
#   elif choice == 2:
#     show enrolled courses
#   elif choice == 3:
#     Edit user courses    
#   elif choice == 4:
#     Display user profile


print("\n\nHi Patron!!! Enter your information as requested:\n")
name_ip = input("Enter your name:")
email_ip = input("Enter your email:")

courses_off = ['Python', 'Java', 'Machine Learning', 'Big data', 'C programming', 'Oracle SQL', 'Power Bi', 'Go lang', 'C++ Graphics', 'React JS', 'Ruby Rails', 'Flask', 'HTML & CSS', 'Salesforce', 'Javascript', 'Django']

courses_off_len=len(courses_off)
user_info = {

'name':name_ip ,
'email':email_ip ,
'courses': []	
}

# print(user_info)
# print(dir(user_info))

while True:
	print("\n\n----------!! Menu !!----------")
	print("1. List of all courses offered by us:")
	print("2. List of courses you have enrolled to:")
	print("3. Edit the courses you enrolled:")
	print("4. Show your profile:")
	print("5. Type 0 to exit the menu:\n\n")
	choice=int(input("Enter your choice:"))

	if choice==1:

		print("\nList of all courses offered by us:\n")

		for ele in range(courses_off_len):
			print( (ele+1) , "-->", courses_off[ele])


		course_choice = int( input( "\nSelect a course to add: " ) )
		selected_course = courses_off[ course_choice-1 ]
		print(f"{selected_course} Added")
		user_info['courses'].append(selected_course)

		exit_choice = input("\n\\nDo you want to continue (Y / N)\n")
		if(exit_choice=='y' or exit_choice=='Y'):
			continue
		else:
			break
	
	elif choice==2:

		print("\nEnrolled courses are:")
		for ele in range ( len(user_info['courses']) ):
			print(ele+1, "-->",user_info['courses'][ele])

		exit_choice = input("\n\nDo you want to continue (Y / N)\n")
		if(exit_choice=='y' or exit_choice=='Y'):
			continue
		else:
			break	

	elif choice==3:

		print("\nYour Enrolled courses are:")
		for ele in range ( len(user_info['courses']) ):
			print(ele+1, "-->", user_info['courses'][ele])

		course_del = int(input( "Enter the course you want to delete :" ))
		user_info['courses'].pop(course_del-1)

		exit_choice = input("\n\nDo you want to continue (Y / N)\n")
		if(exit_choice=='y' or exit_choice=='Y'):
			continue
		else:
			break



	elif choice==4:
		print("\nThe profile is :\n")
		print("Your Name:",user_info['name'] )
		print("\nYour Email: ",user_info['email'] )
		print("\nYour Enrolled courses are:")
		for ele in range ( len(user_info['courses']) ):
			print(ele+1, "-->", user_info['courses'][ele])

		exit_choice = input("\n\nDo you want to continue (Y / N)\n")
		if(exit_choice=='y' or exit_choice=='Y'):
			continue
		else:
			break

	elif choice==0:
		break
	else:
		print("\nEnter a proper Input:")

		exit_choice = input("\n\nDo you want to continue (Y / N)\n")
		if(exit_choice=='y' or exit_choice=='Y'):
			continue
		else:
			break



