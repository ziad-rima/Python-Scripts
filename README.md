# To-Do List Application

## Overview
This project is a CLI-based To-Do List application that began as a basic implementation using text files for data storage. Over time, it evolved into a more robust and dynamic version using JSON to handle tasks and categories. This README documents the journey from the initial implementation to the latest version, highlighting the changes, improvements, and rationale behind each stage.

---

## Initial Version
The first version of the script focused on basic task management functionality using a plain text file (`to_do_list.txt`) to store tasks. The primary functions in this version were:

### 1. **Add Task (`add_task`)**
Allows the user to add a task to the list by appending it to `to_do_list.txt`.

```python
# Initial Version
"""Add a task to your list"""
def add_task():
    task = input("Enter the task you want to add: ")
    with open("to_do_list.txt", "a") as file:
        file.write(task + "\n")
    print("Task added successfully.")
```

### 2. **View Tasks (`view_tasks`)**
Displays all tasks saved in the text file. It handles scenarios where the file is missing or empty.

```python
# Initial Version
"""View all tasks you added"""
def view_tasks():
    try:
        with open("to_do_list.txt", "r") as file:
            tasks = file.readlines()
            if tasks:
                print("\nYour to-do list:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task.strip()}")
            else:
                print("\nYour list is empty.")
    except FileNotFoundError:
        print("\nList doesn't exist, add a task to create one.")
```

### 3. **Clear All Tasks (`clear_all_tasks`)**
Clears all tasks after user confirmation.

```python
# Initial Version
def clear_all_tasks():
    try:
        confirm = input("Are you sure you want to clear all tasks? (y/n): ").lower()
        if confirm == "y":
            with open("to_do_list.txt", "r") as file:
                tasks = file.readlines()
                if not tasks:
                    print("\nYour list is already empty.")
                else:
                    open("to_do_list.txt", "w").close()
                    print("\nAll tasks are cleared.")
        else:
            print("\nClear operation canceled.")
    except FileNotFoundError:
        print("\nNo to-do list was found.")
```

### 4. **Clear a Specific Task (`clear_task`)**
Deletes a specific task chosen by the user.

```python
# Initial Version
def clear_task():
    try:
        view_tasks()
        with open("to_do_list.txt", "r") as file:
            tasks = file.readlines()
            if not tasks:
                print("\nYour to-do list is empty.")
            while True:
                try:
                    task_index = int(input("\nChoose the task number to delete: "))
                    if 1 <= task_index <= len(tasks):
                        break
                    else:
                        print(f"Please enter a number between 1 and {len(tasks)}.")
                except ValueError:
                    print("\nInvalid input. Please enter a number.")
            del tasks[task_index - 1]
            print("\nTask deleted successfully.")
            with open("to_do_list.txt", "w") as file:
                file.writelines(tasks)
            view_tasks()
    except FileNotFoundError:
        print("\nTo-Do list doesn't exist, add a task to create one.")
```

### 5. **Mark Task as Done (`mark_done`)**
Marks one or more tasks as completed by appending "(DONE)" to their description.

```python
# Initial Version
def mark_done():
    try:
        view_tasks()
        with open("to_do_list.txt", "r") as file:
            tasks = file.readlines()
            if not tasks:
                print("\nYour list is empty.")
                return
            while True:
                try:
                    task_indices = input("\nEnter the numbers associated with the tasks you want marked as done (comma separated): ")
                    task_indices = [int(index.strip()) for index in task_indices.split(",")]
                    if all(1 <= index <= len(tasks) for index in task_indices):
                        break
                    else:
                        print("\nEnter valid task numbers separated by commas (e.g., 1, 2, 3).")
                except ValueError:
                    print("\nInvalid input, please enter an integer")

            for index in task_indices:
                tasks[index - 1] = tasks[index - 1].strip() + " (DONE)\n"
            print("\nTasks marked done successfully.")
            with open("to_do_list.txt", "w") as file:
                file.writelines(tasks)
            view_tasks()
    except FileNotFoundError:
        print("\nYour To-Do list is not found, add a task to create one.")
```

---

## Evolution to JSON

Recognizing the limitations of a flat text file (e.g., lack of structure for tasks and categories), the script was upgraded to use JSON as the storage format. This allowed the app to manage tasks more effectively, enabling features like categories, task-specific updates, and dynamic data retrieval.

### Key Changes
- **Storage:** Shifted from a flat file to structured JSON (`to_do_list.json`).
- **Categories:** Added the ability to group tasks by category.
- **Dynamic Data Handling:** Introduced dynamic updates to specific tasks or categories.
- **Error Handling:** Improved exception handling for file operations and invalid input.

---

## Latest Features
The latest version of the application now includes:

