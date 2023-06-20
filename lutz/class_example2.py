"""В качестве примера предположим,
что вам поручили реализовать приложение с базой данных сотрудников."""


class Employee:
    def computeSalary(self): print('computeSalary in Employee')

    def giveRaise(self): ...

    def promote(self): ...

    def retire(self): ...


class Engineer(Employee):
    def computeSalary(self): print('computeSalary in Engineer')


bob = Employee()
sue = Employee()
tom = Engineer()

company = [bob, sue, tom]
for emp in company:
    print(emp.computeSalary())
