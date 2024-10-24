from pathlib import Path
import json


class ShowTask:
    DATABASE_DIR = Path(__file__).resolve().parent.parent.parent / "database"
    ONGOING_TASKS_FILE = DATABASE_DIR / "ongoing.json"

    def __init__(self, user_id, username):
        """Initialize the TaskViewer with user ID and username."""
        self.user_id = user_id
        self.username = username

    def show_tasks(self):
        """Display all tasks for the user, or show a message if no tasks are found."""
        user_tasks = self._load_user_tasks()

        if user_tasks is None:
            print(f"Error loading tasks. Please try again.")
            return

        if not user_tasks:
            print(f"Sorry {self.username}, no tasks found. Please add one.")
            return

        self._display_user_tasks(user_tasks)

    def _load_user_tasks(self):
        """Load and return the tasks for the specific user."""
        if not self.ONGOING_TASKS_FILE.exists():
            return []

        try:
            with self.ONGOING_TASKS_FILE.open("r") as file:
                content = file.read()

                if not content:
                    return []

                ongoing_tasks = json.loads(content)
                return ongoing_tasks.get(str(self.user_id), [])
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error reading or parsing tasks file: {e}")
            return None

    def _display_user_tasks(self, tasks):
        """Display the tasks in a user-friendly format."""
        print(f"Here are your tasks, {self.username}:")
        for task in tasks:
            print("-----------")
            print(f"Task name: {task['name']}")
            print(f"Description: {task['description']}")
            print(f"Created at: {task['created_at']}")
            print(f"Status: {task['status']}")
            print("-----------")

