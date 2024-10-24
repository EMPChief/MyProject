from pathlib import Path
import json


class Login:
    def login(self):
        # Define the path to the users.json file in the database directory
        user_database_file = (
            Path(__file__).resolve().parent.parent.parent / "database" / "users.json"
        )

        # Try to open and load the user database, handle file not found error
        try:
            with user_database_file.open("r") as file:
                user_data = json.load(file)
        except FileNotFoundError:
            print("Error: User database not found. Please register first.")
            return None
        except json.JSONDecodeError:
            print("Error: User database is corrupted or empty. Please contact support.")
            return None

        # Get the username and password from the user input with basic validation
        username_input = input("Enter username: ").strip()
        if not username_input:
            print("Error: Username cannot be empty.")
            return None

        password_input = input("Enter password: ").strip()
        if not password_input:
            print("Error: Password cannot be empty.")
            return None

        # Validate the username and password against the user database
        if username_input in user_data:
            stored_password = user_data[username_input]["password"]
            if stored_password == password_input:
                print(f"Login successful. Welcome, {username_input}!")
                return username_input
            else:
                print("Error: Incorrect password.")
        else:
            print(f"Error: Username '{username_input}' not found in the database.")

        return None
