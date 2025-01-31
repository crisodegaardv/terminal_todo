import os
import questionary
from task import Task

os.system("clear")

todo_list = []

#Test
task_1 = Task("Study", "French", "On progress")
task_2 = Task("áaaaaa", "bbbbb", "ccccc")
todo_list.append(task_1)
todo_list.append(task_2)
#

def create_task() -> None:
  new_task = Task(
    questionary.text("Task name: ").ask(),
    questionary.text("Task description: ").ask(),
    questionary.text("Task status: ").ask()
  )

  todo_list.append(new_task)

def show_todo_list_data() -> None:
  if len(todo_list) == 0:
    print("No tasks")
  else:
    for task in todo_list:
      print("\n")
      task.get_data()

def main_menu() -> None:
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
      edit_menu(todo_list)
    elif choice == "Exit":
      print("Exiting the program")
      break
    else:
      print("Invalid choice")

def edit_menu(tasks: list[Task]) -> None:
  while True:
    task_names_list = [f"{i + 1}.{x.name}" for i, x in enumerate(todo_list)]
    task_names_list.append("Exit")

    choice = questionary.select(
      message = "Select the task you want to edit",
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

def delete_task(task: list[Task]) -> None:
  while True:
    todo_list_names = [f"{index + 1}.{task.name}" for index, task in enumerate(task)]
    todo_list_names.append("Exit")

    choice = questionary.select(
      message = "Choose which task would you like to delete",
      choices = todo_list_names
    ).ask()

    if choice == "Exit":
      break
    else:
      print(choice)


#edit_menu(test_list_name)
#main_menu()

#edit_menu_test(todo_list)
#main_menu()
delete_task(todo_list)