# Task Management Documentation

## Overview
The task management system provides comprehensive task tracking with support for creating, viewing, editing, and deleting tasks.

## Components

### BaseTask Class
- Location: `task/base_task.py`
- Purpose: Base class for all task operations
- Key Features:
  - Common task operations
  - Error handling
  - Display formatting
  - Database interaction

### Task Classes

#### AddTask
- Location: `task/AddTask/AddTask.py`
- Features:
  - Task creation
  - Priority selection
  - Category assignment
  - Due date setting
- Input Validation:
  - Required fields
  - Valid priority levels
  - Valid categories

#### ShowTask
- Location: `task/ShowTask/ShowTask.py`
- Features:
  - Task listing
  - Multiple sort options
  - Detailed/Basic views
- Sort Options:
  - Priority
  - Due Date
  - Category
  - Status
  - Creation Date

#### EditTask
- Location: `task/EditTask/EditTask.py`
- Features:
  - Task modification
  - Field selection
  - Status updates
- Editable Fields:
  - Name
  - Description
  - Priority
  - Category
  - Status

#### DeleteTask
- Location: `task/DeleteTask/DeleteTask.py`
- Features:
  - Task deletion
  - Automatic archiving
  - Completion tracking
- Archive Process:
  - Move to completed tasks
  - Update status
  - Record completion time

## Task Schema
```json
{
    "task_id": "integer",
    "name": "string",
    "description": "string",
    "priority": "string (Urgent|High|Medium|Low)",
    "category": "string (Work|Personal|Shopping|Health|Study|Other)",
    "status": "string (In Progress|On Hold|Almost Done|Completed)",
    "created_at": "timestamp",
    "due_date": "timestamp"
}
```

## Usage Examples

### Creating a Task
```python
from tasks.task import AddTask

task_adder = AddTask(user_id)
task_adder.add_task()
```

### Viewing Tasks
```python
from tasks.task import ShowTask

task_viewer = ShowTask(user_id, username)
task_viewer.show_tasks()
```

### Editing a Task
```python
from tasks.task import EditTask

task_editor = EditTask(user_id)
task_editor.edit_task()
```

### Deleting a Task
```python
from tasks.task import DeleteTask

task_deleter = DeleteTask(user_id)
task_deleter.delete_task()
```

## Error Handling
- Task not found
- Invalid input
- Database errors
- Permission issues

## Display Formatting
- Clear screen functionality
- Consistent layout
- Internationalized messages
- Color coding (future)

## Future Improvements
- [ ] Add task categories customization
- [ ] Implement subtasks
- [ ] Add task priorities customization
- [ ] Include task attachments
- [ ] Add task sharing between users
- [ ] Implement task templates 