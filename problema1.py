 
import pandas
class Employee:
    """Common base class for all employees"""
    
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tasks = {}
        Employee.empCount += 1

    def display_emp_count(self):
        "Displays the number of employees"
        print(f"Total number of employee(s) is {Employee.emp_count}")

    def display_employee(self):
        print("Salary: ", self.salary)

    def __del__ (self):
        Employee.empCount -=1

    def update_salary(self, new_salary):
        self.salary = new_salary


    def modify_task(self, task_name, status="New"):
        self.tasks[task_name]=status

    def display_task(self, status):
        print(f"Taskuri cu statusul {status}")
        for name in self.tasks.keys():
            if self.tasks[name] == status:
                print(name)

## x = 7 => x % 3 = 1
class Manager(Employee):
    mgr_count = 0
    
    def __init__(self,name,salary):
        super().__init__(name,salary)
        self.department='F21'
        Manager.mgr_count+=1
        
    def display_employee(self):
        print("Salary:" ,self.salary)

##Y = 14 => 4        

manager1 = Manager("Nastase Magda",10050)
manager2 = Manager("Dan Andrei",37)
manager3 = Manager("Munteanu Denisa",18)
manager4 = Manager("Burcea Valentin",7)

Manager.display_employee(manager1)
Manager.display_employee(manager2)
Manager.display_employee(manager3)
Manager.display_employee(manager4)
print(Manager.mgr_count)

print('\n')


employee1 = Employee('John Doe',10001)
employee2 = Employee('Jane Doe',20002)
employee3 = Employee("Peter Griffin",50005)
employee4 = Employee("Homer Simpson",5005)


employee1.display_employee()
employee2.display_employee()
employee3.display_employee()
employee4.display_employee()
print(Employee.empCount)