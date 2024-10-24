import json
from pathlib import Path
from datetime import datetime, timedelta


class AddTask:
    DATABASE_DIR = Path(__file__).resolve().parent.parent.parent / "database"
    ONGOING_TASKS_FILE = DATABASE_DIR / "ongoing.json"

    def __init__(self, user_id):
        """Initialize the TaskManager with a user ID."""
        self.user_id = user_id

    def add_task(self):
        """Add a new task for the user."""
        try:
            ongoing_tasks = self._load_tasks()

            # Ensure the user has a list of tasks; if not, create one
            self._initialize_user_tasks(ongoing_tasks)

            # Prompt for task details
            task_name = self._get_task_detail("Enter task name: ")
            task_description = self._get_task_detail("Enter task description: ")

            # Create and save the new task
            new_task = self._create_task(task_name, task_description)
            ongoing_tasks[str(self.user_id)].append(new_task)
            self._save_tasks(ongoing_tasks)

            print("Task added successfully.")

        except Exception as e:
            print(f"An error occurred while adding the task: {e}")

    def _initialize_user_tasks(self, ongoing_tasks):
        """Initialize the user's tasks list if it doesn't exist."""
        if str(self.user_id) not in ongoing_tasks:
            ongoing_tasks[str(self.user_id)] = []

    def _get_task_detail(self, prompt):
        """Prompt the user for a task detail."""
        return input(prompt)

    def _create_task(self, name, description):
        """Create a new task dictionary with the given name and description."""
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        due_date = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")

        return {
            "task_id": self._generate_task_id(),
            "name": name,
            "description": description,
            "created_at": current_time,
            "due_date": due_date,
            "status": "In Progress",
        }

    def _generate_task_id(self):
        """Generate a unique task ID based on the current user's task count."""
        ongoing_tasks = self._load_tasks()
        return len(ongoing_tasks.get(str(self.user_id), [])) + 1

    def _load_tasks(self):
        """Load tasks from the ongoing tasks JSON file."""
        if not self.ONGOING_TASKS_FILE.exists():
            return {}

        try:
            with self.ONGOING_TASKS_FILE.open("r") as file:
                content = file.read()
                return json.loads(content) if content else {}

        except (IOError, json.JSONDecodeError) as e:
            print(f"An error occurred while loading tasks: {e}")
            return {}

    def _save_tasks(self, tasks):
        """Save tasks to the ongoing tasks JSON file."""
        try:
            with self.ONGOING_TASKS_FILE.open("w") as file:
                json.dump(tasks, file, indent=4)
        except IOError as e:
            print(f"An error occurred while saving tasks: {e}")

