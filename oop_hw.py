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

    def stud_av_grade(self):
        stud_average_grade = 0
        for course, grade in self.grades.items():
            for mark in grade:
                stud_average_grade += mark
        result = stud_average_grade / len(grade)
        return result 
    
    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Не могу сравнивать с не студентами!')
            return
        return self.stud_av_grade() < other.stud_av_grade()    

    def __str__(self):
        res = (f'Имя: {self.name} \nФамилия: {self.surname}\n'
        f'Курсы в процессе изучения: {" ".join(best_student.courses_in_progress)}\n'
        f'Средняя оценка за домашние задания: {self.stud_av_grade()} \nЗавершенные курсы: {" ".join(self.finished_courses)}')
        return res

    
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname) 
        self.lecturer_grades = {}   

    def av_grade(self):
        average_grade = 0
        for course, grades in self.lecturer_grades.items():
            for mark in grades:
                average_grade += mark
        result = average_grade / len(grades)
        return result
    
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Не могу сравнивать с не лекторами!')
            return
        return self.av_grade() < other.av_grade()

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}\nСредняя оценка за лекции: {self.av_grade()}'
        return res


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res


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