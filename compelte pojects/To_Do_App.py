
class TodoApp:
    def __init__(self):
        self.tasks = []

    # CREATE
    def add_task(self):
        task = input("Enter task: ")
        self.tasks.append(task)
        print("Task added successfully!")

    # READ
    def show_tasks(self):
        if len(self.tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")

            for number, task in enumerate(self.tasks, start=1):
                print(number, task)

    # UPDATE
    def update_task(self):
        self.show_tasks()

        if len(self.tasks) > 0:
            number = int(input("Enter task number: "))

            if number >= 1 and number <= len(self.tasks):
                new_task = input("Enter new task: ")
                self.tasks[number - 1] = new_task
                print("Task updated successfully!")
            else:
                print("Invalid task number.")

    # DELETE
    def delete_task(self):
        self.show_tasks()

        if len(self.tasks) > 0:
            number = int(input("Enter task number to delete: "))

            if number >= 1 and number <= len(self.tasks):
                self.tasks.pop(number - 1)
                print("Task deleted successfully!")
            else:
                print("Invalid task number.")

    # MENU
    def run(self):
        while True:
            print("\n===== TO-DO APP =====")
            print("1. Add Task")
            print("2. Show Tasks")
            print("3. Update Task")
            print("4. Delete Task")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_task()

            elif choice == "2":
                self.show_tasks()

            elif choice == "3":
                self.update_task()

            elif choice == "4":
                self.delete_task()

            elif choice == "5":
                print("Thank you for using To-Do App!")
                break

            else:
                print("Invalid choice. Try again.")


app = TodoApp()
app.run()