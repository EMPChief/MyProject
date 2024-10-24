import json
from pathlib import Path


class EditTask:
    VALID_STATUSES = ["In Progress", "On Hold", "Almost Done", "Completed"]

    def __init__(self, user_id):
        """Initialize the class with user_id and define the path to the ongoing tasks JSON file."""
        self.user_id = user_id
        self.tasks_file_path = (
            Path(__file__).resolve().parent.parent.parent / "database" / "ongoing.json"
        )

    def edit_task(self):
        """Edit a task for the user."""
        tasks = self._load_tasks()

        if not self._user_has_tasks(tasks):
            print("No tasks found for you.")
            return

        self._display_tasks(tasks[str(self.user_id)])

        task_id_to_edit = self._prompt_task_id(tasks[str(self.user_id)])

        task_to_edit = self._find_task_by_id(tasks[str(self.user_id)], task_id_to_edit)

        if task_to_edit:
            print(f"Editing task {task_id_to_edit}")
            self._edit_task_fields(task_to_edit)
            self._save_tasks(tasks)
            print("Task edited successfully.")
        else:
            print("Task not found. Please try again.")

    def _load_tasks(self):
        """Load tasks from the ongoing.json file."""
        if not self.tasks_file_path.exists():
            return {}

        try:
            with self.tasks_file_path.open() as file:
                content = file.read()
                if not content:
                    return {}

                return json.loads(content)
        except (IOError, json.JSONDecodeError) as error:
            print(f"Error loading tasks: {error}")
            return {}

    def _save_tasks(self, tasks):
        """Save tasks to the ongoing.json file."""
        try:
            with self.tasks_file_path.open("w") as file:
                json.dump(tasks, file, indent=4)
        except IOError as error:
            print(f"Error saving tasks: {error}")

    def _user_has_tasks(self, tasks):
        """Check if the user has any tasks."""
        return str(self.user_id) in tasks and tasks[str(self.user_id)]

    def _display_tasks(self, user_tasks):
        """Display the list of tasks for the user."""
        print("Here are your tasks:")
        for task in user_tasks:
            print(f"[{task['task_id']}] {task['name']} - {task['description']}")

    def _prompt_task_id(self, user_tasks):
        """Prompt the user for a valid task ID to edit."""
        max_task_id = len(user_tasks)
        while True:
            try:
                task_id = int(input(f"Enter the task ID to edit (1-{max_task_id}): "))
                if 1 <= task_id <= max_task_id:
                    return task_id
                else:
                    print("Invalid task ID. Please try again.")
            except ValueError as error:
                print(f"Error: {error}. Please enter a valid task ID.")

    def _find_task_by_id(self, user_tasks, task_id):
        """Find and return the task object by its ID."""
        return next((task for task in user_tasks if task["task_id"] == task_id), None)

    def _edit_task_fields(self, task):
        """Prompt user to edit task fields."""
        field_to_edit = self._prompt_task_field()
        if field_to_edit == "name":
            new_name = input("Enter the new name: ")
            task["name"] = new_name
        elif field_to_edit == "description":
            new_description = input("Enter the new description: ")
            task["description"] = new_description
        elif field_to_edit == "status":
            new_status = self._prompt_valid_status()
            task["status"] = new_status
        else:
            print("Invalid field to edit.")

    def _prompt_task_field(self):
        """Allow user to edit task name, description, and status."""
        print("What field would you like to edit?")
        print("1. Name")
        print("2. Description")
        print("3. Status")
        while True:
            choice = input("Enter your choice (1-3): ")
            if choice == "1":
                return "name"
            elif choice == "2":
                return "description"
            elif choice == "3":
                return "status"
            else:
                print("Invalid choice. Please try again.")

    def _prompt_valid_status(self):
        """Prompt the user to enter a valid status by selecting a number (1-4)."""
        print("Choose a new status for the task:")
        for index, status in enumerate(self.VALID_STATUSES, 1):
            print(f"{index}. {status}")

        while True:
            try:
                choice = int(input("Enter your choice (1-4): "))
                if 1 <= choice <= len(self.VALID_STATUSES):
                    return self.VALID_STATUSES[choice - 1]
                else:
                    print("Invalid choice. Please choose a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 4.")

