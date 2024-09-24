tasks = []
def add_task(task):
    tasks.append({"task": task, "status": "pending"})
    print(f'Task "{task}" added.')
def display_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task['task']} - {task['status']}")
def remove_task(index):
    try:
        removed_task = tasks.pop(index - 1)
        print(f'Task "{removed_task["task"]}" removed.')
    except IndexError:
        print("Invalid index. Please try again.")
def mark_task_completed(index):
    try:
        tasks[index - 1]["status"] = "completed"
        print(f'Task "{tasks[index - 1]["task"]}" marked as completed.')
    except IndexError:
        print("Invalid index. Please try again.")
while True:
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. Display Tasks")
    print("3. Remove Task")
    print("4. Mark Task as Completed")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        task = input("Enter the task: ")
        add_task(task)
    elif choice == "2":
        display_tasks()
    elif choice == "3":
        index = int(input("Enter the task index to remove: "))
        remove_task(index)
    elif choice == "4":
        index = int(input("Enter the task index to mark as completed: "))
        mark_task_completed(index)
    elif choice == "5":
        print("Exiting the application. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
