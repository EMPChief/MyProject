"""Base class for task operations."""

from ..database.db_manager import DatabaseManager
from ..i18n import language_manager
from ..utils import print_with_clear

class BaseTask:
    def __init__(self, user_id):
        """Initialize base task with user ID and database manager."""
        self.user_id = user_id
        self.db = DatabaseManager()

    def _load_tasks(self):
        """Load tasks from the database."""
        return self.db.get_user_tasks(self.user_id)

    def _save_tasks(self, tasks):
        """Save tasks to the database."""
        return self.db.save_user_task(self.user_id, tasks)

    def _user_has_tasks(self, tasks):
        """Check if the user has any tasks."""
        if not tasks:
            print_with_clear(language_manager.get_text("NO_TASKS"))
            return False
        return True

    def _find_task_by_id(self, user_tasks, task_id):
        """Find and return a task by its ID."""
        task = next((task for task in user_tasks if task["task_id"] == task_id), None)
        if task is None:
            print_with_clear(language_manager.get_text("TASK_NOT_FOUND"))
        return task

    def _display_user_tasks(self, tasks, detailed=True):
        """Display the tasks in a user-friendly format.
        
        Args:
            tasks: List of tasks to display
            detailed: Whether to show all task details (True) or just basic info (False)
        """
        print_with_clear("\n" + language_manager.get_text("AVAILABLE_TASKS"))
        for task in tasks:
            print("\n" + "="*50)
            print(f"Task ID: {task['task_id']}")
            print(f"{language_manager.get_text('FIELD_NAME')}: {task['name']}")
            print(f"{language_manager.get_text('FIELD_DESCRIPTION')}: {task['description']}")
            
            if detailed:
                print(f"{language_manager.get_text('FIELD_PRIORITY')}: {task.get('priority', 'Not set')}")
                print(f"{language_manager.get_text('FIELD_CATEGORY')}: {task.get('category', 'Not set')}")
                print(f"{language_manager.get_text('FIELD_STATUS')}: {task['status']}")
                print(f"{language_manager.get_text('SORT_CREATION_DATE')}: {task['created_at']}")
                print(f"{language_manager.get_text('SORT_DUE_DATE')}: {task['due_date']}")
            print("="*50)

    def _handle_error(self, error, message_key="ERROR_UNEXPECTED"):
        """Standardized error handling for task operations."""
        print_with_clear(language_manager.get_text(message_key).format(str(error)))

    def _get_user_tasks(self):
        """Get all tasks for the current user."""
        user_tasks = self.db.get_user_tasks(self.user_id)
        if not user_tasks:
            print_with_clear(language_manager.get_text("NO_TASKS"))
        return user_tasks 