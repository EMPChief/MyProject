"""Database manager for handling JSON database operations."""

import json
from pathlib import Path
from typing import Dict, Any, Optional
from .schemas import USERS_SCHEMA, ONGOING_TASKS_SCHEMA, COMPLETED_TASKS_SCHEMA
from ..i18n import language_manager


try:
    import jsonschema
    SCHEMA_VALIDATION_ENABLED = True
except ImportError:
    SCHEMA_VALIDATION_ENABLED = False
    print("Warning: jsonschema package not found. Schema validation will be disabled.")

class DatabaseManager:
    def __init__(self):
        """Initialize the database manager."""
        self.base_dir = Path(__file__).parent.parent / "data"
        self.base_dir.mkdir(exist_ok=True)
        
        self.users_file = self.base_dir / "users.json"
        self.ongoing_tasks_file = self.base_dir / "ongoing_tasks.json"
        self.completed_tasks_file = self.base_dir / "completed_tasks.json"
        
        self._initialize_files()

    def _initialize_files(self):
        """Initialize JSON files if they don't exist."""
        for file_path in [self.users_file, self.ongoing_tasks_file, self.completed_tasks_file]:
            if not file_path.exists():
                with open(file_path, 'w') as f:
                    json.dump({}, f)

    def _load_json(self, file_path: Path) -> dict:
        """Load data from a JSON file."""
        try:
            with open(file_path, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {}

    def _save_json(self, file_path: Path, data: dict) -> bool:
        """Save data to a JSON file."""
        try:
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=4)
            return True
        except Exception:
            return False

    def _generate_task_id(self, user_id: str, is_completed: bool = False) -> int:
        """Generate a new task ID for a user.
        
        Args:
            user_id: The user's ID
            is_completed: Whether this is for a completed task
            
        Returns:
            A new unique task ID
        """
        file_path = self.completed_tasks_file if is_completed else self.ongoing_tasks_file
        tasks = self._load_json(file_path)
        user_tasks = tasks.get(str(user_id), [])
        return len(user_tasks) + 1

    # User operations
    def get_user(self, username: str) -> Optional[Dict[str, Any]]:
        """Get user data by username."""
        users = self._load_json(self.users_file)
        return users.get(username)

    def get_all_users(self) -> Dict[str, Any]:
        """Get all users data."""
        return self._load_json(self.users_file)

    def save_user(self, username: str, user_data: Dict[str, Any]) -> bool:
        """Save or update user data."""
        users = self._load_json(self.users_file)
        users[username] = user_data
        return self._save_json(self.users_file, users)

    # Task operations
    def get_user_tasks(self, user_id: str) -> list:
        """Get all ongoing tasks for a user."""
        tasks = self._load_json(self.ongoing_tasks_file)
        return tasks.get(str(user_id), [])

    def save_user_task(self, user_id: str, task_data: Dict[str, Any]) -> bool:
        """Save a new task for a user."""
        tasks = self._load_json(self.ongoing_tasks_file)
        if str(user_id) not in tasks:
            tasks[str(user_id)] = []
        
        # Generate new task ID if not provided
        if 'task_id' not in task_data:
            task_data['task_id'] = self._generate_task_id(user_id)
            
        tasks[str(user_id)].append(task_data)
        return self._save_json(self.ongoing_tasks_file, tasks)

    def update_user_task(self, user_id: str, task_id: int, task_data: Dict[str, Any]) -> bool:
        """Update an existing task."""
        tasks = self._load_json(self.ongoing_tasks_file)
        user_tasks = tasks.get(str(user_id), [])
        
        for i, task in enumerate(user_tasks):
            if task["task_id"] == task_id:
                # Preserve the original task ID
                task_data['task_id'] = task_id
                user_tasks[i] = task_data
                return self._save_json(self.ongoing_tasks_file, tasks)
        return False

    def delete_user_task(self, user_id: str, task_id: int) -> bool:
        """Delete a task."""
        tasks = self._load_json(self.ongoing_tasks_file)
        user_tasks = tasks.get(str(user_id), [])
        
        for task in user_tasks[:]:
            if task["task_id"] == task_id:
                user_tasks.remove(task)
                return self._save_json(self.ongoing_tasks_file, tasks)
        return False

    def add_completed_task(self, user_id: str, task_data: Dict[str, Any]) -> bool:
        """Add a task to completed tasks."""
        completed = self._load_json(self.completed_tasks_file)
        if str(user_id) not in completed:
            completed[str(user_id)] = []
            
        # Generate new completed task ID if not provided
        if 'completed_id' not in task_data:
            task_data['completed_id'] = self._generate_task_id(user_id, is_completed=True)
            
        completed[str(user_id)].append(task_data)
        return self._save_json(self.completed_tasks_file, completed)

    def get_completed_tasks(self, user_id: str) -> list:
        """Get all completed tasks for a user."""
        completed = self._load_json(self.completed_tasks_file)
        return completed.get(str(user_id), []) 