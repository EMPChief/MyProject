"""JSON schemas for database validation."""

from typing import Dict, Any

USERS_SCHEMA = {
    "type": "object",
    "patternProperties": {
        "^[a-zA-Z0-9_]+$": {  # username pattern
            "type": "object",
            "required": ["userid", "password"],
            "properties": {
                "userid": {"type": "integer", "minimum": 1},
                "password": {"type": "string", "minLength": 60, "maxLength": 60}  # bcrypt hash length
            },
            "additionalProperties": False
        }
    }
}

ONGOING_TASKS_SCHEMA = {
    "type": "object",
    "patternProperties": {
        "^[0-9]+$": {  # user ID pattern
            "type": "array",
            "items": {
                "type": "object",
                "required": ["task_id", "name", "description", "created_at", "due_date", "status"],
                "properties": {
                    "task_id": {"type": "integer", "minimum": 1},
                    "name": {"type": "string", "minLength": 1},
                    "description": {"type": "string"},
                    "created_at": {"type": "string", "format": "date-time"},
                    "due_date": {"type": "string", "format": "date-time"},
                    "status": {"type": "string", "enum": ["In Progress", "On Hold", "Almost Done", "Completed"]},
                    "priority": {"type": "string", "enum": ["Low", "Medium", "High", "Urgent"]},
                    "category": {"type": "string", "enum": ["Work", "Personal", "Shopping", "Health", "Study", "Other"]}
                },
                "additionalProperties": False
            }
        }
    }
}

COMPLETED_TASKS_SCHEMA = {
    "type": "object",
    "patternProperties": {
        "^[0-9]+$": {  # user ID pattern
            "type": "array",
            "items": {
                "type": "object",
                "required": ["completed_id", "name", "description", "created_at", "due_date", "completed_at", "status"],
                "properties": {
                    "completed_id": {"type": "integer", "minimum": 1},
                    "name": {"type": "string", "minLength": 1},
                    "description": {"type": "string"},
                    "created_at": {"type": "string", "format": "date-time"},
                    "due_date": {"type": "string", "format": "date-time"},
                    "completed_at": {"type": "string", "format": "date-time"},
                    "status": {"type": "string", "enum": ["Completed"]},
                    "priority": {"type": "string", "enum": ["Low", "Medium", "High", "Urgent"]},
                    "category": {"type": "string", "enum": ["Work", "Personal", "Shopping", "Health", "Study", "Other"]}
                },
                "additionalProperties": False
            }
        }
    }
} 