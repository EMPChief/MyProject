"""Task editing functionality."""

from ...i18n import language_manager
from ..base_task import BaseTask
from ...utils import print_with_clear


class EditTask(BaseTask):
    def edit_task(self):
        """Edit a task for the user."""
        try:
            user_tasks = self.db.get_user_tasks(self.user_id)

            if not self._user_has_tasks(user_tasks):
                return

            self._display_tasks(user_tasks)
            task_id = self._prompt_task_id(len(user_tasks))
            task_to_edit = self._find_task_by_id(user_tasks, task_id)

            if task_to_edit:
                print_with_clear(language_manager.get_text("EDITING_TASK").format(task_id))
                updated_task = self._edit_task_fields(task_to_edit)
                if self.db.update_user_task(self.user_id, task_id, updated_task):
                    print_with_clear(language_manager.get_text("TASK_UPDATED"))
                else:
                    print_with_clear(language_manager.get_text("ERROR_SAVING"))
            else:
                print_with_clear(language_manager.get_text("TASK_NOT_FOUND"))

        except Exception as e:
            print_with_clear(language_manager.get_text("ERROR_UNEXPECTED").format(str(e)))

    def _display_tasks(self, user_tasks):
        """Display the list of tasks for the user."""
        print_with_clear("\n" + language_manager.get_text("AVAILABLE_TASKS"))
        for task in user_tasks:
            print(f"[{task['task_id']}] {task['name']} - {task['description']}")
            print(f"    {language_manager.get_text('PRIORITY')}: {task.get('priority', 'Not set')} | "
                  f"{language_manager.get_text('CATEGORY')}: {task.get('category', 'Not set')} | "
                  f"{language_manager.get_text('STATUS')}: {task['status']}")

    def _prompt_task_id(self, max_id):
        """Prompt the user for a valid task ID to edit."""
        while True:
            try:
                task_id = int(input(language_manager.get_text("ENTER_TASK_ID").format(max_id)))
                if 1 <= task_id <= max_id:
                    return task_id
                print_with_clear(language_manager.get_text("INVALID_INPUT").format("Invalid task ID"))
            except ValueError:
                print_with_clear(language_manager.get_text("INVALID_INPUT").format("Please enter a number"))

    def _edit_task_fields(self, task):
        """Edit task fields based on user input."""
        field_to_edit = self._prompt_task_field()
        updated_task = task.copy()

        if field_to_edit == "name":
            updated_task["name"] = self._get_task_detail(language_manager.get_text("ENTER_NEW_NAME"))
        elif field_to_edit == "description":
            updated_task["description"] = self._get_task_detail(language_manager.get_text("ENTER_NEW_DESCRIPTION"))
        elif field_to_edit == "status":
            updated_task["status"] = self._prompt_valid_status()
        elif field_to_edit == "priority":
            updated_task["priority"] = self._prompt_valid_priority()
        elif field_to_edit == "category":
            updated_task["category"] = self._prompt_valid_category()

        return updated_task

    def _prompt_task_field(self):
        """Allow user to select which field to edit."""
        print_with_clear("\n" + language_manager.get_text("EDIT_FIELD_PROMPT"))
        fields = ["name", "description", "status", "priority", "category"]
        field_names = [
            language_manager.get_text("FIELD_NAME"),
            language_manager.get_text("FIELD_DESCRIPTION"),
            language_manager.get_text("FIELD_STATUS"),
            language_manager.get_text("FIELD_PRIORITY"),
            language_manager.get_text("FIELD_CATEGORY")
        ]
        
        for i, name in enumerate(field_names, 1):
            print(f"{i}. {name}")

        while True:
            try:
                choice = int(input(language_manager.get_text("ENTER_FIELD_CHOICE")))
                if 1 <= choice <= len(fields):
                    return fields[choice - 1]
                print_with_clear(language_manager.get_text("INVALID_INPUT").format("Invalid choice"))
            except ValueError:
                print_with_clear(language_manager.get_text("INVALID_INPUT").format("Please enter a number"))

    def _get_task_detail(self, prompt):
        """Get task detail from user input."""
        while True:
            detail = input(prompt).strip()
            if detail:
                return detail
            print_with_clear(language_manager.get_text("INVALID_INPUT").format("Input cannot be empty"))

    def _prompt_valid_status(self):
        """Prompt the user to select a valid status."""
        print_with_clear("\n" + language_manager.get_text("SELECT_STATUS"))
        statuses = [
            language_manager.get_text("STATUS_IN_PROGRESS"),
            language_manager.get_text("STATUS_ON_HOLD"),
            language_manager.get_text("STATUS_ALMOST_DONE"),
            language_manager.get_text("STATUS_COMPLETED")
        ]
        
        for i, status in enumerate(statuses, 1):
            print(f"{i}. {status}")

        while True:
            try:
                choice = int(input(language_manager.get_text("ENTER_STATUS_CHOICE")))
                if 1 <= choice <= len(statuses):
                    return statuses[choice - 1]
                print_with_clear(language_manager.get_text("INVALID_INPUT").format("Invalid status"))
            except ValueError:
                print_with_clear(language_manager.get_text("INVALID_INPUT").format("Please enter a number"))

    def _prompt_valid_priority(self):
        """Prompt the user to select a valid priority level."""
        print_with_clear("\n" + language_manager.get_text("SELECT_PRIORITY"))
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
                choice = int(input(language_manager.get_text("ENTER_PRIORITY_CHOICE")))
                if 1 <= choice <= len(priorities):
                    return priorities[choice - 1]
                print_with_clear(language_manager.get_text("INVALID_INPUT").format("Invalid priority"))
            except ValueError:
                print_with_clear(language_manager.get_text("INVALID_INPUT").format("Please enter a number"))

    def _prompt_valid_category(self):
        """Prompt the user to select a valid category."""
        print_with_clear("\n" + language_manager.get_text("SELECT_CATEGORY"))
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
                choice = int(input(language_manager.get_text("ENTER_CATEGORY_CHOICE")))
                if 1 <= choice <= len(categories):
                    return categories[choice - 1]
                print_with_clear(language_manager.get_text("INVALID_INPUT").format("Invalid category"))
            except ValueError:
                print_with_clear(language_manager.get_text("INVALID_INPUT").format("Please enter a number"))

