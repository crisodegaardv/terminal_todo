import uuid

class Task:
  def __init__(self, name, description, state):
    self.id = uuid.uuid4()
    self.name = name
    self.description = description
    self.state = state

  def get_data(self):
    print(f"Task id: {self.id} \nTask name: {self.name} \nTask description {self.description} \nTask state: {self.state}")


