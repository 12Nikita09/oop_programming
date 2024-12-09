#from pprint import pprint
#from asd import students


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = [] # завершенные курсы студента
        self.courses_in_progress = [] # курсы в процессе изучения студентом
        self.grades = {} # словарь,в котором хранятся оценки студента за Д/З

    # lecturer - Это экземпляр класса Lecturer
    # course - Это входящий курс (типа Python)
    # grade - Оценка (10)
    # isinstance(lecturer, Lecturer) - Проверяем, что пришел экземпляр класса Lecturer
    # course in lecturer.courses_attached - Проверяем, что Входящий курс существует в списке курсов лектора
    # course in self.courses_in_progress - Проверяем, что Входящий курс существует в списке начатых курсов у студента

    # Метод по выставлению оценок студентами лектору за лекции
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __eq__(self, other_student):
        return self.average_rate() == other_student.average_grade_lecturer()

    #Метод по высчитыванию средней оценки за домашнее задание
    def average_rate(self):
        sum_rate = 0
        amount = 0
        for grades in self.grades.values():
            if len(self.grades) > 0:
                sum_rate += sum(grades)
                amount += len(grades)
                result = sum_rate / amount
            else:
                result = 0

            return  result

    def __str__(self):
        return (f' Имя Студента: {self.name} \n'
                f' Фамилия Студента: {self.surname} \n'
                f' Средняя оценка за домашнее задание {self.average_rate()} \n'
                f' Курсы в процессе изучения: {", ".join(self.courses_in_progress)} \n'
                f' Завершенные курсы: {self.finished_courses}')

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    grades = {}

    # Метод по высчитыванию средней оценки за лекции
    def average_grade_lecturer(self):
        sum_grade = 0
        len_rate = 0
        for grades in self.grades.values():
            if len(self.grades) > 0:
                sum_grade += sum(grades)
                len_rate += len(grades)
                result = sum_grade / len_rate
            else:
                result = 0

            return result

    def __eq__(self, other_lecturer):
        return self.average_grade_lecturer() == other_lecturer.average_rate()

    def __str__(self):
        return (f' Имя Лектора: {self.name} \n'
                f' Фамилия Лектора: {self.surname} \n'
                f' Средняя оценка за лекции: {self.average_grade_lecturer()}')

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    # Метод по выставлению оценок ревьюером студенту за домашнее задание
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f' Имя Ревьюера: {self.name} \n '
                f'Фамилия Ревьера: {self.surname}')


def average_all_student(students, course):
    sum_rate = 0
    len_rate = 0
    for student in students:
        if course in student.grades:
            sum_rate += sum(student.grades[course])
            len_rate += len(student.grades[course])
    if len_rate > 0:
        result = sum_rate / len_rate
    else:
        result = 0
    return result

def average_all_lecturer(lecturers, course):
    sum_rate = 0
    len_rate = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            sum_rate += sum(lecturer.grades[course])
            len_rate += len(lecturer.grades[course])
    if len_rate > 0:
        result = sum_rate / len_rate
    else:
        result = 0
    return result


# экземпляр класса Студент 1
best_student = Student('Raya', 'Garcia', 'M')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Java']

#Экземпляр класса Лектор 1
lecturer = Lecturer('Ivan', 'Ivanov')
lecturer.courses_attached += ['Python']
lecturer.courses_attached += ['Git']

# экземпляр класса Ревьюера
reviewer = Reviewer('Petya', 'Petrov')
reviewer.courses_attached += ['Python']
reviewer.courses_attached += ['Git']

# выставление оценок Ревюьером 1 Студенту 1 за домашнее задание по Питону
reviewer.rate_hw(best_student, 'Python', 10)
reviewer.rate_hw(best_student, 'Python', 9)
reviewer.rate_hw(best_student, 'Python', 7)
reviewer.rate_hw(best_student, 'Git', 10)
reviewer.rate_hw(best_student, 'Git', 9)
reviewer.rate_hw(best_student, 'Git', 7)
print(best_student)

# Оценка Студента Лектору за лекцию по Питону
best_student.rate_lecturer(lecturer, 'Python', 10)
best_student.rate_lecturer(lecturer, 'Python', 3)
best_student.rate_lecturer(lecturer, 'Python', 5)
best_student.rate_lecturer(lecturer, 'Git', 10)
best_student.rate_lecturer(lecturer, 'Git', 8)
best_student.rate_lecturer(lecturer, 'Git', 8)

print(lecturer)


# экземпляр класса Студент 2
best_student2 = Student('Semen', 'Semenov', 'M')
best_student2.courses_in_progress += ['Git']
best_student2.courses_in_progress += ['Python']
best_student2.finished_courses += ['Java']

# Экземпляр класса Лектор 2
lecturer1 = Lecturer('Kolya', 'Kolyanov')
lecturer1.courses_attached += ['Git']
lecturer1.courses_attached += ['Python']

# экземпляр класса Ревьюера2
reviewer2 = Reviewer('Nikita', 'Nikitin')
reviewer2.courses_attached += ['Git']
reviewer2.courses_attached += ['Python']

# выставление оценок Ревюьером 1 Студенту 2 за домашнее задание по Питону
reviewer2.rate_hw(best_student2, 'Git', 10)
reviewer2.rate_hw(best_student2, 'Git', 6)
reviewer2.rate_hw(best_student2, 'Git', 5)
reviewer2.rate_hw(best_student2, 'Python', 10)
reviewer2.rate_hw(best_student2, 'Python', 6)
reviewer2.rate_hw(best_student2, 'Python', 5)
print(best_student2)

# Оценка Студента 2 Лектору 1 за лекцию по Питону
best_student2.rate_lecturer(lecturer1, 'Git', 8)
best_student2.rate_lecturer(lecturer1, 'Git', 6)
best_student2.rate_lecturer(lecturer1, 'Git', 7)
best_student2.rate_lecturer(lecturer1, 'Python', 8)
best_student2.rate_lecturer(lecturer1, 'Python', 6)
best_student2.rate_lecturer(lecturer1, 'Python', 7)


print(lecturer1)


pit = 'Python'
git = 'Git'

students = [best_student,best_student2]

average_all_students = average_all_student(students,pit)
print(f'Средняя оценка по всем студентам в рамках {pit} составляет - {average_all_students}')

average_all_stude = average_all_student(students, git)
print(f'Средняя оценка по всем студентам в рамках {git} составляет - {average_all_stude}')

lecturers = [lecturer,lecturer1]

average_all_lecturers = average_all_lecturer(lecturers,pit)
print(f'Средняя оценка за лекции всех лекторов в рамках курса {pit} составляет - {average_all_lecturers}')

lecturers = [lecturer, lecturer1]
average_all_lect = average_all_lecturer(lecturers,git)
print(f'Средняя оценка за лекции всех лекторов в рамках курса {git} составляет - {average_all_lect}')
