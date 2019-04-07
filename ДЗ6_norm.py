# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.


class Person:
    def __init__(self, name, surname, patronymic):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
    def full_name(self):
     return self.surname + ' ' + self.name  + ' ' + self.patronymic
    
    def FIO (self):
        return self.surname + ' ' + self.name[0] +'.' + self.patronymic[0] +'.'
class Teacher(Person):
    def __init__(self, name, surname, patronymic, teach_clas):
        super().__init__(name, surname, patronymic)
        self.teach_clas = teach_clas
    def get_teach_clas(self):
        return self.teach_clas
class Parent (Person):
     def __init__(self, name, surname, patronymic, status, number):
        super().__init__(name, surname, patronymic)
        self.status = status
        self.number = number

     def number2(self):
        return self.number

     def stat(self):
        return self.status
        
class Student(Person):
    def __init__(self, name, surname, patronymic, class_room, number):
        super().__init__(name, surname, patronymic)
        self.class_room = class_room
        self.number = number
        
    def get_class_room(self):
        return self.class_room

    def number1(self):
        return self.number
            
class Sp_cl:
   def __init__(self, class_room):
        self.class_room = class_room
   def sp_cl_r(self):
        return self.class_room     
class Lesson:
    def __init__(self, class_room, teach_clas):
        self.class_room = class_room
        self.teach_clas = teach_clas
    def sp_class_room (self):
        return self.class_room
    def sp_teach_clas (self):
        return self.teach_clas
    


Sp_cls = {Sp_cl("1А"),
          Sp_cl("1Б"),
          Sp_cl("2А"),
          Sp_cl("3А"),
          Sp_cl("3Б")}
                
Lessons = {Lesson("1А", "Математика"),
           Lesson("1А", "Русский язык"),
           Lesson("1А", "Литература"), 
           Lesson("1Б", "Математика"),
           Lesson("1Б", "Русский язык"),
           Lesson("1Б", "Литература"),
           Lesson("2А", "Математика"),
           Lesson("2А", "Русский язык"),
           Lesson("2А", "Литература"),
           Lesson("2А", "Физкультура"),
           Lesson("2А", "Музыка"), 
           Lesson("3А", "Математика"),
           Lesson("3А", "Русский язык"),
           Lesson("3А", "Литература"),
           Lesson("3А", "История"),
           Lesson("3Б", "Математика"),
           Lesson("3Б", "Русский язык"),
           Lesson("3Б", "Литература"),
           Lesson("3Б", "История")}
                
students = {Student("Алексей", "Иванов", "Иванович", "1А", 1),
            Student("Ольга", "Сидорова", "Петровна", "1А", 2),
            Student("Алексей", "Сидоров", "Федорович", "1А", 3),
            Student("Сергей", "Иванов", "Иванович", "1А", 4),
            Student("Светлана", "Сидорова", "Петровна", "1А", 5),
            Student("Сергей", "Сидоров", "Федорович", "2А", 6),
            Student("Алексей", "Иванов", "Иванович", "2А", 7),
            Student("Ольга", "Сидорова", "Петровна", "2А", 8),
            Student("Елена", "Сидорова", "Сергеевна", "1Б", 9),
            Student("Светлана", "Иванова", "Ивановна", "1Б", 10),
            Student("Светлана", "Сидорова", "Петровна", "1Б", 11),
            Student("Сергей", "Сергеев", "Федорович", "3А", 12),
            Student("Алексей", "Зайцев", "Иванович", "3А", 13),
            Student("Ольга", "Котова", "Петровна", "3А", 14),
            Student("Алексей", "Козлов", "Федорович", "3Б", 15),
            Student("Нина", "Ким", "Ченовна", "3Б", 16),
            Student("Альфред", "Соловейчик", "Богданович", "3Б", 17)}

teachers = {Teacher("Александр", "Пушкин", "Сергеевич", "Литература"),
            Teacher("Николай", "Лобачевский", "Иванович", "Математика"),
            Teacher("Лев", "Гумилев", "Николаевич", "История"),
            Teacher("Юрий", "Лотман", "Михайлович", "Русский язык"),
            Teacher("Иван", "Поддубный", "Максимович", "Физкультура"),
            Teacher("Петр", "Чайковский", "Ильич", "Музыка")}

