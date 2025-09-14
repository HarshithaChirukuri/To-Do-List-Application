import os
import json

FILENAME = "tasks.json"

# Load tasks from JSON file
def load_tasks():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r") as file:
        return json.load(file)

# Save tasks to JSON file
def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        json.dump(tasks, file)

# Show all tasks
def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.\n")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            status = "✅" if task["completed"] else "❌"
            print(f"{i}. {task['title']} [{status}]")
        print()

# Add a new task
def add_task(tasks):
    task_title = input("Enter a new task: ")
    tasks.append({"title": task_title, "completed": False})
    save_tasks(tasks)
    print("✅ Task added successfully!\n")

# Delete a task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        choice = int(input("Enter task number to delete: "))
        if 1 <= choice <= len(tasks):
            removed = tasks.pop(choice - 1)
            save_tasks(tasks)
            print(f"🗑️ Task '{removed['title']}' deleted.\n")
        else:
            print("❌ Invalid task number.\n")
    except ValueError:
        print("❌ Please enter a valid number.\n")

# Mark a task as completed
def complete_task(tasks):
    view_tasks(tasks)
    try:
        choice = int(input("Enter task number to mark as completed: "))
        if 1 <= choice <= len(tasks):
            tasks[choice - 1]["completed"] = True
            save_tasks(tasks)
            print(f"✔️ Task '{tasks[choice - 1]['title']}' marked as completed!\n")
        else:
            print("❌ Invalid task number.\n")
    except ValueError:
        print("❌ Please enter a valid number.\n")

# Main program loop
def main():
    tasks = load_tasks()
    while True:
        print("==== TO-DO LIST APP ====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Mark Task as Completed")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            complete_task(tasks)
        elif choice == "5":
            print("Goodbye! 👋")
            break
        else:
            print("❌ Invalid option, try again.\n")

if __name__ == "__main__":
    main()
