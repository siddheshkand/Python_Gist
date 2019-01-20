from operator import attrgetter


def sort_in_list_tuple():
    # Sort all different types of object
    li = [9, 1, 8, 2, 7, 3, 6, 4, 5]
    tu = (9, 1, 8, 2, 7, 3, 6, 4, 5)  # tuple does not have sort() method
    s_li = sorted(li, reverse=True)

    print("Unsorted list " + str(li))
    print("Sorted list " + str(s_li))

    # Sort without creating new variable

    print("li Before" + str(li))
    li.sort(reverse=True)  # inplace modify i.e. it sort li in same array do not return sorted list
    print("li After" + str(li))


def sort_dict_simple():
    # SORTING IN DICT
    di = {"name": "sid", "age": 21, "favorite os": "Ubuntu"}
    print("di Before" + str(di))
    s_di = sorted(di)  # return list of keys in dict in alphabetical order Capital letters, then Small
    print("s_di After" + str(s_di))


def absolute_value_sort():
    # ABSOLUTE VALUE SORT
    li = [-6, -5, -4, 1, 2, 3]
    s_li = sorted(li, key=abs)
    print(s_li)


class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return "{} {}, ${}".format(self.name, self.age, self.salary)


e1 = Employee('Carl', 27, 70000)
e2 = Employee('Mark', 25, 65000)
e3 = Employee('Jone', 22, 40000)

employees = [e1, e2, e3]


def e_sort_name(emp):
    return emp.name


def e_sort_age(emp):
    return emp.age


def e_sort_salary(emp):
    return emp.salary


s_employees = sorted(employees, key=e_sort_name)
# OR
s_employees_lambda = sorted(employees, key=lambda e: e.age, reverse=True)
# OR
s_employees_attrgetter = sorted(employees, key=attrgetter('salary'))

print(s_employees)
print(s_employees_lambda)
print(s_employees_attrgetter)

