def parse_aggregate(agg):
    operations = ['avg', 'min', 'max']
    for operation in operations:
        if operation in agg:
            column, op = agg.split('=')
            return column, op
    raise ValueError('Неверные параметры агрегации')

def apply_aggregate(data, column, op):
    values = []
    for row in data:
        try:
            values.append(float(row[column]))
        except ValueError:
            raise ValueError('Агрегация поддерживает только числовые поля')

    if not values:
        raise ValueError('Нет значений для агрегации')

    if op == 'avg':
        return sum(values) / len(values)
    elif op == 'min':
        return min(values)
    elif op == 'max':
        return max(values)
    else:
        raise ValueError('Неверная операция агрегации')

