from pathlib import Path
import json
import bcrypt


class Login:
    def __init__(self):
        self.user_database_file = (
            Path(__file__).resolve().parent.parent.parent / "database" / "users.json"
        )

    def load_user_data(self):
        """Load existing user data from the JSON file."""
        try:
            with self.user_database_file.open("r") as file:
                return json.load(file)
        except FileNotFoundError:
            print("Error: User database not found. Please register first.")
            return None
        except json.JSONDecodeError:
            print("Error: User database is corrupted or empty. Please contact support.")
            return None
        except Exception as e:
            print(f"Unexpected error loading user database: {e}")
            return None

    def get_user_input(self, prompt):
        """Get validated user input with error handling."""
        try:
            user_input = input(prompt).strip()
            if not user_input:
                print(f"Error: {prompt.split(':')[0]} cannot be empty.")
                return None
            return user_input
        except Exception as e:
            print(f"Unexpected error during input: {e}")
            return None

    def verify_password(self, password, hashed_password):
        """Verify the password against the hashed password."""
        try:
            return bcrypt.checkpw(password.encode(), hashed_password.encode())
        except Exception as e:
            print(f"Error verifying password: {e}")
            return False

    def login(self):
        """Main function to handle user login."""
        try:
            user_data = self.load_user_data()
            if not user_data:
                return None

            username_input = self.get_user_input("Enter username: ")
            if not username_input:
                return None

            password_input = self.get_user_input("Enter password: ")
            if not password_input:
                return None

            if username_input in user_data:
                stored_password = user_data[username_input]["password"]
                if self.verify_password(password_input, stored_password):
                    print(f"Login successful. Welcome, {username_input}!")
                    return username_input
                else:
                    print("Error: Incorrect password.")
            else:
                print(f"Error: Username '{username_input}' not found in the database.")
        except Exception as e:
            print(f"Unexpected error during login: {e}")
        return None
