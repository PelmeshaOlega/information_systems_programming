from datetime import date

class EducationalClasses:

    class_date: date = date(1,1,1)
    audience_name = ""
    teacher_name: str = ""
    def __init__(self, class_year: int, class_month: int, class_day: int, audience: str, teacher: str):
        self.date = date(class_year, class_month, class_day)
        self.audience_name = audience
        self.teacher_name = teacher

information: str = ""
while True:
    information = str(input())
    if information == "stop":
        break
    info_sep = information.split()
    year = int(info_sep[0].split(".")[0])
    month = int(info_sep[0].split(".")[1])
    day = int(info_sep[0].split(".")[2])
    try:
        new_class = EducationalClasses(year, month, day, info_sep[1],     str(" ".join(info_sep[2:])))
    except ValueError:
        print("ВВЕДИТЕ ДАТУ В НУЖНОМ ФОРМАТЕ")
        print("Создан стандартный объект, с вашими данными, не учитывающими дату")
        new_class = EducationalClasses(2003, 11, 22, info_sep[1], info_sep[2])

    print(new_class.class_date)
    print(new_class.audience_name)
    print(new_class.teacher_name)