parents = {Parent("Иван", "Иванов", "Сидорович", "отец", 1),
           Parent("Ольга", "Иванова", "Петровна", "мать", 1),
           Parent("Петр", "Сидоров", "Евгеньевич", "отец",2),
           Parent("Юлия", "Сидорова", "Сергеевна", "мать", 2),
           Parent("Федор", "Сидоров", "Петрович", "отец", 3),
           Parent("Клавдия", "Сидорова", "Евгеньевна", "мать",3),
           Parent("Иван", "Иванов", "Сидорович", "отец", 4),
           Parent("Ольга", "Иванова", "Петровна", "мать", 4),
           Parent("Петр", "Сидоров", "Евгеньевич", "отец",5),
           Parent("Юлия", "Сидорова", "Сергеевна", "мать", 5),
           Parent("Федор", "Сидоров", "Петрович", "отец", 6),
           Parent("Клавдия", "Сидорова", "Евгеньевна", "мать",6),
           Parent("Иван", "Иванов", "Сидорович", "отец", 7),
           Parent("Ольга", "Иванова", "Петровна", "мать", 7),
           Parent("Петр", "Сидоров", "Евгеньевич", "отец",8),
           Parent("Юлия", "Сидорова", "Сергеевна", "мать", 8),
           Parent("Сергей", "Сидоров", "Петрович", "отец", 9),
           Parent("Светлана", "Сидорова", "Евгеньевна", "мать",9),
           Parent("Иван", "Иванов", "Сидорович", "отец", 10),
           Parent("Ольга", "Иванова", "Петровна", "мать", 10),
           Parent("Петр", "Сидоров", "Евгеньевич", "отец",11),
           Parent("Юлия", "Сидорова", "Сергеевна", "мать", 11),
           Parent("Федор", "Сергеев", "Олегович", "отец", 12),
           Parent("Нина", "Сергеева", "Евгеньевна", "мать",12),
           Parent("Иван", "Зайцев", "Никитович", "отец", 13),
           Parent("Ольга", "Зайцева", "Петровна", "мать", 13),
           Parent("Петр", "Котов", "Емельянович", "отец",14),
           Parent("Юлия", "Котова", "Сергеевна", "мать", 14),
           Parent("Федор", "Козлов", "Петрович", "отец", 15),
           Parent("Альбина", "Козлова", "Михайловна", "мать",15),
           Parent("Чен", "Ким", "Ир", "отец", 16),
           Parent("Ольга", "Ким", "Юрьевна", "мать", 16),
           Parent("Богдан", "Соловейчик", "Альбертович", "отец",17),
           Parent("Татьяна", "Соловейчик", "Сергеевна", "мать", 17)}
# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
print ("Список классов:")
for Sp_cl in Sp_cls :
    print (Sp_cl.sp_cl_r())
    
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
choice_cl = input("Выберите номер класса " )
print ("Список учеников класса "  + choice_cl)
for Student in students:
    if Student.class_room == choice_cl:
        print (Student.FIO())
   
  
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
choice_st = input("Выберите  ученика ")

print ("Класс ",choice_cl)
print ("Предметы:")
for Lesson in Lessons:
    if choice_cl == Lesson.sp_class_room():
        print(Lesson.sp_teach_clas())
    

        
# 4. Узнать ФИО родителей указанного ученика
for Student in students:
    if choice_st == Student.FIO():
        num1 = Student.number1()
print ("Родители:")
for Parent in parents:
     if num1 == Parent.number2():
         print (Parent.stat(), Parent.full_name())

# 5. Получить список всех Учителей, преподающих в указанном классе 
print ("Учителя:")
for Lesson in Lessons:
    if choice_cl == Lesson.sp_class_room():
        les1 = Lesson.sp_teach_clas()
        for Teacher in teachers:
            if Teacher.teach_clas == les1:
                print (Teacher.teach_clas, Teacher.FIO())

     
