from auth import Auth
from task import Task


class MainProgram:
    def welcome(self):
        print("Hello to my task program!")
        user_input = input("Do you want to use my program? (y/n): ").lower()
        if user_input in ["y", "yes"]:
            auth = Auth()
            is_authenticated, username = auth.welcome()
            if is_authenticated:
                print(f"Welcome, {
                      username}! You can now continue with the program.")
                self.run_main_program(username)
            else:
                print("Login or registration failed. Exiting the program.")
        else:
            print("Bye")

    def run_main_program(self, username):
        while True:
            user_action = input(
                "What do you want to do? (add, view, delete, edit, exit): "
            ).lower()
            if user_action == "add":
                Task(username).add_task()
            if user_action == "view":
                Task(username).show_task()
            if user_action == "delete":
                Task(username).delete_task()
            if user_action == "edit":
                Task(username).edit_task()
            if user_action == "exit":
                break


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


if __name__ == "__main__":
    MainProgram().welcome()
