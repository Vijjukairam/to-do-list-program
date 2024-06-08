tasks = []

def add_task():
  task = input("Enter a new task: ")
  tasks.append(task)
  print("Task added!")

def view_tasks():
  if tasks:
    for i, task in enumerate(tasks):
      print(f"{i+1}. {task}")
  else:
    print("No tasks added yet!")

def mark_done():
  if tasks:
    for i, task in enumerate(tasks):
      print(f"{i+1}. {task}")
    choice = int(input("Enter the number of the task to mark as done: ")) - 1
    if 0 <= choice < len(tasks):
      tasks.pop(choice)
      print("Task marked done!")
    else:
      print("Invalid task number!")
  else:
    print("No tasks to mark done!")

def exit_program():
  print("Exiting to-do list.")
  exit()

while True:
  print("\nTo-Do List")
  print("1. Add Task")
  print("2. View Tasks")
  print("3. Mark Task Done")
  print("4. Exit")
  choice = input("Enter your choice: ")

  if choice == '1':
    add_task()
  elif choice == '2':
    view_tasks()
  elif choice == '3':
    mark_done()
  elif choice == '4':
    exit_program()
  else:
    print("Invalid choice. Please try again.")
