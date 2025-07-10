from read_csv import aggregate_csv, filter_csv, print_table, filter_and_aggregate_csv
from parser import parse_args

def main():
    args = parse_args()
    filepath = args.file
    filter = args.where
    agg = args.aggregate
    if filter and agg:
        filter_and_aggregate_csv(filepath, filter, agg)
    elif filter:
        filter_csv(filepath, filter)
    elif agg:
        aggregate_csv(filepath, agg)
    else:
        print_table(filepath)

if __name__ == '__main__':
    try:
        main()
    except ValueError as e:
        print(f'Ошибка {e}')