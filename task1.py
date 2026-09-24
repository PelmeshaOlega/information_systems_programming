"""
Данный модуль используется для выполнения
второй лабораторной работы по предмету проектирование ИС

В связи с этим меняются и классы:
EducationalClasses - сведения в расписании
Вместо ChemistryClasses и MusicClasses будет класс Lesson (тип урока)
Новый класс Materials (те самый сведения:  число учеников, инструмент, число инструментов, тема.)
"""

from datetime import date

class EducationalClasses:
    """
    Это класс EducationalClasses.
    Он представляет собой учебное занятие в расписании.
    """
    _class_date: date
    _audience_name: str
    _teacher_name: str
    def __init__(self, class_date: date, audience: str, teacher: str):
        self.class_date = class_date
        self.audience_name = audience
        self.teacher_name = teacher

class Lesson(EducationalClasses):
    __lesson_type: str

    def __init__(self, class_date: date,
                 audience: str, teacher: str, lesson_type: str):
        super().__init__(class_date, audience, teacher)
        self.__lesson_type = lesson_type

    def print_type(self):
        print(self.__lesson_type + " " + self.audience_name + " " + self.teacher_name + " " + str(self.class_date))

class Materials(EducationalClasses):
    __students_count: int
    __instruments_count: int
    __theme: str
    __materials: list

    def __init__(self, class_date: date,
                 audience: str, teacher: str, students_count: int, instruments_count: int, theme: str, materials:list):
        super().__init__(class_date, audience, teacher)
        self.__students_count = students_count
        self.__theme = theme
        self.__materials = materials
        self.__instruments_count = instruments_count

    def print_info(self):
        print(str(self.__students_count) + " "+ str(self.__instruments_count) + " " +
              self.__theme + " " + " ".join(self.__materials))

class Factory():

    last_date: date = date(1,1,1)
    last_teacher = ""
    last_audience = ""

    def create_lesson(self, info):
        year = int(info[1].split(".")[0])
        month = int(info[1].split(".")[1])
        day = int(info[1].split(".")[2])
        new_date = date(year, month, day)
        Factory.last_date = new_date
        Factory.last_audience = info[2]
        Factory.last_teacher = str(" ".join(info[3:5]))
        return Lesson(Factory.last_date, Factory.last_audience, Factory.last_teacher, info[5])

    def create_materials(self, info):
        theme = str(" ".join(info[2:info.index("материалы:")]))
        return Materials (Factory.last_date, Factory.last_audience, Factory.last_teacher, int(info[1].strip()),
               int(info[2].strip()), theme, materials_for_lessons("материалы:", info))
    pass

def extract_lines(way: str) -> list:
    with open(way, "r", encoding="utf8") as file:
        return file.readlines()

def materials_for_lessons(start: str, source_info: list) -> list:
    """
    source_info - информация из введённой пользователем строки в файле, разделённая на слова.
    start - слово, с которого начинаются материалы определённого типа в source_info (реагенты или музыка).
    end - слово, с которого начинаются дополнительные материалы к уроку в source_info.
    (защита, в случае реагентов и инструменты, в случае музыки)
    """
    materials = []
    for i in range(source_info.index(start) + 1, len(source_info)):
        materials.append(source_info[i])
    return materials

def parser(information: list) -> list:
    objects_list = []
    new_factory = Factory()

    for info in information:
        info_sep = info.split()

        if info_sep[0] == "урок:":
            new_class = new_factory.create_lesson(info_sep)
            objects_list.append(new_class)
        elif info_sep[0] == "сведения:":
            new_class = new_factory.create_materials(info_sep)
            objects_list.append(new_class)
    return objects_list

list_of_all_objects = []
parsing_objects = []

while True:
    print("1 - добавить в файл\n2 - вывести\n3 - считать с файла\n4 - выход\n")
    menu_number:int = int(input())
    print("Выберите одну из комманд:")
    if menu_number == 1:
        for obj in parsing_objects:
            list_of_all_objects.append(obj)
    elif menu_number == 2:
        for obj in list_of_all_objects:
            if isinstance(obj, Lesson):
                obj.print_type()
            elif isinstance(obj, Materials):
                obj.print_info()
        print("\n")
    elif menu_number == 3:
         parsing_objects = parser(extract_lines("text.txt"))
    elif menu_number == 4:
        break
