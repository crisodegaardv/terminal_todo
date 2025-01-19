import os
import questionary
from task import Task

os.system("clear")

todo_list = []

def create_task():
  new_task = Task(
    questionary.text("Task name: ").ask(),
    questionary.text("Task description: ").ask(),
    questionary.text("Task status: ").ask()
  )

  todo_list.append(new_task)

def show_todo_list_data():
  if len(todo_list) == 0:
    print("No tasks")
  else:
    for i in todo_list:
      print("\n")
      i.get_data()
      print("\n")

while True:
  choice = questionary.select (
    "Terminal Todo Menu",
    choices = [
      "1. Check todo list",
      "2. Add task",
      "Exit"
    ]
  ).ask()

  if choice == "1. Check todo list":
    show_todo_list_data()
  elif choice == "2. Add task":
    create_task()
  elif choice == "Exit":
    print("Exiting the program")
    break
  else:
    print("Invalid choice")


