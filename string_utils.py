def split_before_each_uppercases(formula):
    result = []
    current_part = ""
    for char in formula:
        if char.isupper():
            if current_part:
                result.append(current_part)
            current_part = char
        else:
            current_part += char
    if current_part:
        result.append(current_part)
    return result
    
def split_at_first_digit(formula):
    for i in range(1, len(formula)):
        if formula[i].isdigit():
            return formula[:i], int(formula[i:])
    return formula, 1 
