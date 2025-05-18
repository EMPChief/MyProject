"""Registration functionality for the task management system."""

import bcrypt
from ..base_auth import BaseAuth
from ...i18n import language_manager


class Register(BaseAuth):
    def register(self):
        """Main function to handle user registration."""
        try:
            # Get user input
            username_input = self.get_user_input("Enter username: ")
            if not username_input:
                return None

            password_input = self.get_user_input("Enter password: ")
            if not password_input:
                return None

            # Check if username exists
            if self.db.get_user(username_input):
                print(language_manager.get_text("USERNAME_TAKEN").format(username_input))
                return None

            # Hash password
            try:
                hashed_password = bcrypt.hashpw(password_input.encode(), bcrypt.gensalt()).decode()
            except Exception as e:
                print(language_manager.get_text("ERROR_UNEXPECTED").format(f"Error hashing password: {str(e)}"))
                return None

            # Generate user ID
            existing_users = self.db.get_all_users()
            user_id = 1
            while any(user_info.get("userid") == user_id for user_info in existing_users.values()):
                user_id += 1

            # Save user
            user_data = {"userid": user_id, "password": hashed_password}
            if self.db.save_user(username_input, user_data):
                print(language_manager.get_text("REGISTER_SUCCESS").format(username_input))
                return username_input

            print(language_manager.get_text("ERROR_SAVING").format("Failed to save user data"))
            return None

        except Exception as e:
            print(language_manager.get_text("ERROR_UNEXPECTED").format(str(e)))
            return None
