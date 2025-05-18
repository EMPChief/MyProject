"""Configuration module that centralizes all constants and configuration settings."""

from .constants import (
    # Application Information
    APP_NAME, APP_VERSION, APP_AUTHOR,
    
    # Directory and File Paths
    ROOT_DIR, DATABASE_DIR, DATABASE_DIR_NAME,
    
    # Database Files
    USERS_FILENAME, ONGOING_TASKS_FILENAME, COMPLETED_TASKS_FILENAME,
    
    # Date and Time Formats
    DATETIME_FORMAT, DATE_FORMAT, TIME_FORMAT,
    
    # Task Related Constants
    VALID_STATUSES, PRIORITY_LEVELS, PRIORITY_ORDER, CATEGORIES,
    
    # System Messages
    MESSAGES
)

# Re-export all constants
__all__ = [
    'APP_NAME', 'APP_VERSION', 'APP_AUTHOR',
    'ROOT_DIR', 'DATABASE_DIR', 'DATABASE_DIR_NAME',
    'USERS_FILENAME', 'ONGOING_TASKS_FILENAME', 'COMPLETED_TASKS_FILENAME',
    'DATETIME_FORMAT', 'DATE_FORMAT', 'TIME_FORMAT',
    'VALID_STATUSES', 'PRIORITY_LEVELS', 'PRIORITY_ORDER', 'CATEGORIES',
    'MESSAGES'
] 