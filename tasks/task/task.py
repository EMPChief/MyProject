import json
from pathlib import Path
from task import AddTask, ShowTask, EditTask, DeleteTask


class Task:
    def __init__(self, username):
        self.users_file = (
            Path(__file__).resolve().parent.parent / "database" / "users.json"
        )
        self.username = username

    def get_user_id(self):
        """Fetch the user ID from the users.json file based on the username."""
        if not self.users_file.exists():
            raise FileNotFoundError(f"Users file not found: {self.users_file}")

        try:
            with self.users_file.open("r") as file:
                user_data = json.load(file)
                if self.username in user_data:
                    return user_data[self.username]["userid"]
                else:
                    raise ValueError(
                        f"Username '{self.username}' not found in users file."
                    )
        except json.JSONDecodeError as e:
            raise ValueError(f"Error decoding JSON: {e}")
        except IOError as e:
            raise ValueError(f"Error reading users file: {e}")

    def add_task(self):
        """Add a new task for the user."""
        try:
            task_adder = AddTask(self.get_user_id())
            task_adder.add_task()
        except (FileNotFoundError, ValueError) as e:
            print(f"Error adding task: {e}")

    def show_task(self):
        """Show tasks for the user."""
        try:
            task_shower = ShowTask(self.get_user_id(), self.username)
            task_shower.show_tasks()
        except (FileNotFoundError, ValueError) as e:
            print(f"Error showing tasks: {e}")

    def edit_task(self):
        """Edit an existing task for the user."""
        try:
            task_editor = EditTask(self.get_user_id())
            task_editor.edit_task()
        except (FileNotFoundError, ValueError) as e:
            print(f"Error editing task: {e}")

    def delete_task(self):
        """Delete a task for the user."""
        try:
            task_deleter = DeleteTask(self.get_user_id())
            task_deleter.delete_task()
        except (FileNotFoundError, ValueError) as e:
            print(f"Error deleting task: {e}")
