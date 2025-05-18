# Task Management System

A robust, multilingual command-line task management system built with Python. This system allows users to manage their tasks with features like task creation, editing, deletion, and status tracking.

## Features

- **User Authentication**
  - Secure login and registration system
  - User-specific task management

- **Task Management**
  - Create new tasks with name, description, priority, and category
  - View tasks with multiple sorting options
  - Edit existing tasks
  - Delete tasks with automatic archiving
  - Track task status and completion

- **Multilingual Support**
  - English
  - Spanish
  - Norwegian (Bokmål)
  - Chinese
  - Romanian

- **Rich Task Properties**
  - Priority levels (Urgent, High, Medium, Low)
  - Categories (Work, Personal, Shopping, Health, Study, Other)
  - Status tracking (In Progress, On Hold, Almost Done, Completed)
  - Creation and due dates
  - Detailed descriptions

- **Data Management**
  - JSON-based data storage
  - Optional JSON schema validation
  - Automatic task ID generation
  - Completed tasks archiving

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd task-management-system
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the program:
   ```bash
   python -m tasks
   ```

2. Select your preferred language when prompted

3. Log in or register a new account

4. Use the following commands:
   - `add` - Create a new task
   - `view` - View all tasks
   - `edit` - Modify an existing task
   - `delete` - Remove a task
   - `help` - Show available commands
   - `exit` - Close the program

## Project Structure

```
tasks/
├── __init__.py
├── __main__.py
├── main.py
├── utils.py
├── auth/
│   ├── __init__.py
│   ├── auth.py
│   ├── base_auth.py
│   ├── Login/
│   └── Register/
├── database/
│   ├── __init__.py
│   ├── db_manager.py
│   └── schemas.py
├── i18n/
│   ├── __init__.py
│   ├── language_manager.py
│   └── languages.py
└── task/
    ├── __init__.py
    ├── task.py
    ├── base_task.py
    ├── AddTask/
    ├── DeleteTask/
    ├── EditTask/
    └── ShowTask/
```

## Dependencies

- Python 3.6+
- jsonschema (optional, for JSON validation)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 