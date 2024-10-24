from pathlib import Path
import json


class Register:
    def register(self):
        # Define the path to the users.json file in the database directory
        user_database_file = (
            Path(__file__).resolve().parent.parent.parent / "database" / "users.json"
        )

        # Load existing user data, handling cases where the file doesn't exist or is corrupted
        try:
            with user_database_file.open("r") as file:
                try:
                    user_data = json.load(file)
                except json.JSONDecodeError:
                    print(
                        "Warning: User database is corrupted. Starting with an empty database."
                    )
                    user_data = {}
        except FileNotFoundError:
            print("User database not found. Starting new registration process.")
            user_data = {}

        # Prompt the user for their username and password with basic validation
        username_input = input("Enter username: ").strip()
        if not username_input:
            print("Error: Username cannot be empty.")
            return None

        password_input = input("Enter password: ").strip()
        if not password_input:
            print("Error: Password cannot be empty.")
            return None

        # Check if the username already exists
        if username_input in user_data:
            print(f"Error: Username '{username_input}' is already taken.")
            return None

        # Generate a unique user ID based on existing user data
        existing_user_ids = [user_info["userid"] for user_info in user_data.values()]
        user_id = 1
        while user_id in existing_user_ids:
            user_id += 1

        # Add the new user to the data dictionary
        user_data[username_input] = {"userid": user_id, "password": password_input}

        # Ensure the parent directory exists before saving the file
        user_database_file.parent.mkdir(parents=True, exist_ok=True)

        # Save the updated user data back to the users.json file
        with user_database_file.open("w") as file:
            json.dump(user_data, file, indent=4)

        print(f"Registration successful. Welcome, {username_input}!")
        return username_input
