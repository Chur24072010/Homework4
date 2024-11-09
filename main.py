class StudySubject:

 def __init__(self):

     self.name = input("Введіть назву предмету: ")

     self.hours = int(input("Введіть кількість годин: "))

     self.enable = input("Чи є активним? (Так/Ні): ").lower() == 'так'

 def info_study(self):

     print(f'Предмет: {self.name} | {self.hours} годин')

class Student:

 def __init__(self):

     self.name = input("Введіть ім'я студента: ")

     self.surname = input("Введіть прізвище студента: ")

     self.subjects = []

     num_subjects = int(input("Введіть кількість предметів: "))

     for _ in range(num_subjects):

         print(f"\nВведіть дані для предмету {_+1}:")

         self.subjects.append(StudySubject())

 def info_student(self):

     print(f'Студент: {self.name} | {self.surname}')

 def info_all(self):

     self.info_student()

     for subject in self.subjects:

         subject.info_study()

class Group:

 def __init__(self):

     self.group_name = input("Введіть назву групи: ")

     self.num_students = int(input("Введіть кількість студентів у групі: "))

     self.age_category = input("Введіть вікову категорію: ")

     self.students = []

     for _ in range(self.num_students):

         print(f"\nВведіть дані для студента {_+1}:")

         self.students.append(Student())

 def display_group_info(self):

     print(f"\nНазва групи: {self.group_name}")

     print(f"Вікова категорія: {self.age_category}")

     print(f"Кількість студентів: {self.num_students}")

     print("\nІнформація про студентів:")

     for student in self.students:

         student.info_all()
