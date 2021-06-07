# print("om namah shivaya !")
# print("Hello World !")

# Global variables
user_cart = {}
user_wish = {}
user_name, user_age, user_city = "","",""

# Function to display entered user information
def disp_userinfo():
	print("\nName: {}".format(user_name))
	print("Age: {}".format(user_age))
	print("City: {}".format(user_city))
	disp_main_menu()	


# Function to display cart contents
def disp_cart():
	if len(user_cart)==0:
		print("Your cart is empty")
		disp_main_menu()

	else:
		num=1
		print("\nYour cart has following content:")
		for key, value in user_cart.items():
			print(num," ", key, value)
			num +=1
		disp_main_menu()


# Function to display wishlist contents
def disp_wishlist():
	if len(user_wish)==0:
		print("Your wishlist is empty")
		disp_main_menu()

	else:
		num=1
		print("\nYour wishlist has following content:")
		for key, value in user_wish.items():
			print(num," ", key, value)
			num +=1
		disp_main_menu()


# Function to Greet User
def disp_user_greet():
	global user_name
	global user_age
	global user_city
	user_name = input("Enter your name:")
	user_age = input("\nEnter your age:")
	user_city = input("\nEnter your city:")
	print(f"\nHi {user_name.upper()}. Welcome to Online Mart !!! Happy shopping !!!")


# Function to add specific items to the cart
def add_cart(selected_item):
	global user_cart
	new_dict = {}

	new_dict[selected_item[0]] = selected_item[1]	
	user_cart.update(new_dict)

	print("Your Cart is: ")
	print(user_cart)

	disp_categories()


# Function to add specific items to the wishlist
def add_wishlist(selected_item):
	global user_wish
	new_dict = {}

	new_dict[selected_item[0]] = selected_item[1]	
	user_wish.update(new_dict)

	print("\nYour Wishlist is: ")
	print(user_wish)

	disp_categories()


# Function to display Mobiles
def disp_mobiles():
	mobiles = { 'Apple' : 80000, 'Samsung' : 50000, 'Oneplus' : 40000, 'Xiomi' : 20000 }
	num=1

	for brand, price in mobiles.items():
		print(f"\n{num}. {brand} = {price}")
		num +=1

	choice = int(input("\nEnter your choice of mobile: Press 0 to go back to Previous Menu:\n"))

	if choice==0:
		disp_categories()

	else:
		selected_item = list(mobiles.items())
		# print(type(selected_item))
		# print(selected_item)
		selected_item = list(selected_item[choice-1])
		# print(type(selected_item))
		print(selected_item)

		print(f"The selected item is {selected_item[0]}, and it is of {selected_item[1]} value")

		option = int(input("\nPress 1 to add to the cart.\nPress 2 to add to the wishlist.\nPress any other key to go back to Previous Menu\n"))

		if option == 1:
			add_cart(selected_item)

		elif option ==2:
			add_wishlist(selected_item)

		else:
			disp_categories()


# Function to display Laptops
def disp_laptops():
	laptops = { 'Apple' : 120000, 'Acer' : 74000, 'HP' : 40000, 'Dell' : 50000 }
	num=1

	for brand, price in laptops.items():
		print(f"\n{num}. {brand} = {price}")
		num +=1

	choice = int(input("\nEnter your choice of laptop: Press 0 to go back to Previous Menu:\n"))

	if choice==0:
		disp_categories()

	else:
		selected_item = list(laptops.items())
		# print(type(selected_item))
		# print(selected_item)
		selected_item = list(selected_item[choice-1])
		# print(type(selected_item))
		print(selected_item)

		print(f"The selected item is {selected_item[0]}, and it is of {selected_item[1]} value")

		option = int(input("\nPress 1 to add to the cart.\nPress 2 to add to the wishlist.\nPress any other key to go back to Previous Menu\n"))

		if option == 1:
			add_cart(selected_item)

		elif option ==2:
			add_wishlist(selected_item)

		else:
			disp_categories()


# Function to display Watches
def disp_watches():
	watches = { 'Titan' : 5000, 'Casio' : 12000, 'Tommy' : 18000, 'TagHeuer' : 95000 }
	num=1

	for brand, price in watches.items():
		print(f"\n{num}. {brand} = {price}")
		num +=1

	choice = int(input("\nEnter your choice of watch: Press 0 to go back to Previous Menu:\n"))

	if choice==0:
		disp_categories()

	else:
		selected_item = list(watches.items())
		# print(type(selected_item))
		# print(selected_item)
		selected_item = list(selected_item[choice-1])
		# print(type(selected_item))
		print(selected_item)

		print(f"The selected item is {selected_item[0]}, and it is of {selected_item[1]} value")

		option = int(input("\nPress 1 to add to the cart.\nPress 2 to add to the wishlist.\nPress any other key to go back to Previous Menu\n"))

		if option == 1:
			add_cart(selected_item)

		elif option ==2:
			add_wishlist(selected_item)

		else:
			disp_categories()


# Function to display Books
def disp_books():
	books = { 'Polity' : 998, 'Comic' : 250, 'History' : 499, 'Economics' : 1299 }
	num=1

	for brand, price in books.items():
		print(f"\n{num}. {brand} = {price}")
		num +=1

	choice = int(input("\nEnter your choice of watch: Press 0 to go back to Previous Menu:\n"))

	if choice==0:
		disp_categories()

	else:
		selected_item = list(books.items())
		# print(type(selected_item))
		# print(selected_item)
		selected_item = list(selected_item[choice-1])
		# print(type(selected_item))
		print(selected_item)

		print(f"The selected item is {selected_item[0]}, and it is of {selected_item[1]} value")

		option = int(input("\nPress 1 to add to the cart.\nPress 2 to add to the wishlist.\nPress any other key to go back to Previous Menu\n"))

		if option == 1:
			add_cart(selected_item)

		elif option ==2:
			add_wishlist(selected_item)

		else:
			disp_categories()

# Function to display categories of Items
def disp_categories():
	categories = ['Mobiles', 'Laptops', 'Watches', 'Books', 'Main Menu']
	print("\n*** CATEGORIES ***\n")

	for i in range(len(categories)):
		print(f"{i+1}. {categories[i]}\n")	

	choice = int(input("Enter your choice:"))

	if choice == 1:
		disp_mobiles()

	elif choice == 2:
		disp_laptops()
	
	elif choice == 3:
		disp_watches()
		pass

	elif choice == 4:
		disp_books()
		pass

	elif choice == 5:
		disp_main_menu()

	else:
		print("\nInvalid choice. Enter again")
		disp_categories()

# Function to display Main Menu of the app
def disp_main_menu():
	main_menu = ['Categories', 'Display Cart', 'Display Wishlist', 'Display Userinfo', 'Exit']
	print("\n*** MAIN MENU ***\n")

	for i in range(len(main_menu)):
		print(f"{i+1}. {main_menu[i]}\n")	

	choice = int(input("Enter your choice:"))

	if choice == 1:
		disp_categories()

	elif choice == 2:
		disp_cart()
	
	elif choice == 3:
		disp_wishlist()

	elif choice == 4:
		disp_userinfo()
		pass

	elif choice == 5:
		exit()

	else:
		print("\nInvalid choice. Enter again")
		disp_main_menu()

# Program starts here
disp_user_greet()
disp_main_menu()