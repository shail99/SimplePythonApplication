from collections import defaultdict


class Employee(object):
    def __init__(self, id, name, manager_id):
        self.id = id
        self.name = name
        self.manager_id = manager_id
        self.employees = []


class OrgChartSol1(object):
    def __init__(self):
        self.employees = []
        self.employee_map = defaultdict(Employee)
        self.manager_to_employee_map = defaultdict(list)

    '''
    @Name: add
    @Input: employee_id : String
            name : String
            manager_id : String
    Adds an employee under his direct report 
    '''
    def add(self, id, name, manager_id):
        new_employee = Employee(id, name, manager_id)
        self.employee_map[int(id)] = new_employee
        self.manager_to_employee_map[int(manager_id)].append(int(id))

        if int(manager_id) == -1:
            self.employees.append(self.employee_map.get(int(id)))
        else:
            if self.employee_map.__contains__(int(manager_id)):
                self.employee_map[int(manager_id)].employees.append(self.employee_map.get(int(id)))

        # check for his direct reports in case they were added earlier before the manager
        if self.manager_to_employee_map.__contains__(int(id)):
            list_of_direct_reports = self.manager_to_employee_map[int(id)]
            for direct_report in list_of_direct_reports:
                self.employee_map[int(id)].employees.append(self.employee_map[int(direct_report)])
    '''
    @Name: remove
    @Input: employee_id : String
    Removes an employee from the hierarchy and any direct reports under him will report to the removed employees manager
    '''
    def remove(self, id):
        # Get the removed employees manager in order to update his list of direct reports
        manager_for_removed_employee = int(self.employee_map[int(id)].manager_id)
        employee_list_to_update = self.employees if int(manager_for_removed_employee) == -1 else self.employee_map[int(manager_for_removed_employee)].employees

        # Remove from the employee list of his manager
        # Also remove the employee from his manager's direct reports
        employee_list_to_update.remove(self.employee_map[int(id)])
        self.manager_to_employee_map[manager_for_removed_employee].remove(int(id))

        # Update the removed employees direct reports to reflect the new manager
        # Add the direct report's of the removed manager to the new manager's direct report list
        # Also add the removed employees direct reports to the new manager direct reports
        for direct_report in self.manager_to_employee_map[int(id)]:
            self.employee_map[direct_report].manager_id = self.employee_map[int(id)].manager_id
            employee_list_to_update.append(self.employee_map[int(direct_report)])
            self.manager_to_employee_map[manager_for_removed_employee].append(int(direct_report))

        del self.employee_map[int(id)]
        del self.manager_to_employee_map[int(id)]

    def print(self):
        self.print_employees(self.employees, '')

    def print_employees(self, employees, padding):
        for e in employees:
            print(padding + e.id + ", " + e.name)
            self.print_employees(e.employees, padding + ' ')


if __name__ == '__main__':
    organization = OrgChartSol1()
    input = "2,Dan,3\n12,Shailesh,-1\n3,Robert,12\n4,Hozefa,-1\n7,Jack,-1\n8,Nick,4\n9,Brandon,12\n11,Charu,12\n55,Sumit,3"
    for line in input.splitlines():
        employee_info = line.split(',')
        organization.add(employee_info[0], employee_info[1], employee_info[2])

    organization.add("15", "Ed", "99")
    organization.add("16", "Ralph", "15")
    organization.add("99", "Brian", "-1")
    organization.print()
    organization.remove("3")
    print("After deletion")
    organization.print()
    print("Check Values")
    print(organization.manager_to_employee_map)
