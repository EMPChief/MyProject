"""Base class for authentication operations."""

from ..database.db_manager import DatabaseManager
from ..i18n import language_manager


class BaseAuth:
    def __init__(self):
        """Initialize base authentication with database manager."""
        self.db = DatabaseManager()

    def get_user_input(self, prompt):
        """Get validated user input."""
        try:
            user_input = input(prompt).strip()
            if not user_input:
                field_name = prompt.split(':')[0]
                print(language_manager.get_text("INVALID_INPUT").format(f"{field_name} cannot be empty"))
                return None
            return user_input
        except Exception as e:
            print(language_manager.get_text("ERROR_UNEXPECTED").format(f"Error during input: {str(e)}"))
            return None 