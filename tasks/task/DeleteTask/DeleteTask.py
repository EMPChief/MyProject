import json
from pathlib import Path
from datetime import datetime


class DeleteTask:
    DATABASE_DIR = Path(__file__).resolve().parent.parent.parent / "database"
    ONGOING_TASKS_FILE = DATABASE_DIR / "ongoing.json"
    COMPLETED_TASKS_FILE = DATABASE_DIR / "completed.json"

    def __init__(self, user_id):
        """Initialize the DeleteTask with a user ID."""
        self.user_id = user_id

    def delete_task(self):
        """Delete a task for the user and move it to completed tasks."""
        try:
            ongoing_tasks = self._load_tasks()

            if not self._has_tasks(ongoing_tasks):
                print("You have no tasks to delete.")
                return

            user_tasks = ongoing_tasks[str(self.user_id)]
            self._display_user_tasks(user_tasks)

            task_id = self._get_task_detail(len(user_tasks))
            task_to_delete = self._find_task(user_tasks, task_id)

            if task_to_delete:
                self._move_to_completed(task_to_delete)
                user_tasks.remove(task_to_delete)
                self._reorder_tasks(user_tasks)
                self._save_tasks(ongoing_tasks)
                print("Task deleted successfully.")
            else:
                print("Invalid task ID. Please try again.")

        except Exception as e:
            print(f"An error occurred while deleting the task: {e}")

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

    def _has_tasks(self, ongoing_tasks):
        """Check if the user has any tasks."""
        return str(self.user_id) in ongoing_tasks and ongoing_tasks[str(self.user_id)]

    def _display_user_tasks(self, tasks):
        """Display the user's tasks in a formatted manner."""
        print("Here are your tasks:")
        for task in tasks:
            print(
                f"Task ID: {task['task_id']} | Name: {task['name']} | Status: {task['status']}"
            )

    def _get_task_detail(self, max_id):
        """Prompt for and validate task ID input."""
        while True:
            try:
                task_id = int(input(f"Enter the task ID to delete (1-{max_id}): "))
                if 1 <= task_id <= max_id:
                    return task_id
                print("Invalid task ID. Please try again.")
            except ValueError:
                print("Please enter a valid number.")

    def _find_task(self, tasks, task_id):
        """Find a task by its ID."""
        return next((task for task in tasks if task["task_id"] == task_id), None)

    def _reorder_tasks(self, tasks):
        """Reorder task IDs after deletion."""
        for idx, task in enumerate(tasks, 1):
            task["task_id"] = idx

    def _move_to_completed(self, task):
        """Move a task to the completed tasks file."""
        completed_tasks = self._load_completed_tasks()

        if str(self.user_id) not in completed_tasks:
            completed_tasks[str(self.user_id)] = []

        completed_task = {
            "completed_id": len(completed_tasks[str(self.user_id)]) + 1,
            "name": task["name"],
            "description": task["description"],
            "created_at": task["created_at"],
            "due_date": task["due_date"],
            "completed_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "status": "Completed",
        }

        completed_tasks[str(self.user_id)].append(completed_task)
        self._save_completed_tasks(completed_tasks)

    def _load_completed_tasks(self):
        """Load tasks from the completed tasks JSON file."""
        if not self.COMPLETED_TASKS_FILE.exists():
            return {}

        try:
            with self.COMPLETED_TASKS_FILE.open("r") as file:
                content = file.read()
                return json.loads(content) if content else {}
        except (IOError, json.JSONDecodeError) as e:
            print(f"An error occurred while loading completed tasks: {e}")
            return {}

    def _save_completed_tasks(self, tasks):
        """Save tasks to the completed tasks JSON file."""
        try:
            with self.COMPLETED_TASKS_FILE.open("w") as file:
                json.dump(tasks, file, indent=4)
        except IOError as e:
            print(f"An error occurred while saving completed tasks: {e}")

    def _save_tasks(self, tasks):
        """Save tasks to the ongoing tasks JSON file."""
        try:
            with self.ONGOING_TASKS_FILE.open("w") as file:
                json.dump(tasks, file, indent=4)
        except IOError as e:
            print(f"An error occurred while saving tasks: {e}")

