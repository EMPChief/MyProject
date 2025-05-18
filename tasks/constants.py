"""Global constants used across the task management system."""

from pathlib import Path
from .i18n import language_manager

# Application Information
APP_NAME = "Task Management System"
APP_VERSION = "1.0.0"
APP_AUTHOR = "EmpChief"

# Directory and File Paths
ROOT_DIR = Path(__file__).resolve().parent
DATABASE_DIR = ROOT_DIR / "database"
DATABASE_DIR_NAME = "database"  # For backwards compatibility

# Database Files
USERS_FILENAME = "users.json"
ONGOING_TASKS_FILENAME = "ongoing.json"
COMPLETED_TASKS_FILENAME = "completed.json"

# Date and Time Formats
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
DATE_FORMAT = "%Y-%m-%d"
TIME_FORMAT = "%H:%M:%S"

# Task Status Options
VALID_STATUSES = language_manager.get_status_options()

# Task Priority Levels
PRIORITY_LEVELS = language_manager.get_priority_levels()
PRIORITY_ORDER = {
    language_manager.get_text("PRIORITY_URGENT"): 0,
    language_manager.get_text("PRIORITY_HIGH"): 1,
    language_manager.get_text("PRIORITY_MEDIUM"): 2,
    language_manager.get_text("PRIORITY_LOW"): 3
}

# Task Categories
CATEGORIES = language_manager.get_categories()

# System Messages
MESSAGES = {key: language_manager.get_text(key) for key in [
    "LOGIN_SUCCESS",
    "LOGIN_FAILED",
    "REGISTER_SUCCESS",
    "USERNAME_TAKEN",
    "INVALID_INPUT",
    "TASK_ADDED",
    "TASK_UPDATED",
    "TASK_DELETED",
    "TASK_NOT_FOUND",
    "NO_TASKS",
    "ERROR_LOADING",
    "ERROR_SAVING",
    "ERROR_INVALID_ACTION",
    "ERROR_PERMISSION"
]} 