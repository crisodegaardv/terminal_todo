import questionary

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
    print(todo_list)
  #elif choice == "2":

  elif choice == "Exit":
    print("Exiting the program")
    break
  else:
    print("Invalid choice")

