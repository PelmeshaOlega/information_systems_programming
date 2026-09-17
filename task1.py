"""
Данный модуль используется для выполнения
первой лабораторной работы по предмету проектирование ИС
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

class ChemistryClasses(EducationalClasses):
    """
    Это класс ChemistryClasses.
    Он представляет собой учебное занятие по химии в расписании.
    """
    __reagents: list
    __protective_equipment: list

    def __init__(self, class_date: date,
                 audience: str, teacher: str, reagents:list, protect:list):
        super().__init__(class_date, audience, teacher)
        self.reagents = reagents
        self.protective_equipment = protect

class MusicClasses(EducationalClasses):
    """
    Это класс MusicClasses.
    Он представляет собой учебное занятие по музыке в расписании.
    """
    __music: str
    __instrument: list

    def __init__(self, class_date,
                 audience: str, teacher: str, music:str, instrument:list):
        super().__init__(class_date, audience, teacher)
        self.music = music
        self.instrument = instrument

def materials_for_lessons(start: str, end:str, source_info: list) -> list:
    """
    source_info - информация из введённой пользователем строки в файле, разделённая на слова.
    start - слово, с которого начинаются материалы определённого типа в source_info (реагенты или музыка).
    end - слово, с которого начинаются дополнительные материалы к уроку в source_info.
    (защита, в случае реагентов и инструменты, в случае музыки)
    """
    materials = []
    for i in range(source_info.index(start) + 1, source_info.index(end)):
        materials.append(info_sep[i])
    return materials

def additional_for_lessons(start:str, source_info:list) -> list:
    """
    source_info - информация из введённой пользователем строки в файле, разделённая на слова.
    start - слово в source info, с которого начинаются дополнительные материалы к уроку.
    """
    additional = []
    for i in range(source_info.index(start) + 1, len(source_info)):
        additional.append(source_info[i])
    return additional

objects_list = []
with open("text.txt", "r", encoding="utf8") as f:
    information = f.readlines()


for info in information:
    info_sep = info.split()
    mat = []
    add = []
    new_info_starts = 0

    year = int(info_sep[0].split(".")[0])
    month = int(info_sep[0].split(".")[1])
    day = int(info_sep[0].split(".")[2])
    teacher_info = str(" ".join(info_sep[2:4]))
    new_date = date(year, month, day)
    try:
        if "реагенты:" in info_sep:
            mat = materials_for_lessons("реагенты:", "защита:", info_sep)
            add = additional_for_lessons("защита:", info_sep)
            additional_info_starts = info_sep.index("реагенты:")
            new_class = ChemistryClasses(new_date, info_sep[1], teacher_info, mat, add)
            objects_list.append(new_class)
        elif "музыка:" in info_sep:
            mat = materials_for_lessons("музыка:", "инструменты:", info_sep)
            add = additional_for_lessons("инструменты:", info_sep)
            additional_info_starts = info_sep.index("музыка:")
            new_class = MusicClasses(new_date,info_sep[1],teacher_info," ".join(mat),add)
            objects_list.append(new_class)
        else:
            new_class = EducationalClasses(new_date,info_sep[1],teacher_info)
            objects_list.append(new_class)
    except ValueError:
        print("ВВЕДИТЕ ДАТУ В НУЖНОМ ФОРМАТЕ")
        print("Создан стандартный объект, с вашими данными, не учитывающими дату")
        new_class = EducationalClasses(date(2003, 11, 22), info_sep[1], str(" ".join(info_sep[2:])))
