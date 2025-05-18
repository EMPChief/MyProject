"""Task deletion functionality."""

from datetime import datetime
from ...i18n import language_manager
from ..base_task import BaseTask
from ...utils import print_with_clear


class DeleteTask(BaseTask):
    def delete_task(self):
        """Delete a task for the user and move it to completed tasks."""
        try:
            user_tasks = self.db.get_user_tasks(self.user_id)

            if not self._user_has_tasks(user_tasks):
                return

            self._display_user_tasks(user_tasks, detailed=False)
            task_id = self._get_task_id(len(user_tasks))
            task_to_delete = self._find_task_by_id(user_tasks, task_id)

            if task_to_delete:
                # Move to completed tasks
                completed_task = self._prepare_completed_task(task_to_delete)
                if self.db.add_completed_task(self.user_id, completed_task):
                    # Delete from ongoing tasks
                    if self.db.delete_user_task(self.user_id, task_id):
                        print_with_clear(language_manager.get_text("TASK_DELETED"))
                    else:
                        print_with_clear(language_manager.get_text("ERROR_SAVING"))
                else:
                    print_with_clear(language_manager.get_text("ERROR_SAVING"))

        except Exception as e:
            self._handle_error(e)

    def _get_task_id(self, max_id):
        """Get a valid task ID from user input."""
        while True:
            try:
                task_id = int(input(f"Enter the task ID to delete (1-{max_id}): "))
                if 1 <= task_id <= max_id:
                    return task_id
                print_with_clear(language_manager.get_text("INVALID_INPUT").format("Invalid task ID"))
            except ValueError:
                print_with_clear(language_manager.get_text("INVALID_INPUT").format("Please enter a number"))

    def _prepare_completed_task(self, task):
        """Prepare a task for moving to completed tasks."""
        completed_tasks = self.db.get_completed_tasks(self.user_id)
        completed_id = len(completed_tasks) + 1
        
        return {
            "completed_id": completed_id,
            "name": task["name"],
            "description": task["description"],
            "created_at": task["created_at"],
            "due_date": task["due_date"],
            "completed_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "status": language_manager.get_text("STATUS_COMPLETED"),
            "priority": task.get("priority"),
            "category": task.get("category")
        }

