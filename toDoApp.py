# TO-DO list script 

# App Overview:

# 1. Add tasks to a to-do list
# 2. View all tasks
# 3. Clear all tasks
# 4. Keep the list saved in a file


# the users see four options: 
    # 1. Add a task (should click the number 1)
    # 2. View all tasks (should click the number 2)
    # 3. Clear all tasks (should click the number 3)
    # 4. Clear a specific task (should click number 4)
    # 5. Mark tasks as done (should click number 5)
    # 6. Quit (should click the number 6)

# We'll start by writing out the functions: 

# Add task function:

def add_task():
    """Add a task to your list"""
    task = input("Enter the task you want to add: ")
    with open("to_do_list.txt", "a") as file:
        file.write(task + "\n")
    print("Task added successfully.")


# View all tasks function: 

# We should handle the case where the list is either empty or doesn't exist.

def view_tasks():
    """View all tasks you added"""
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


#Clear all tasks

#Users can't clear tasks of a list that doesn't exist.
#Add a confirmation


def clear_all_tasks():
    try:
        confirm = input("Are you sure you want to clear all tasks? (y/n): ").lower()
        if confirm == "y":
            with open("to_do_list.txt", "r") as file:
                tasks = file.readlines()
                if not(tasks):
                    print("\nYour list is already empty.")
                else:
                    open("to_do_list.txt", "w").close()
                    print("\nAll tasks are cleard.")
        else:
            print("\nClear operation canceled.")
    except FileNotFoundError:
        print("\nNo to-do list was found.")



#Clear a specific task
#Users should first view all their tasks enumerated, then choose which task to be deleted.

def clear_task():
    try:
        view_tasks()
        with open("to_do_list.txt", "r") as file:
            tasks = file.readlines()
            if (not(tasks)):
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
    























