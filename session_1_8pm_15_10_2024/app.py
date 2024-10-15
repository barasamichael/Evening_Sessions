def manage_food_page():
    """
    Displays food menu options and validates user's choice.
    """
    pass


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
