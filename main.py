import os
import questionary
from task import Task

os.system("clear")

todo_list = []

#Test
task_1 = Task("fasdf", "djfkasdf", "djfgkasdjg")
task_2 = Task("áaaaaa", "bbbbb", "ccccc")
todo_list.append(task_1)
todo_list.append(task_2)
#

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
    for task in todo_list:
      print("\n")
      task.get_data()

def show_todo_list_names():
  for task in todo_list:
    print("\n")
    print(task.name)

def main_menu():
  while True:
    print("\n")
    choice = questionary.select (
      "Terminal Todo Menu",
      choices = [
        "1. Check todo list",
        "2. Add task",
        "3. Edit task",
        "Exit"
      ]
    ).ask()

    if choice == "1. Check todo list":
      show_todo_list_data()
    elif choice == "2. Add task":
      create_task()
    elif choice == "3. Edit task":
      show_todo_list_names()
    elif choice == "Exit":
      print("Exiting the program")
      break
    else:
      print("Invalid choice")

def edit_menu(task_list):
  new_list = [f"{i +1 }. {x}" for i, x in enumerate(task_list)]
  new_list.append("Exit")
  while True:
    #print("\n")
    choice = questionary.select (
      "Select the task to edit",
      choices = new_list
    ).ask()

    if choice == "Exit":
      print("Exiting the menu...")
      break
    else:
      task_index = int(choice.split(".")[0]) - 1
      #print(test_list)
      print(f"task selected: {task_index}")


def edit_menu_test(todo_list):
  while True:
    task_names_list = [f"{i + 1}.{x.name}" for i, x in enumerate(todo_list)]
    task_names_list.append("Exit")

    choice = questionary.select(
      "Select the task you want to edit",
      choices = task_names_list
    ).ask()

    if choice == "Exit":
      print("Exiting the program...")
      break
    else:
      task_index = int(choice.split(".")[0]) - 1
      task_data = [
        f"Name: {todo_list[task_index].name}",
        f"Description: {todo_list[task_index].description}",
        f"Status: {todo_list[task_index].state}",
        "Exit"
      ]

      action = questionary.select(
        "Choose what you want to edit",
        choices = task_data
      ).ask()

      task_detail = action.split(":")[0]
      if task_detail == "Name":
        print("you selected name")
        user_input = questionary.text("Enter new name: ").ask()
        todo_list[task_index].name = user_input

      elif task_detail == "Description":
        user_input = questionary.text("Enter new description: ").ask()
        todo_list[task_index].description = user_input
        print("changes applied successfully")

      elif task_detail == "Status":
        user_input = questionary.text("Write new status: ").ask()
        todo_list[task_index].state = user_input
        print("changes applied successfully")

      #print(task_data)

      #print("Task data")
      #print(todo_list[task_index].name)
      #print(todo_list[task_index].description)

#edit_menu(test_list_name)
#main_menu()

edit_menu_test(todo_list)