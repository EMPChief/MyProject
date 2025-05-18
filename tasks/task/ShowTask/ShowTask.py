"""Task display functionality."""

from operator import itemgetter
from ...i18n import language_manager
from ..base_task import BaseTask
from ...utils import print_with_clear


class ShowTask(BaseTask):
    def __init__(self, user_id, username):
        """Initialize the TaskViewer with user ID and username."""
        super().__init__(user_id)
        self.username = username

    def show_tasks(self):
        """Display all tasks for the user."""
        try:
            user_tasks = self.db.get_user_tasks(self.user_id)

            if not self._user_has_tasks(user_tasks):
                print_with_clear(f"Sorry {self.username}, {language_manager.get_text('NO_TASKS')}")
                return

            sort_option = self._get_sort_option()
            sorted_tasks = self._sort_tasks(user_tasks, sort_option)
            self._display_user_tasks(sorted_tasks, detailed=True)

        except Exception as e:
            self._handle_error(e)

    def _get_sort_option(self):
        """Get the sorting preference from the user."""
        print_with_clear("\n" + language_manager.get_text("SORT_BY"))
        print("1. " + language_manager.get_text("SORT_PRIORITY"))
        print("2. " + language_manager.get_text("SORT_DUE_DATE"))
        print("3. " + language_manager.get_text("SORT_CATEGORY"))
        print("4. " + language_manager.get_text("SORT_STATUS"))
        print("5. " + language_manager.get_text("SORT_CREATION_DATE"))
        
        while True:
            try:
                choice = int(input(language_manager.get_text("ENTER_SORT_OPTION")))
                if 1 <= choice <= 5:
                    return choice
                print_with_clear(language_manager.get_text("INVALID_INPUT").format("Invalid choice"))
            except ValueError:
                print_with_clear(language_manager.get_text("INVALID_INPUT").format("Please enter a number"))

    def _sort_tasks(self, tasks, sort_option):
        """Sort tasks based on user preference."""
        if sort_option == 1:  # Priority
            priority_order = {
                language_manager.get_text("PRIORITY_URGENT"): 0,
                language_manager.get_text("PRIORITY_HIGH"): 1,
                language_manager.get_text("PRIORITY_MEDIUM"): 2,
                language_manager.get_text("PRIORITY_LOW"): 3
            }
            return sorted(tasks, key=lambda x: priority_order.get(x.get('priority', 'Low'), 4))
        elif sort_option == 2:  # Due Date
            return sorted(tasks, key=itemgetter('due_date'))
        elif sort_option == 3:  # Category
            return sorted(tasks, key=itemgetter('category'))
        elif sort_option == 4:  # Status
            return sorted(tasks, key=itemgetter('status'))
        else:  # Creation Date
            return sorted(tasks, key=itemgetter('created_at'))

    def _display_user_tasks(self, tasks, detailed=False):
        """Display the tasks in a user-friendly format."""
        print_with_clear(f"\n{language_manager.get_text('AVAILABLE_TASKS')}, {self.username}:")
        for task in tasks:
            print("\n" + "="*50)
            print(f"Task ID: {task['task_id']}")
            print(f"{language_manager.get_text('FIELD_NAME')}: {task['name']}")
            print(f"{language_manager.get_text('FIELD_DESCRIPTION')}: {task['description']}")
            print(f"{language_manager.get_text('FIELD_PRIORITY')}: {task.get('priority', 'Not set')}")
            print(f"{language_manager.get_text('FIELD_CATEGORY')}: {task.get('category', 'Not set')}")
            print(f"{language_manager.get_text('FIELD_STATUS')}: {task['status']}")
            print(f"{language_manager.get_text('SORT_CREATION_DATE')}: {task['created_at']}")
            print(f"{language_manager.get_text('SORT_DUE_DATE')}: {task['due_date']}")
            print("="*50)

