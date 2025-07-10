import csv
from filter import parse_filter, apply_filter
from aggregator import parse_aggregate, apply_aggregate
from tabulate import tabulate

def filter_csv(filepath, filter):
    field, operator, value = parse_filter(filter)
    result_rows = []
    with open(filepath, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if apply_filter(row, field, operator, value):
                result_rows.append(row)
    if result_rows:
        print(tabulate(result_rows, headers='keys', tablefmt='grid'))
    else:
        print('Нет данных, подходящих под фильтр')

def aggregate_csv(filepath, agg):
    column, op = parse_aggregate(agg)
    data = []
    with open(filepath, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    result = apply_aggregate(data, column, op)
    print(tabulate([[result]], headers=[op], tablefmt='grid'))

def print_table(filepath):
    with open(filepath, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        if rows:
            print(tabulate(rows, headers='keys', tablefmt='grid'))
        else:
            print('Файл пустой')

def filter_and_aggregate_csv(filepath, filter, agg):
    field, operator, value = parse_filter(filter)
    data_filtered = []
    with open(filepath, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if apply_filter(row, field, operator, value):
                data_filtered.append(row)
    if not data_filtered:
        print('Нет данных после фильтрации')
        return
    column, op = parse_aggregate(agg)
    try:
        result = apply_aggregate(data_filtered, column, op)
    except ValueError as e:
        print(f'Ошибка агрегации: {e}')
        return
    print(tabulate([[result]], headers=[op], tablefmt='grid'))
