"""Main entry point for the task management system."""

import os
import sys

# Add the parent directory to sys.path if running as script
if __name__ == "__main__" and __package__ is None:
    file_path = os.path.abspath(__file__)
    parent_dir = os.path.dirname(os.path.dirname(file_path))
    sys.path.insert(0, parent_dir)
    __package__ = "tasks"

from tasks.auth.auth import Auth
from tasks.task.task import Task
from tasks.i18n import language_manager
from tasks.utils import print_with_clear


class TaskManager:
    ACTIONS = {
        'add': ('Add a new task', lambda task: task.add_task()),
        'view': ('View all tasks', lambda task: task.show_task()),
        'edit': ('Edit a task', lambda task: task.edit_task()),
        'delete': ('Delete a task', lambda task: task.delete_task()),
        'help': ('Show this help message', lambda _: None),
        'exit': ('Exit the program', lambda _: None)
    }

    def __init__(self):
        """Initialize the task manager."""
        self.auth = Auth()
        self.task = None
        self.username = None

    def start(self):
        """Start the task management system."""
        self._select_language()
        self._show_welcome_message()
        if not self._confirm_start():
            print_with_clear(language_manager.get_text("GOODBYE"))
            return

        if self._authenticate():
            self._run_main_program()

    def _select_language(self):
        """Handle language selection."""
        print_with_clear("""
=== Language Selection / Selección de Idioma / Språkvalg / 语言选择 / Selectare Limbă ===
en) English
es) Español
nb) Norsk (Bokmål)
zh) 中文
ro) Română
""")
        while True:
            choice = input("\nSelect your language / Seleccione su idioma / Velg språk / 选择语言 / Selectați limba (en/es/nb/zh/ro): ").lower().strip()
            if choice in ["en", "es", "nb", "zh", "ro"]:
                language_manager.set_language(choice)
                break
            print_with_clear("Invalid choice. Please try again. / Elección inválida. Inténtelo de nuevo.")

    def _show_welcome_message(self):
        """Display the welcome message."""
        print_with_clear(f"""
{language_manager.get_text("WELCOME_TITLE")}
{language_manager.get_text("WELCOME_MESSAGE")}
""")

    def _confirm_start(self):
        """Confirm if the user wants to start the program."""
        while True:
            choice = input(language_manager.get_text("CONFIRM_START")).lower().strip()
            if choice in ['y', 'yes', 's', 'si', 'sí', 'j', 'ja', '是', 'd', 'da']:
                return True
            if choice in ['n', 'no', 'nei', '否', 'nu']:
                return False
            print(language_manager.get_text("INVALID_YES_NO"))

    def _authenticate(self):
        """Handle user authentication."""
        try:
            print_with_clear()
            is_authenticated, username = self.auth.welcome()
            if is_authenticated:
                self.username = username
                self.task = Task(username)
                print_with_clear(language_manager.get_text("AUTH_SUCCESS").format(username))
                return True
            print(language_manager.get_text("AUTH_FAILED"))
            return False
        except Exception as e:
            print(language_manager.get_text("ERROR_AUTH").format(str(e)))
            return False

    def _run_main_program(self):
        """Run the main program loop."""
        print("\n" + language_manager.get_text("HELP_HINT"))
        
        while True:
            try:
                action = self._get_user_action()
                if action == 'exit':
                    print_with_clear(language_manager.get_text("GOODBYE_MESSAGE"))
                    break
                elif action == 'help':
                    self._show_help()
                else:
                    print_with_clear()  # Clear screen before executing action
                    self._execute_action(action)
            except KeyboardInterrupt:
                print("\n" + language_manager.get_text("PROGRAM_INTERRUPTED"))
                break
            except Exception as e:
                print(language_manager.get_text("ERROR_GENERAL").format(str(e)))
                print(language_manager.get_text("ERROR_TRY_AGAIN"))

    def _get_user_action(self):
        """Get and validate user action."""
        while True:
            action = input("\n" + language_manager.get_text("PROMPT_ACTION")).lower().strip()
            if action in self.ACTIONS:
                return action
            print(language_manager.get_text("INVALID_ACTION"))

    def _show_help(self):
        """Display available commands."""
        print_with_clear(language_manager.get_text("AVAILABLE_COMMANDS"))
        for cmd, (desc, _) in self.ACTIONS.items():
            print(f"  {cmd:<10} - {desc}")

    def _execute_action(self, action):
        """Execute the selected action."""
        _, func = self.ACTIONS[action]
        func(self.task)


if __name__ == "__main__":
    task_manager = TaskManager()
    task_manager.start()


class TestProgram:
    def __init__(self):
        # Mocked variables for testing
        self.mock_auth_success = True
        self.mock_username = "empchief"

    def bypass_auth_and_test(self):
        print("Bypassing authentication for testing.")
        self.run_main_program(self.mock_username)

    def run_main_program(self, username):
        print(f"Simulating running the main program for {username}...")
        task_manager = Task(self.mock_username)
        print(task_manager.get_user_id())
        while True:
            user_action = input(
                "What do you want to do? (add, view, delete, edit, exit): "
            ).lower()
            if user_action == "add":
                task_manager.add_task()
            if user_action == "view":
                task_manager.show_task()
            if user_action == "delete":
                task_manager.delete_task()
            if user_action == "edit":
                task_manager.edit_task()
            if user_action == "exit":
                break

    def test(self):
        print("Starting test...")
        self.bypass_auth_and_test()
