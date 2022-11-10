def arithmetic_arranger(problems, result=False):
    operators = {"+": lambda a, b: a + b, "-": lambda a, b: a - b}
    errors = {
        0: "Error: Too many problems.",
        1: "Error: Operator must be '+' or '-'.",
        2: "Error: Numbers cannot be more than four digits.",
        3: "Error: Numbers must only contain digits.",
    }
    if len(problems) > 5:
        return errors[0]
    rows = {i: "" for i in range(4)}

    for val1, operator, val2 in [p.split() for p in problems]:
        size = max([len(val1), len(val2)])
        if operator not in operators:
            return errors[1]
        if size > 4:
            return errors[2]
        try:
            total = str(operators[operator](int(val1), int(val2)))
        except:
            return errors[3]
        space = "    "
        rows[0] += " " * (size + 2 - len(val1)) + val1 + space
        rows[1] += operator + " " * (size + 1 - len(val2)) + val2 + space
        rows[2] += "-" * (size + 2) + space
        rows[3] += " " * (size + 2 - len(total)) + total + space

    arranged_problems = ""
    for index in range(4):
        row = rows[index][:-4]
        if index == 3:
            if result:
                arranged_problems += "\n" + row
        elif index == 2:
            arranged_problems += row
        else:
            arranged_problems += row + "\n"

    return arranged_problems
