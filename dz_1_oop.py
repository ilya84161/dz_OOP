class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __eq__(self, stud) -> bool:
        return (self.average_rating == stud.average_rating)

    def average_rating(self, course):
        return round(sum(self.grades[course])/len(self.grades[course]), 1)

    def __str__(self) -> str:
        return (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_rating('Python')}'
            f'\nКурсы в процессе изучения: {','.join(self.courses_in_progress)}\n'
            f'Завершенные курсы: {','.join(self.finished_courses)}')


    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades ={}

    def __eq__(self, value: object) -> bool:
        return (self.average_rating == value.average_rating)

    def average_rating(self, course):
        return round(sum(self.grades[course])/len(self.grades[course]), 1)

    def __str__(self) -> str:
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rating('Python')}'

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self) -> str:
        return f'Имя: {self.name}\nФамилия: {self.surname}'

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

 
best_student = Student('Ruoy', 'Eman', 'your_gender')
student = Student('Stasyuk', 'Voronkovich', 'man')
cool_mentor = Lecturer('Some', 'Buddy')
mentor = Lecturer('Stasik', 'Bzheshkovich')
cool_mentor1 = Reviewer('Some1', 'Buddy1')
cool_mentor11 = Reviewer('Some11', 'Buddy11')

best_student.courses_in_progress += ['Python']
student.courses_in_progress += ['Python']
best_student.finished_courses +=['Git']
student.finished_courses +=['C++']
 
cool_mentor.courses_attached += ['Python']
mentor.courses_attached += ['Python']
cool_mentor1.courses_attached += ['Python']
cool_mentor11.courses_attached += ['Python']
 
cool_mentor1.rate_hw(best_student, 'Python', 8)
cool_mentor1.rate_hw(best_student, 'Python', 9)
cool_mentor1.rate_hw(best_student, 'Python', 10)

cool_mentor11.rate_hw(student, 'Python', 6)
cool_mentor11.rate_hw(student, 'Python', 5)
cool_mentor11.rate_hw(student, 'Python', 3)

best_student.rate_hw(cool_mentor, 'Python', 9)
best_student.rate_hw(cool_mentor, 'Python', 7)
best_student.rate_hw(cool_mentor, 'Python', 6)
student.rate_hw(mentor, 'Python', 5)
student.rate_hw(mentor, 'Python', 6)
student.rate_hw(mentor, 'Python', 7)
 
print(best_student)
print(student)
print(cool_mentor)
print(mentor)
print(cool_mentor1)
print(cool_mentor11)
print(best_student == student)
print(cool_mentor == mentor)

list_students = [best_student, student]
list_lecturer = [mentor, cool_mentor]
course = 'Python'

def rating_dz(stud: list, course: str):
    rating_stud=[]
    rating_stud +=(i.average_rating(course) for i in stud)
    return sum(rating_stud)/len(rating_stud)

def rating_lecturer(lect: list, course: str):
    rating_lect=[]
    rating_lect +=(i.average_rating(course) for i in lect)
    return sum(rating_lect)/len(rating_lect)

print(f'средняя оценка за домашние задания по всем студентам в рамках курса {course}: {rating_dz(list_students, course)}')
print(f'средняя оценка за лекции всех лекторов в рамках курса {course}: {rating_lecturer(list_lecturer, course)}')