from auth import Register, Login


class Auth:
    def welcome(self):
        # Prompt the user to register or log in
        user_choice = input("Do you want to register or login? (r/l): ").strip().lower()

        # Handle registration
        if user_choice in ["r", "register", "new", "create"]:
            registered_username = Register().register()
            if registered_username:
                return True, registered_username
            else:
                print("Registration failed. Please try again.")

        # Handle login
        elif user_choice in ["l", "login", "existing", "old"]:
            logged_in_username = Login().login()
            if logged_in_username:
                return True, logged_in_username
            else:
                print("Login failed. Please try again.")

        # Invalid input handling
        else:
            print("Invalid input. Please enter 'r' to register or 'l' to login.")

        return False, None
