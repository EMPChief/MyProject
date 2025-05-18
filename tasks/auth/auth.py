"""Authentication module for the task management system."""

from .Register.Register import Register
from .Login.Login import Login
from ..i18n import language_manager
from ..utils import print_with_clear


class Auth:
    def welcome(self):
        """Handle user authentication choice and process."""
        print_with_clear(language_manager.get_text("AUTH_WELCOME"))
        user_choice = input(language_manager.get_text("AUTH_CHOICE")).strip().lower()

        # Handle registration
        if user_choice in ["r", "register", "new", "create"]:
            print_with_clear(language_manager.get_text("AUTH_REGISTER_START"))
            registered_username = Register().register()
            if registered_username:
                return True, registered_username
            print(language_manager.get_text("AUTH_REGISTER_FAILED"))

        # Handle login
        elif user_choice in ["l", "login", "existing", "old"]:
            print_with_clear(language_manager.get_text("AUTH_LOGIN_START"))
            logged_in_username = Login().login()
            if logged_in_username:
                return True, logged_in_username
            print(language_manager.get_text("AUTH_LOGIN_FAILED"))

        # Invalid input handling
        else:
            print(language_manager.get_text("AUTH_INVALID_CHOICE"))

        return False, None
