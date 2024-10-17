def add_food_item():
    banner = """
    +====================================================+
    +                   ADD FOOD ITEM PAGE               +
    +----------------------------------------------------+
    +             Allows you to add food items           +
    +====================================================+
    Enter required details:
    """
    print(banner)
    # Prompt user for number of food items to be added
    food_items = int(input("How many food items do you want to add? "))

    if food_items < 0:
        # Display the error message
        print("You cannot put a negative value")

        # Redirect back to add food item page for retrying
        add_food_item()

    for item in range(food_items):
        print(f"ENTER ITEM #{item + 1}")

        # Prompt user for food items
        food_id = int(input("Enter food ID: "))
        name = input("Enter food name: ")
        category = input("Enter food category: ")
        purchase_date = input("Enter purchase date: ")
        price = float(input("Enter the price: "))
        quantity = int(input("Enter the quantity: "))

        # TODO: Save the data

        # Display added food item
        print("\n------FOOD ITEM DETAILS------")
        print(f"Food ID: {food_id}")
        print(f"Name: {name}")
        print(f"Category: {category}")
        print(f"Purchase Date: {purchase_date}")
        print(f"Price: $ {price}")
        print(f"Quantity: {quantity}")

        # Display success message
        print(f"\n{name} has been added successfully.")

    # Redirect them to the food item menu
    manage_food_page()


def update_food_item():
    pass


def delete_food_item():
    pass


def view_food_items():
    pass


def logout():
    choice = input("Are you sure you want to logout? (Y/N): ")

    if choice == "Y" or choice == "y":
        # Render success message
        print("Log out successful. Redirecting to login page ...")

        # Redirect to login page
        login_page()

    else:
        # Redirect user to the food management page
        manage_food_page()


def exit_food_banner():
    """
    Smoothly terminates user program.
    """
    choice = input("Are you sure you want to exit? (Y/N): ")

    if choice == "Y" or choice == "y":
        print("Exiting the program...")
        exit()

    else:
        # Display redirect message
        print("Redirecting to the main menu...")

        # Redirect user to the main menu
        manage_food_page()


def manage_food_page():
    """
    Displays food menu options and validates user's choice.
    """
    # Display registration banner
    manage_food_banner = """
    +====================================================+
    +                  FOOD MANAGEMENT PAGE              +
    +----------------------------------------------------+
    +  Add, Delete, Update and View all you foods here!  +
    +====================================================+
    Select an option from the food menu:

    1. Add Food Item
    2. Update Food Item
    3. Delete Food Item
    4. View Food Items
    5. Logout
    6. Exit Program
    """
    print(manage_food_banner)

    # Allow user to make choice
    choice = int(input("Enter your choice: "))

    # Validate user choice
    if choice == 1:
        add_food_item()

    elif choice == 2:
        update_food_item()

    elif choice == 3:
        delete_food_item()

    elif choice == 4:
        view_food_items()

    elif choice == 5:
        logout()

    elif choice == 6:
        exit_food_banner()

    else:
        # Display error message
        print("You made an invalid choice. Please try again.")

        # Redirect user to manage food page to retry
        manage_food_page()


def registration_page():
    """
    Prompts user for registration details and redirects them to main menu.
    """
    # Display registration banner
    registration_banner = """
    +====================================================+
    +             MANAGER REGISTRATION PAGE              +
    +----------------------------------------------------+
    +    You don't have an account? Create one here!     +
    +====================================================+
    Fill in the requested details:
    """
    print(registration_banner)

    # Prompt user for registration details
    manager_id = int(input("Enter your Manager ID: "))
    name = input("Enter your full name: ")
    years_of_experience = int(input("Enter your years of experience: "))
    password = input("Enter your password: ")
    email_address = input("Enter your email address: ")
    phone_number = input("Enter your phone number: ")

    # Save to file
    print(f"Hello {name}. You have been registered successfully.")

    # Redirect to the main menu
    main_menu()


def login_page():
    """
    Prompts user for credentials.
    """
    # Display banner
    login_banner = """
    +====================================================+
    +                  MANAGER LOGIN PAGE                +
    +----------------------------------------------------+
    +         Already have an account? Login here!       +
    +====================================================+
    Fill in the requested details:
    """
    print(login_banner)

    # Request user credentials
    email_address = input("Enter your email address: ")
    password = input("Enter your password: ")

    # Validate user credentials
    if email_address == "kamau.ngengi@gmail.com" and password == "password":
        # Display success message
        print("You have logged in successfully. Redecting to the food page...")

        # Redirect user to manage food page
        manage_food_page()

    else:
        # Display the error message
        print("You have not logged in successfully.")

        # Redirect them to the login page
        login_page()


def exit_program():
    """
    Smoothly terminates user program.
    """
    choice = input("Are you sure you want to exit? (Y/N): ")

    if choice == "Y" or choice == "y":
        print("Exiting the program...")
        exit()

    else:
        # Display redirect message
        print("Redirecting to the main menu...")

        # Redirect user to the main menu
        main_menu()


def main_menu():
    """
    Displays main menu and validates user choice.
    """
    # Display the menu main banner
    main_menu_banner = """
    Select an item from the main menu:
    1. Register
    2. Login
    3. Exit
    """
    print(main_menu_banner)

    # Prompt user to select from the main menu
    choice = int(input("Enter your choice: "))

    # Validate user input
    if choice == 1:
        registration_page()

    elif choice == 2:
        login_page()

    elif choice == 3:
        exit_program()

    else:
        # Display error message to user
        print("You have made an invalid choice. Please try again!")

        # Redirect user to main menu to retry
        main_menu()


def main():
    """
    Displays main welcome page.
    """
    # Displaying the welcome banner
    welcome_banner = """
    +============================================================+
    +                  WELCOME TO UPESI JOINT                    +
    +------------------------------------------------------------+
    + We serve the hottest African Dishes in the Southern Sahara +
    +============================================================+
    """
    print(welcome_banner)

    # Go to the main menu
    main_menu()


main()
