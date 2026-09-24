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
    for info in information:
        info_sep = info.split()

        try:
            if "урок:" in info_sep:
                    year = int(info_sep[1].split(".")[0])
                    month = int(info_sep[1].split(".")[1])
                    day = int(info_sep[1].split(".")[2])
                    new_date = date(year, month, day)
                    current_date = new_date
                    current_audience = info_sep[2]
                    current_teacher = str(" ".join(info_sep[3:5]))
                    new_class = Lesson(current_date, current_audience, current_teacher, info_sep[5])
                    objects_list.append(new_class)
                #поправить, тут Value Error есть.
            elif "сведения:" in info_sep:
                    theme = str(" ".join(info_sep[2:info_sep.index("материалы:")]))
                    new_class = Materials(current_date, current_audience, current_teacher, int(info_sep[1].strip()),
                                          int(info_sep[2].strip()), theme, materials_for_lessons("материалы:", info_sep))
                    objects_list.append(new_class)
            else:
                    new_class = EducationalClasses(current_date, current_audience, current_teacher)
                    objects_list.append(new_class)
        except ValueError:
            print("ВВЕДИТЕ ДАТУ В НУЖНОМ ФОРМАТЕ")
            print("Создан стандартный объект, с вашими данными, не учитывающими дату")
            new_class = EducationalClasses(date(2003, 11, 22), info_sep[1], str(" ".join(info_sep[2:])))
    return objects_list

objects_list = []
result:list = parser(extract_lines("text.txt"))

for obj in objects_list:
    if isinstance(obj, Lesson):
        obj.print_type()
    elif isinstance(obj, Materials):
        obj.print_info()
