import questionary

new_task_template = {
  "id": None,
  "task_name": None,
  "task_description": None,
  "task_state": None
}

todo = [
  {
    "id": 1,
    "task_name": "program",
    "task_description": "program a to do list",
    "task_state": "ongoing"
  }
]

print(todo)


question = questionary.text("write your task details here: ")
new_task_template["task_name"] = questionary.text("Write task name here: ").ask()
new_task_template["task_description"] = questionary.text("Write task description here: ").ask()
new_task_template["task_state"] = questionary.text("Write task state here: ").ask()


print(new_task_template)