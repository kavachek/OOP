import random
from os import path
from pathlib import Path


class Member:
    def __init__(self, name, surname, email, age, tel):
        self.name = name
        self.surname = surname
        self.email = email
        self.age = age
        self.tel = tel


class Employee(Member):
    ALL_employee = []

    def __init__(self, name, surname, email, age, tel, position, personal_data,
                 contract, skills):
        super().__init__(name, surname, email, age, tel)
        self.position = position
        self.personal_data = personal_data
        self.rate = random.randint(10000, 50000)  # rate - ставка
        self.contract = contract
        self.skills = skills
        self.__passport_ser_number = None
        Employee.ALL_employee.append(self)

        @property
        def passport_ser_number(self):
            return self.__passport_ser_number

        @passport_ser_number.setter
        def passport_ser_number(self, passport):
            if len(str(passport)) == 10:
                self.__passport_ser_number = passport = 1234
            else:
                print('Неверное значение')


class Curator(Employee):
    ALL_event = []
    ALL_curator = []

    def __init__(self, name, surname, email, age, tel, position, personal_data,
                 rate, contract):  # rate - ставка
        super().__init__(name, surname, email, age, tel, position, personal_data, rate, contract)

    @staticmethod
    def create_event(name_event, participants, date):
        Curator.ALL_event.append([name_event, participants, date])
        return True


def sending_notifications(message, list_recipient: list):
    for stud in list_recipient:
        print(f'{message} для {stud.email}')


# print(Сurator.ALL_event[0]['name_event'])


class Student(Member):
    ALL_student = []
    Last_id = 0

    def __init__(self, name, surname, email, age, tel):
        super().__init__(name, surname, email, age, tel)
        self.knowledge = []
        self.id = Student.Last_id
        Student.Last_id += 1

        Student.ALL_student.append(self)

    def dead(self):
        print('Я удалился')
        del self

    def __del__(self):
        print(f'Меня больше нет {self}')

# i = 0
# while i < 1000:
#     Student()
#     i += 1
# print('Количество студентов:', len(Student.ALL_student))

    @staticmethod
    def get_all_students():
        return Student.ALL_student

    @staticmethod
    def check_student(student):
        if student in Student.ALL_student:
            return True
        else:
            return False

    def get_knowledge(self, lesson):
        self.knowledge.append(lesson)
        return True

    def __str__(self):
        return self.name + ' ' + self.surname

    def __repr__(self):
        full_name = path.basename(Path(__file__))
        name_module = path.splitext(full_name)[0]
        print(name_module)
        return f'{name_module}.Student(\'{self.name}\', \'{self.surname}\', \'{self.age}\', \'{self.email}\')'


class Teacher(Employee):
    ALL_teachers = []
    Teacher_id = 0

    def __init__(self, name, surname, email, age, tel, position, personal_data,
                 rate, contract, skills):
        super().__init__(name, surname, email, age, tel, position, personal_data, rate, contract)
        self.rate = rate
        self.skills = skills
        self.id = Teacher.Teacher_id
        Teacher.ALL_teachers.append(self)
        Teacher.Teacher_id += 1

    def dead(self):
        print('Меня уволили')
        del self

    def __del__(self):
        print(f'Меня больше нет {self}')

    def __str__(self):
        return self.name + ' ' + self.surname

    @staticmethod
    def get_all_teachers():
        return Teacher.ALL_teachers

    @staticmethod
    def check_teacher(teacher: "Teacher"):
        if teacher in Teacher.ALL_teachers:
            return True
        else:
            print(f'Самозванец, {teacher.name}, {teacher.surname}')
            return False

    def hold_lesson(self, lesson: "Discipline", students: list) -> bool:
        if Teacher.check_teacher(self) and Discipline.check_teacher_by_lesson(lesson, self):
            student_names = []
            for student in students:
                student.get_knowledge(lesson)
                student_names.append(student.name)
            print(f"Преподаватель {self.surname} {self.name} провел занятие"
                  f" \"{lesson.discipline_name}\" \n  Для студентов: \n{student_names}")
            return True
        return False


class Discipline:
    ALL_disciplines = []

    def __init__(self, discipline_name, list_lessons, list_teachers):
        self.discipline_name = discipline_name
        self.list_lessons = list_lessons
        self.list_teachers = list_teachers
        Discipline.ALL_disciplines.append(self)

    def add_lesson(self, discipline):
        self.list_lessons.append(discipline)

    def del_lesson(self, discipline):
        self.list_lessons.remove(discipline)

    def check_teacher_by_lesson(self, teacher: "Teacher"):
        if teacher in self.list_teachers:
            return True
        else:
            print(f"Преподаватель {teacher.surname} {teacher.name} не может преподать урок"
                  f"\"{self.discipline_name}\", так как не знает его")
            return False

    def get_teachers_by_lesson(self):
        return self.list_teachers


class Lesson(Discipline):
    ALL_lesson = []

    def __init__(self, lesson_name, list_themes):
        self.themes = None
        self.lesson_name = lesson_name
        self.list_themes = list_themes
        Lesson.ALL_lesson.append(self)

    def add_theme(self, themes):
        self.list_themes.append(themes)

    def del_theme(self, themes):
        self.list_themes.remove(themes)

    def check_theme(self, themes):
        if themes in self.list_themes:
            return True
        print(f'Данная тема урока {self.themes} не была найдена в уроке {self.lesson_name}')
        return False

    @staticmethod
    def get_all_lesson():
        return Lesson.ALL_lesson


