# from collections import defaultdict
#
#
# class OrgChart(object):
#     def __init__(self):
#         self.employees = []
#         self.employee_map = defaultdict(Employee)
#         self.manager_to_employee_map = defaultdict(list)
#
#     def build_employee_map(self, id, name, manager_id):
#         employee = Employee(id, name, manager_id)
#         self.employee_map[int(id)] = employee
#
#         if self.manager_to_employee_map.__contains__(int(manager_id)):
#             self.manager_to_employee_map[int(manager_id)].append(int(id))
#         else:
#             self.manager_to_employee_map[int(manager_id)] = [int(id)]
#
#     def add(self, id, name, manager_id):
#         if not self.employee_map.__contains__(int(id)):
#             self.employee_map[int(id)] = Employee(id, name, manager_id)
#
#         if int(manager_id) == -1:
#             self.employees.append(self.employee_map.get(int(id)))
#         else:
#             if self.employee_map.__contains__(int(manager_id)):
#                 self.employee_map[int(manager_id)].employees.append(self.employee_map.get(int(id)))
#
#     def print(self):
#         self.print_employees(self.employees, '')
#
#     def print_employees(self, employees, padding):
#         for e in employees:
#             print(padding + e.id + ", " + e.name)
#             self.print_employees(e.employees, padding + ' ')
#
#
# class Employee(object):
#     def __init__(self, id, name, manager_id):
#         self.id = id
#         self.name = name
#         self.manager_id = manager_id
#         self.employees = []
#
#
# if __name__ == '__main__':
#     organization = OrgChart()
#     input = "2,Dan,3\n12,Shailesh,-1\n3,Robert,12\n4,Hozefa,-1\n7,Jack,-1\n8,Nick,4\n9,Brandon,12\n11,Charu,12"
#     for line in input.splitlines():
#         employee_info = line.split(',')
#         organization.build_employee_map(employee_info[0], employee_info[1], employee_info[2])
#
#     for employee_id, employee in organization.employee_map.items():
#         organization.add(employee.id, employee.name, employee.manager_id)
#
#     organization.add("99", "Brian", "-1")
#     organization.add("15", "Ed", "99")
#     organization.add("16", "Ralph", "15")
#
#
#     organization.print()