1. **Add Tasks to Specific Categories**
```python
import json
def add_task():
    try:
        with open("to_do_list.json", "r") as file:
            dictionary = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        dictionary = {}
    task = input("Enter your task: ")
    category = input("Enter the category of the task: ").upper()
    if category not in dictionary:
        dictionary[category] = []
    dictionary[category].append(task)
    with open("to_do_list.json", "w") as file:
        json.dump(dictionary, file, indent=4)
    print("Task added successfully.")    
```
2. **View Tasks by Category**
```python
def view_tasks():
    try:
        with open("to_do_list.json", "r") as file:
            dictionary = json.load(file)
            if dictionary:
                print("\nYour to-do list:")
                for category, tasks in dictionary.items():
                    print(f"\n{category}:\n{tasks}")
            else: 
                print("\nYour list is empty.")
    except (FileNotFoundError, json.JSONDecodeError):
        print("\nList is empty.")
```
4. **Mark Multiple Tasks as Done**
```python
def mark_done():
    try:
        with open ("to_do_list.json", "r") as file:
            dictionary = json.load(file)
            if not dictionary:
                print("\nYour list is empty.")
                return 
            while True:
                try:
                    j = 1
                    for category, tasks in dictionary.items():
                        print(f"\n{j}. {category}: {tasks}")
                        j = j + 1
                    category_index = int(input("\nEnter the category number from which you want mark tasks as done: "))
                    if 1 <= category_index <= len(dictionary):
                        category_tasks = list(dictionary.values())[category_index - 1]
                        for i, tasks in enumerate(category_tasks, 1):
                            print(f"\n{i}. {tasks}")
                        task_indices = input("\nEnter the numbers associated with the tasks you want marked as done (comma separated): ")
                        task_indices = [int(index.strip()) for index in task_indices.split(",")]                                                                                     
                    if all (1 <= index <= len(category_tasks) for index in task_indices):
                        break
                    else:
                        print("\nEnter valid task numbers separated by commas (e.g., 1, 2, 3).")
                except ValueError:
                    print("\nInvalid input, please enter an integer")
            
            for index in task_indices:
                category_tasks[index - 1] = category_tasks[index - 1].strip() + " (DONE)"
            print("\nTasks marked done successfully.")
            categories = list(dictionary.keys())
            name_of_category = categories[category_index - 1]
            dictionary[name_of_category] = category_tasks
            with open("to_do_list.json", "w") as file:
                json.dump(dictionary, file, indent=4)
            view_tasks()
    except (FileNotFoundError, json.JSONDecodeError):
        print("\nYour To-Do list is not found, add a task to create one.")
```
6. **Clear All Tasks**
```python
def clear_all_tasks():
    try:
        confirm = input("Are you sure you want to clear all tasks? (y/n): ").lower()
        if confirm == "y":
            with open("to_do_list.json", "r") as file:
                dictionary = json.load(file) 
                if not dictionary:
                    print("\nYour list is already empty.")
                else:
                    open("to_do_list.json", "w").close()
                    print("\nAll tasks are cleard.")
        else:
            print("\nClear operation canceled.")
    except (FileNotFoundError, json.JSONDecodeError):
        print("\nNo to-do list was found.")
```
7. **Clear Tasks from Specific Categories**
```python
def clear_task():
    try:
        with open("to_do_list.json", "r") as file:
            dictionary = json.load(file)
            if not dictionary:
                print("\nYour to-do list is empty.")
                return
            while True:
                try: 
                    i = 1
                    for category, tasks in dictionary.items():
                        print(f"{i}. {category}: {tasks}")
                        i = i + 1
                    category_index = int(input("\nEnter the category number to delete the task from: "))
                    if 1 <= category_index <= len(dictionary):
                        category_tasks = list(dictionary.values())[category_index - 1]
                        for j, task in enumerate(category_tasks, 1):
                            print(f"{j}. {task}")
                        task_index = int(input("\nEnter the number of the task you want to delete: "))
                        if 1 <= task_index <= len(category_tasks):
                            break
                        else:
                            print(f"\nEnter a number between 1 and {len(category_tasks)}.")
                    else: 
                        print(f"Please enter a number between 1 and {len(dictionary)}.")
                except ValueError: 
                    print("\nInvalid input. Please enter a number.")
            del category_tasks[task_index - 1]
            categories = list(dictionary.keys())
            name_of_category = categories[category_index - 1]
            if not category_tasks:
                del dictionary[name_of_category]
                print(f"\nThe '{name_of_category}' category has been removed as it is now empty.")
            dictionary.update({f"{name_of_category}": category_tasks})
            print("\nTask deleted successfully.")
            with open("to_do_list.json", "w") as file:
                json.dump(dictionary, file, indent = 4)
            view_tasks()
    except (FileNotFoundError, json.JSONDecodeError):
        print("\nTo-Do list doesn't exist, add a task to create one.")
```
---

## Running the Application

1. Ensure Python is installed on your system.
2. Save the script to a file (e.g., `todo.py`).
3. Run the script using:

```bash
python todo.py
```

---

## Conclusion
This journey highlights the evolution of the To-Do List app from a simple file-based script to a JSON-driven, category-aware tool. The changes made it more dynamic, scalable, and user-friendly.

