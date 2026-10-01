def extract_lines():
    with open("graph.txt") as f:
        return f.readlines()

def inheritance_or_aggregation(all_classes:list, class_name:str, work_mode:str):
    children = []
    for dependency in all_classes:
        trim_string = dependency.replace(" ", "")
        if (class_name in trim_string) and (work_mode in trim_string) and (class_name == trim_string[4]):
                children.append(trim_string[0])
    return children

def check_for_dependencies(class_name:str):
    all_classes = extract_lines()
    inheritance:list = inheritance_or_aggregation(all_classes, class_name, "-->")
    aggregation:list = inheritance_or_aggregation(all_classes, class_name, "o->")
    return [class_name, inheritance, aggregation]

print(check_for_dependencies("F"))
