"""Task addition functionality."""

from datetime import datetime, timedelta
from ...i18n import language_manager
from ..base_task import BaseTask
from ...utils import print_with_clear


class AddTask(BaseTask):
    def add_task(self):
        """Add a new task for the user."""
        try:
            # Get task details from user
            task_name = self._get_task_detail("Enter task name: ")
            task_description = self._get_task_detail("Enter task description: ")
            priority = self._get_priority()
            category = self._get_category()

            # Create the new task
            new_task = self._create_task(task_name, task_description, priority, category)
            
            # Save the task
            if self.db.save_user_task(self.user_id, new_task):
                print_with_clear(language_manager.get_text("TASK_ADDED"))
            else:
                self._handle_error(None, "ERROR_SAVING")

        except Exception as e:
            self._handle_error(e)

    def _get_task_detail(self, prompt):
        """Get task detail from user input."""
        while True:
            detail = input(prompt).strip()
            if detail:
                return detail
            print(language_manager.get_text("INVALID_INPUT").format("Input cannot be empty"))

    def _get_priority(self):
        """Get task priority from user."""
        print_with_clear("\nPriority Levels:")
        priorities = [
            language_manager.get_text("PRIORITY_LOW"),
            language_manager.get_text("PRIORITY_MEDIUM"),
            language_manager.get_text("PRIORITY_HIGH"),
            language_manager.get_text("PRIORITY_URGENT")
        ]
        for i, priority in enumerate(priorities, 1):
            print(f"{i}. {priority}")

        while True:
            try:
                choice = int(input("Select priority (1-4): "))
                if 1 <= choice <= 4:
                    return priorities[choice - 1]
                print(language_manager.get_text("INVALID_INPUT").format("Invalid priority number"))
            except ValueError:
                print(language_manager.get_text("INVALID_INPUT").format("Please enter a number"))

    def _get_category(self):
        """Get task category from user."""
        print_with_clear("\nCategories:")
        categories = [
            language_manager.get_text("CATEGORY_WORK"),
            language_manager.get_text("CATEGORY_PERSONAL"),
            language_manager.get_text("CATEGORY_SHOPPING"),
            language_manager.get_text("CATEGORY_HEALTH"),
            language_manager.get_text("CATEGORY_STUDY"),
            language_manager.get_text("CATEGORY_OTHER")
        ]
        for i, category in enumerate(categories, 1):
            print(f"{i}. {category}")

        while True:
            try:
                choice = int(input("Select category (1-6): "))
                if 1 <= choice <= 6:
                    return categories[choice - 1]
                print(language_manager.get_text("INVALID_INPUT").format("Invalid category number"))
            except ValueError:
                print(language_manager.get_text("INVALID_INPUT").format("Please enter a number"))

    def _create_task(self, name, description, priority, category):
        """Create a new task with the given details."""
        now = datetime.now()
        
        return {
            "name": name,
            "description": description,
            "priority": priority,
            "category": category,
            "created_at": now.strftime("%Y-%m-%d %H:%M:%S"),
            "due_date": (now + timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S"),
            "status": language_manager.get_text("STATUS_IN_PROGRESS")
        }

