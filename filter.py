def parse_filter(filter):
    operators = ['>', '<', '==', '=']
    for operator in operators:
        if operator in filter:
            field, value = filter.split(operator)
            return field, operator, value
    raise ValueError('Введен неправильный фильтр')

def apply_filter(row, field, operator, value):
    try:
        row_value = float(row[field])
        value = float(value)
    except ValueError:
        row_value = str(row[field]).lower()
        value = str(value).lower()

    if operator == '>':
        return row_value > value
    elif operator == '<':
        return row_value < value
    elif operator == '=':
        return row_value == value
    elif operator == '==':
        return row_value == value
    else:
        return False