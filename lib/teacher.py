# teacher.py
from user import User

class Teacher(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = ["Teaching method 1", "Teaching method 2"]

    def teach(self):
        # The method that returns knowledge the teacher teaches
        return self.knowledge[0]
