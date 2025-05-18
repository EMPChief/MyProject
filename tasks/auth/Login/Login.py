"""Login functionality for the task management system."""

import bcrypt
from ..base_auth import BaseAuth
from ...i18n import language_manager


class Login(BaseAuth):
    def login(self):
        """Main function to handle user login."""
        try:
            username_input = self.get_user_input("Enter username: ")
            if not username_input:
                return None

            password_input = self.get_user_input("Enter password: ")
            if not password_input:
                return None

            user_data = self.db.get_user(username_input)
            if user_data:
                stored_password = user_data["password"]
                if self.verify_password(password_input, stored_password):
                    print(language_manager.get_text("LOGIN_SUCCESS").format(username_input))
                    return username_input
                else:
                    print(language_manager.get_text("LOGIN_FAILED"))
            else:
                print(language_manager.get_text("LOGIN_FAILED"))

        except Exception as e:
            print(language_manager.get_text("ERROR_UNEXPECTED").format(str(e)))
        return None

    def verify_password(self, password, hashed_password):
        """Verify the password against the hashed password."""
        try:
            return bcrypt.checkpw(password.encode(), hashed_password.encode())
        except Exception as e:
            print(language_manager.get_text("ERROR_UNEXPECTED").format(f"Error verifying password: {str(e)}"))
            return False