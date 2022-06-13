class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.lecturer_grades:
                lecturer.lecturer_grades[course] += [grade]
            else:
                lecturer.lecturer_grades[course] = [grade]
        else:
            return 'Ошибка'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    lecturer_grades = {}

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

Oleg = Lecturer("Олег", "Булыгин")
Oleg.courses_attached += ['Python', 'Java']

Alex = Reviewer("Александр","Бардин")
Alex.courses_attached += ['Python']

best_student = Student('Иван', 'Иванов', 'муж')
best_student.courses_in_progress += ['Python']
best_student.rate_lecturer(Oleg,'Python', 9)

Alex.rate_hw(best_student, 'Python', 8)

print(f'{best_student.surname} {best_student.name} - оценка за д/з по {best_student.grades}')
print(f'{Oleg.surname} {Oleg.name} - оценка за лекцию по {Oleg.lecturer_grades}')