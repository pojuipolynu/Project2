class Student:
    def __init__(self, name, surname, rbn, grades):
        self.name = name
        self.surname = surname
        self.rbn = rbn
        self.grades = grades
        self.average = 0

    def __str__(self):
        return f'Student: {self.surname} {self.name[0]}\nRecord book number: {self.rbn}\nGrades: {self.grades} '


class Group:
    def __init__(self):
        self.student = []

    def add_stud(self, a):
        if not isinstance(a, Student) or a in self.student:
            raise Exception('Given information is invalid')
        elif len(self.student) > 20:
            raise Exception('Group can contain no more than twenty students')
        else:
            self.student.append(a)
        return self.student

    def high_grade(self):
        for x in self.student:
            x.average = round(sum(x.grades)/len(x.grades), 2)
        self.student.sort(key=lambda a: a.average, reverse=True)
        return self.student[:5]

    def print_score(self):
        for x in self.high_grade():
            print(x, '\nAverage score:', x.average, '\n')


student1 = Student('Yulia', 'Ponomareva', '3905798684', (2, 4, 6, 1, 34, 6))
student2 = Student('Lesyk', 'Teliha', '23009459884', (3, 4, 12, 1, 4, 7))
student3 = Student('Nastusia', 'Ponomareva', '03457-034484', (3, 11, 0, 3, 3, 23))
student4 = Student('Anna', 'Schwetc', '320957301', (12, 41, 0, 0, 2, 6))
student5 = Student('Katria', 'Zhuk', '128349875', (1, 6, 6, 7, 22, 4))
student6 = Student('Tia', 'Nailo', '973658902', (11, 0, 16, 23, 45, 0))
group = Group()
group.add_stud(student1)
group.add_stud(student2)
group.add_stud(student3)
group.add_stud(student4)
group.add_stud(student5)
group.add_stud(student6)
print(group.print_score())
