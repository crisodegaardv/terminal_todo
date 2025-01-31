def delete_task_menu(tasks: list[Task]) -> None:
  while True:
    todo_list_names = [f"{index + 1}.{task.name}" for index, task in enumerate(tasks)]
    todo_list_names.append("Exit")

    choice = questionary.select(
      message="Choose which task would you like to delete",
      choices=todo_list_names
    ).ask()

    if choice == "Exit":
      print("Exiting delete menu...")
      break
    else:
      task_name = choice.split(".", 1)[1]  # Extracts the task name correctly
      delete_task(task_name, tasks)
      print("Task deleted")