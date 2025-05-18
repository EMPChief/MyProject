"""Task module for the task management system."""

from .AddTask.AddTask import AddTask
from .ShowTask.ShowTask import ShowTask
from .EditTask.EditTask import EditTask
from .DeleteTask.DeleteTask import DeleteTask
from ..database.db_manager import DatabaseManager
from ..i18n import language_manager
from ..utils import print_with_clear


class Task:
    def __init__(self, username):
        """Initialize task manager with username."""
        self.username = username
        self.db = DatabaseManager()

    def get_user_id(self):
        """Fetch the user ID from the database based on the username."""
        try:
            user_data = self.db.get_user(self.username)
            if user_data:
                return user_data["userid"]
            raise ValueError(language_manager.get_text("USER_NOT_FOUND").format(self.username))
        except Exception as e:
            raise ValueError(language_manager.get_text("ERROR_LOADING").format(str(e)))

    def add_task(self):
        """Add a new task for the user."""
        try:
            task_adder = AddTask(self.get_user_id())
            task_adder.add_task()
        except Exception as e:
            print_with_clear(language_manager.get_text("ERROR_UNEXPECTED").format(str(e)))

    def show_task(self):
        """Show tasks for the user."""
        try:
            task_shower = ShowTask(self.get_user_id(), self.username)
            task_shower.show_tasks()
        except Exception as e:
            print_with_clear(language_manager.get_text("ERROR_UNEXPECTED").format(str(e)))

    def edit_task(self):
        """Edit an existing task for the user."""
        try:
            task_editor = EditTask(self.get_user_id())
            task_editor.edit_task()
        except Exception as e:
            print_with_clear(language_manager.get_text("ERROR_UNEXPECTED").format(str(e)))

    def delete_task(self):
        """Delete a task for the user."""
        try:
            task_deleter = DeleteTask(self.get_user_id())
            task_deleter.delete_task()
        except Exception as e:
            print_with_clear(language_manager.get_text("ERROR_UNEXPECTED").format(str(e)))
