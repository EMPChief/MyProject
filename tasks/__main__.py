"""Main entry point for running the task management system as a module."""

from .main import TaskManager

def main():
    task_manager = TaskManager()
    task_manager.start()

if __name__ == "__main__":
    main() 