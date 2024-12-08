from pathlib import Path
import json
import bcrypt


class Register:
    def __init__(self):
        self.user_database_file = (
            Path(__file__).resolve().parent.parent.parent / "database" / "users.json"
        )

    def load_user_data(self):
        """Load existing user data from the JSON file."""
        try:
            with self.user_database_file.open("r") as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    print(
                        "Warning: User database is corrupted. Starting with an empty database."
                    )
                    return {}
        except FileNotFoundError:
            print("User database not found. Starting new registration process.")
            return {}
        except Exception as e:
            print(f"Unexpected error loading user database: {e}")
            return {}

    def save_user_data(self, user_data):
        """Save the user data back to the JSON file."""
        try:
            self.user_database_file.parent.mkdir(parents=True, exist_ok=True)
            with self.user_database_file.open("w") as file:
                json.dump(user_data, file, indent=4)
        except Exception as e:
            print(f"Error saving user data: {e}")

    def get_user_input(self, prompt):
        """Get validated user input."""
        try:
            user_input = input(prompt).strip()
            if not user_input:
                print(f"Error: {prompt.split(':')[0]} cannot be empty.")
                return None
            return user_input
        except Exception as e:
            print(f"Unexpected error during input: {e}")
            return None

    def hash_password(self, password):
        """Hash the password using bcrypt."""
        try:
            return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        except Exception as e:
            print(f"Error hashing password: {e}")
            return None

    def generate_user_id(self, existing_user_ids):
        """Generate a unique user ID."""
        try:
            user_id = 1
            while user_id in existing_user_ids:
                user_id += 1
            return user_id
        except Exception as e:
            print(f"Error generating user ID: {e}")
            return None

    def register(self):
        """Main function to handle user registration."""
        try:
            user_data = self.load_user_data()

            username_input = self.get_user_input("Enter username: ")
            if not username_input:
                return None

            password_input = self.get_user_input("Enter password: ")
            if not password_input:
                return None

            if username_input in user_data:
                print(f"Error: Username '{username_input}' is already taken.")
                return None

            hashed_password = self.hash_password(password_input)
            if not hashed_password:
                print("Error: Failed to hash password.")
                return None

            user_id = self.generate_user_id(
                [user_info["userid"] for user_info in user_data.values()]
            )
            if not user_id:
                print("Error: Failed to generate user ID.")
                return None

            user_data[username_input] = {"userid": user_id, "password": hashed_password}
            self.save_user_data(user_data)

            print(f"Registration successful. Welcome, {username_input}!")
            return username_input
        except Exception as e:
            print(f"Unexpected error during registration: {e}")
            return None
