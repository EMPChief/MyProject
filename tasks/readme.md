# Task Management System
#### Video Demo: <(https://youtu.be/rDXZaSi-ECQ)>
#### Description:
The Task Management System is a Python-based application designed to help users manage their tasks efficiently. The application allows users to create, read, update, and delete their tasks through a command-line interface, providing an intuitive way to stay organized. Each user is required to authenticate themselves using a unique username, ensuring that tasks are linked to the correct individual. Data is stored persistently in JSON files, enabling users to manage their tasks across multiple sessions without losing any information.

The system leverages simple file handling, user authentication, and basic CRUD (Create, Read, Update, Delete) operations to provide users with full control over their tasks. It is ideal for anyone looking for a lightweight task manager that can be accessed from a Python environment.

### Features:
The Task Management System includes a variety of features designed to make task management more efficient for users. These features include:

1. **User Authentication**: Users must register or log in with a unique username to access the task management system. The system ensures that only authenticated users can manage their tasks.
2. **Add Tasks**: Users can create new tasks by entering a name, description, and status (e.g., "In Progress", "Completed"). The system assigns a unique ID to each task and stores it in a persistent JSON file.
3. **View Tasks**: After logging in, users can view all their tasks with relevant details such as task name, description, creation time, and current status. This feature provides a clear overview of tasks that need attention or have been completed.
4. **Edit Tasks**: Users can modify the details of existing tasks, such as updating the task's name, description, or status. This feature allows users to track the progress of tasks or adjust deadlines and priorities as necessary.
5. **Delete Tasks**: Users can delete tasks they no longer need or want to track. Deleting tasks helps users maintain a clean and organized task list, especially when tasks are completed or canceled.

### Technologies Used:
This project is built using Python and relies on the following technologies:

- **Python**: The core logic of the application is written in Python. Python is chosen for its simplicity and ease of use, making it perfect for this command-line task manager.
- **JSON**: Data is stored in JSON files, which allows for easy reading and writing of user and task data. The data is stored in plain text format, which makes it simple to manage and review manually if needed.
- **File I/O**: The system reads and writes to JSON files using Python’s built-in file handling capabilities. This ensures that data is preserved across application restarts, allowing for persistent storage of tasks and user information.

### How the System Works:
The Task Management System operates in a simple, step-by-step process:

1. **User Authentication**:
   When a user first interacts with the system, they are asked to either register a new username or log in with an existing one. Registration involves creating a new user entry in the `users.json` file, and login involves verifying that the entered username matches an existing user. If the username is not found, the user will be prompted to register instead.

2. **Task Management**:
   Once logged in, the user can begin managing their tasks. The user is presented with a menu of options to add, view, edit, or delete tasks. The system stores tasks in the `ongoing.json` file, where each user’s tasks are stored under their unique user ID. This ensures that each user’s tasks are isolated from those of other users.
   
   - **Add Task**: To add a task, the user is prompted to provide a task name, description, and status. The task is then assigned a unique ID and added to the user's task list.
   - **View Tasks**: The user can view all their tasks, including their status and details such as when they were created. The system presents tasks in a user-friendly format, making it easy for the user to track their progress.
   - **Edit Task**: If a user wants to change the details of a task, they can edit the task’s name, description, or status. The system updates the task in the `ongoing.json` file to reflect the changes.
   - **Delete Task**: When a task is no longer needed or has been completed, the user can delete it. The task is removed from the user’s task list, and the `ongoing.json` file is updated accordingly.

3. **Data Storage**:
   All user and task data is stored in JSON files. The `users.json` file contains a mapping of usernames to user IDs, and the `ongoing.json` file contains each user’s tasks. The system reads from these files when users log in or view tasks, and writes to them when tasks are added, edited, or deleted. This ensures data is stored persistently across different sessions and can be easily modified.

### Key Components:
- **User Authentication**: The `Task` class handles user authentication. It manages the process of registering new users and logging in existing ones. Each user is associated with a unique ID, which is used to identify them in the `ongoing.json` file where their tasks are stored.
- **Task Operations**: The `AddTask`, `ShowTask`, `EditTask`, and `DeleteTask` classes handle the CRUD operations for tasks. Each class is responsible for one specific operation, and they work in conjunction to provide users with full control over their tasks.
- **Data Management**: User data and task data are stored in JSON files, ensuring that all information is preserved even when the program is restarted.

### Example Usage:
Here’s an example of how a user might interact with the system:

1. **User Registration**:
   - The user enters their desired username.
   - If the username is not already in use, the system creates a new entry for them in the `users.json` file.

2. **Adding Tasks**:
   - The user is prompted to enter the task name, description, and status.
   - The task is added to the `ongoing.json` file under the user’s unique ID.

3. **Viewing Tasks**:
   - The user selects the option to view their tasks.
   - The system displays a list of all tasks with their details (name, description, status).

4. **Editing Tasks**:
   - The user selects a task to edit.
   - The system prompts the user for updated details, such as a new name or description, and updates the task accordingly.

5. **Deleting Tasks**:
   - The user selects a task to delete.
   - The task is removed from the list, and the `ongoing.json` file is updated.


### usage of llm:
- Claude was used to fix the grammar and spelling errors in the code.
- ChatGPT was used to add more comments to the code and make my comment look a bit more professional.
