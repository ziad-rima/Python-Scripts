import json

# TO-DO list script 

# App Overview:

# . Add tasks to a to-do list
# . Do some stuff
# . Keep the list saved in a file (JSON format)


# We'll start by writing out the functions: 

# Add task function:

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

# View all tasks function: 

# We should handle the case where the list is either empty or doesn't exist.

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


#Clear all tasks

#Users can't clear tasks of a list that doesn't exist.
#Add a confirmation


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



#Clear a specific task
#Users should first view all their tasks enumerated, then choose which task to be deleted.

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


#Mark tasks as done. 
#Users should first see their tasks enumerated, then choose which task to be marked as done --> a better version of this is 
# to ask the users for multiple indices in case they wanted to mark multiple tasks, so that they wouldn't have to go back
# to the options list again each time they want to mark a task as done.

def mark_done():
    try:
        view_tasks()
        with open ("to_do_list.txt", "r") as file:
            tasks = file.readlines()
            if not(tasks):
                print("\nYour list is empty.")
                return 
            while True:
                try:
                    task_indices = input("\nEnter the numbers associated with the tasks you want marked as done (comma separated): ") # eg: 1, 3, 4
                    task_indices = [int(index.strip()) for index in task_indices.split(",")] # task_indices.split(",") results in an array containing strings ["1", " 3", " 4"]
                                                                                            # int(index.strip()) takes each string in task_indices and removes whitespaces and turns it into an integer
                                                                                                                                                                                # [1, 3, 4]
                    if all (1 <= index <= len(tasks) for index in task_indices):
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

#Main function (or the user's interface):

def main():
    while True:
        """TO-DO List APP"""

        """Add a task (1)"""
        """View all tasks (2)"""
        """Clear all tasks (3)"""
        """Clear a specific task (4)"""
        """Mark tasks as done (5)"""
        """Quit (6)"""

        
        print("\n**TO-DO List APP**")
        print("1. Add a task")
        print("2. View all tasks")
        print("3. Clear all tasks")
        print("4. Clear a specifc task")
        print("5. Mark tasks as done")
        print("6. Exit")

        choice = input("Choose an option: ")

        if (choice == "1"):
            add_task()
    
        elif (choice == "2"):
            view_tasks()

        elif (choice == "3"):
            clear_all_tasks()
        
        elif (choice == "4"):
            clear_task()
        
        elif (choice == "5"):
            mark_done()
        
        elif (choice == "6"):
            print("Goodbye!")
            break
        else:
            print("Invalid option, please choose a valid option.")


if __name__ == "__main__":
    main()
    























