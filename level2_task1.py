import json
import os

FILE_NAME = "todo_data.json"

class ToDoApp:
    def __init__(self):
        self.tasks = self._load_tasks()

    def _load_tasks(self):
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, "r") as f:
                return json.load(f)
        return []

    def _save_tasks(self):
        with open(FILE_NAME, "w") as f:
            json.dump(self.tasks, f, indent=2)

    def add(self, task_text):
        self.tasks.append({"title": task_text, "completed": False})
        self._save_tasks()
        print(f"Added: {task_text}")

    def show(self):
        if not self.tasks:
            print("No tasks yet.")
            return
        print("\n--- Current Tasks ---")
        for idx, task in enumerate(self.tasks, start=1):
            status = "✓" if task["completed"] else "✗"
            print(f"{idx}. {task['title']} [{status}]")
        print()

    def remove(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            removed = self.tasks.pop(task_number - 1)
            self._save_tasks()
            print(f"Deleted: {removed['title']}")
        else:
            print("Invalid task number.")

    def mark_done(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True
            self._save_tasks()
            print(f"Marked as done: {self.tasks[task_number - 1]['title']}")
        else:
            print("Invalid task number.")

def run():
    app = ToDoApp()
    while True:
        print("\nOptions: 1-Add | 2-List | 3-Delete | 4-Done | 5-Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            text = input("Task description: ")
            app.add(text)
        elif choice == "2":
            app.show()
        elif choice == "3":
            app.show()
            try:
                num = int(input("Task number to delete: "))
                app.remove(num)
            except ValueError:
                print("Enter a valid number.")
        elif choice == "4":
            app.show()
            try:
                num = int(input("Task number to mark done: "))
                app.mark_done(num)
            except ValueError:
                print("Enter a valid number.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    run()
