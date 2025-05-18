# Database System Documentation

## Overview
The database system uses JSON files for data storage with optional schema validation, providing a lightweight and portable solution for managing user and task data.

## Components

### DatabaseManager Class
- Location: `database/db_manager.py`
- Purpose: Centralized database operations manager
- Features:
  - JSON file handling
  - Schema validation
  - Error handling
  - ID generation

## File Structure

### Data Directory
```
data/
├── users.json
├── ongoing_tasks.json
└── completed_tasks.json
```

### Schema Validation
- Location: `database/schemas.py`
- Optional validation using jsonschema
- Schemas for:
  - Users
  - Ongoing tasks
  - Completed tasks

## Database Operations

### User Operations
```python
# Get user
user_data = db.get_user(username)

# Save user
success = db.save_user(username, user_data)

# Get all users
users = db.get_all_users()
```

### Task Operations
```python
# Get user tasks
tasks = db.get_user_tasks(user_id)

# Save new task
success = db.save_user_task(user_id, task_data)

# Update task
success = db.update_user_task(user_id, task_id, task_data)

# Delete task
success = db.delete_user_task(user_id, task_id)

# Add completed task
success = db.add_completed_task(user_id, completed_task)
```

## Data Schemas

### Users Schema
```json
{
    "type": "object",
    "properties": {
        "username": {
            "type": "object",
            "properties": {
                "userid": {"type": "string"},
                "password": {"type": "string"},
                "created_at": {"type": "string"},
                "last_login": {"type": "string"}
            },
            "required": ["userid", "password", "created_at"]
        }
    }
}
```

### Tasks Schema
```json
{
    "type": "object",
    "properties": {
        "user_id": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "task_id": {"type": "integer"},
                    "name": {"type": "string"},
                    "description": {"type": "string"},
                    "priority": {"type": "string"},
                    "category": {"type": "string"},
                    "status": {"type": "string"},
                    "created_at": {"type": "string"},
                    "due_date": {"type": "string"}
                },
                "required": ["task_id", "name", "description", "status"]
            }
        }
    }
}
```

## Error Handling
- File not found
- JSON decode errors
- Schema validation errors
- Permission errors
- Disk space issues

## Data Backup
Currently manual, future improvements planned:
- [ ] Automatic backups
- [ ] Backup rotation
- [ ] Data export/import
- [ ] Recovery tools

## Security
- File permissions
- Data validation
- Error logging
- Safe file operations

## Future Improvements
- [ ] Add SQLite/PostgreSQL support
- [ ] Implement data migration tools
- [ ] Add data compression
- [ ] Add encryption support
- [ ] Implement backup system
- [ ] Add data versioning 