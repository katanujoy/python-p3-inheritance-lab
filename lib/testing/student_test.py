# test_student.py
from student import Student
from user import User

class TestStudent:
    '''Class "Student" in student.py'''

    def test_is_subclass(self):
        '''is a subclass of "User".'''
        # Check if Student is a subclass of User
        assert(User in Student.__bases__)

    def test_initializes_with_names(self):
        '''initializes with first and last name.'''
        my_student = Student("My", "Student")
        # Assert that the first and last names match
        assert((my_student.first_name, my_student.last_name) == ("My", "Student"))

    def test_initializes_with_knowledge(self):
        '''initializes with empty list attribute "knowledge".'''
        my_student = Student("My", "Student")
        # Assert that the "knowledge" attribute exists
        assert(hasattr(my_student, "knowledge"))

    def test_can_learn(self):
        '''learns from a string and adds to self.knowledge.'''
        my_student = Student("My", "Student")
        my_student.learn("New information")
        # Assert that "New information" is added to knowledge
        assert("New information" in my_student.knowledge)