class Test:
    pass


class Materials:
    pass


def add_test(test: "Test"):
    Themes.ALL_themes.append(test)


def get_all_themes():
    return Themes.ALL_themes


def del_test(test: "Test"):
    Themes.ALL_themes.remove(test)


def add_materials(materials: "Materials"):
    Themes.ALL_Materials.append(materials)


def del_materials(materials: "Materials"):
    Themes.ALL_Materials.remove(materials)


def get_all_test():
    return Themes.ALL_Test


def get_all_materials():
    return Themes.ALL_Materials


class Themes:
    ALL_themes = []
    ALL_Test = []
    ALL_Materials = []

    def __init__(self, theme_name, materials):
        self.theme_name = theme_name
        self.materials = materials
        Themes.ALL_themes.append(self)
        Themes.ALL_Materials.append(materials)
        Themes.ALL_Test.append(theme_name)

    def __repr__(self):
        return self.theme_name


class EducationProgram:
    ALL_EducationProgram = []

    def __init__(self, program_name, list_disciplines):
        self.program_name = program_name
        self.list_disciplines = list_disciplines
        EducationProgram.ALL_EducationProgram.append(self)

    def add_discipline(self, discipline):
        self.list_disciplines.append(discipline)

    def del_discipline(self, discipline):
        self.list_disciplines.remove(discipline)

    @staticmethod
    def get_ALL_program():
        return EducationProgram.ALL_EducationProgram


class Grade:
    grade_dist = {2: range(0, 50), 3: range(50, 70), 4: range(70, 90), 5: range(90, 100 + 1)}

    @staticmethod
    def grade_translation(points):
        try:
            """перевод баллов в оценку"""
            for K, V in Grade.grade_dist.items():
                if points in V:
                    return K
        except ValueError:
            print('Ты ломаешь систему.')
            return False


class Group:
    ALL_Group = []

    def __init__(self, curator, list_student):
        self.curator = curator
        self.list_student = list_student
        Group.ALL_Group.append(self)

    def add_student(self, student):
        self.list_student.append(student)

    def del_student(self, student):
        self.list_student.remove(student)

    def get_all_student_group(self):
        return self.list_student

    def get_all_email_group(self):
        list_email = []
        for stud in self.list_student:
            list_email.append(stud.email)
        print(list_email)

    def check_student_by_group(self, student):
        if student in self.list_student:
            print(f'Студент в группе {self}')
            return True
        else:
            print('Неизвестно кто.')
            return False


# Учителя
Teacher_Vladislav = Teacher('Владислав', 'Духовских', 'prizrak@mail.ru', 26, '89169999999', 'programmer',
                            'личной информации пока нет', 20000, 'ГПХ', 6)
Teacher_Alexey = Teacher('Aлексей', 'Пивозавр', 'pivo@mail.ru', 29, '89169999999', 'musician',
                         'личной информации пока нет', 20000, 'ГПХ', 5)

# Студенты
Stud_Vitya = Student('Витя', 'Витевский', 'vita@mail.ru', 18, '89169999999')
Stud_Dima = Student('Дима', 'Димас', 'dimas@mail.ru', 0, '89169999999')
Stud_Anna = Student('Анна', 'Аннна', 'anna@mail.ru', 19, '89169999999')
Stud_Sasha = Student('Саша', 'Сасашаша', 'Sasha@mail.ru', -1, '89169999999')

list_s = Student.ALL_student.copy()
list_s.append(Teacher_Vladislav)

# for student in list_s:
#     print(Student.check_student(student))

# Список уроков
Programming = Discipline("программирование", ["ооп"], [Teacher_Vladislav])
Music = Discipline("музыка", ["ноты"], [Teacher_Alexey])

# Teacher_Vladislav.hold_lesson(Programming, [Stud_Dima, Stud_Anna])
# Teacher_Alexey.hold_lesson(Music, [Stud_Sasha, Stud_Vitya])
# Teacher_Alexey.hold_lesson(Programming, [Stud_Dima])
# Teacher.hold_lesson(Stud_Sasha, Programming, [Stud_Vitya])

# # Кураторы
# Curator_Vitya = Curator('Витя', 'Витевский', 'vita@mail.ru', 18, '89169999999', 'Куратор', 'Личное информации нет',
#                         20000, 'ГПХ')
#
# # Сообщение
# message = 'Поздравляю всех с постулением!'


# Список получателей
# list_email = []
# for students in Student.ALL_student:
#     list_email.append(students.email)
#
# # Рассылка
# sending_notifications(message = message, list_recipient = list_email)
#
# print('Ставим оценку:', Grade.grade_translation(48))
#
# One = Group(Curator_Vitya, [Stud_Dima, Stud_Sasha])

# tem_1 = Themes('Вводное занятие', [1, 2, 3, 67, 0.9, 3])
# tem_2 = Themes('Занятие_1', [5, 676, 2346, 8])
# tem_3 = Themes('Занятие_2', [3, 456, 643, 2])
#
# Group.get_all_student_group(One)
# Group.check_student_by_group(One, Stud_Sasha)
# Group.check_student_by_group(One, Stud_Vitya)
#
# Les_1 = Lesson('Урок_1', [tem_2, tem_3, tem_1])
# print(Les_1.list_themes)

