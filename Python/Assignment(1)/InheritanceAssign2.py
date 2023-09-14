# Implement a class hierarchy for different types of employees in an organisation using inheritance

class Hierarchy:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def print(self):
        pass


class Executive(Hierarchy):
    def __init__(self, name, emp_id, head):
        super().__init__(name, emp_id)
        self.head = head

    def print(self):
        print(f"{self.name} is chief {self.head} officer with employee id {self.emp_id}")


class Manager(Hierarchy):
    def __init__(self, name, emp_id, dept):
        super().__init__(name, emp_id)
        self.dept = dept

    def print(self):
        print(f"{self.name} is an {self.dept} manager with employee id {self.emp_id}")


class EntryLevel(Hierarchy):
    def __init__(self, name, emp_id, job):
        super().__init__(name, emp_id)
        self.job = job

    def print(self):
        print(f"{self.name} is an {self.job} with employee id {self.emp_id}")


obj1 = Executive("Alice", "EX001", "Executive")
obj2 = Manager("Bob", "MN001", "IT")
obj3 = EntryLevel("Carol", "EL001", "Software Engineer")

obj1.print()
obj2.print()
obj3.print()
