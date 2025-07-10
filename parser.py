import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Фильтрация и агрегация csv файла')
    parser.add_argument('--file', type=str, required=True, help='Путь к csv-файлу')
    parser.add_argument('--where', type=str, required=False, help='Фильтрация. Пример: "price>100"')
    parser.add_argument('--aggregate', type=str, required=False, help='Агрегация. Пример: "avg=price"')
    args = parser.parse_args()
    return args