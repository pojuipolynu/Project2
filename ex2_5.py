class Student:
    def __init__(self, name, surname, rbn, grades):
        self.name = name
        self.surname = surname
        self.rbn = rbn
        self.grades = grades


class Group:
    def high_grade(self, grade):
        high = [0 for x in range(len(grade))]
        for x, i in enumerate(grade):
            high[x] = [round(sum(i.grades)/len(i.grades), 2), f'Student: {i.surname} {i.name[0]}.']
        high.sort(reverse=True)
        return high

    def stud_info(self, grade):
        k = ''
        b = self.high_grade(grade)
        for x in range(5):
            k += f'{b[x][1]}\nAverage score: {b[x][0]}\n'
        return k


students = []
students.append(Student('Yulia', 'Ponomareva', '3905798684', (2, 4, 6, 1, 34, 6)))
students.append(Student('Lesyk', 'Teliha', '23009459884', (3, 4, 12, 1, 4, 7)))
students.append(Student('Nastusia', 'Ponomareva', '03457-034484', (3, 11, 0, 3, 3, 23)))
students.append(Student('Anna', 'Schwetc', '320957301', (12, 41, 0, 0, 2, 6)))
students.append(Student('Katria', 'Zhuk', '128349875', (1, 6, 6, 7, 22, 4)))
students.append(Student('Tia', 'Nailo', '973658902', (11, 0, 16, 23, 45, 0)))
grad = Group()
print(grad.stud_info(students))
