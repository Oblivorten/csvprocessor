import pytest
from read_csv import filter_csv, aggregate_csv, print_table, filter_and_aggregate_csv

def test_filter_csv(capsys, tmp_path):
    path = tmp_path / 'test.csv'
    path.write_text('name,price,rating\nApple,100,4.5\nBanana,50,3.0\nCherry,150,4.8\n')
    filter_csv(str(path), 'price>100')
    captured = capsys.readouterr()
    assert 'Apple' not in captured.out
    assert 'Cherry' in captured.out

def test_filter_csv_no_matches(capsys, tmp_path):
    path = tmp_path / 'test.csv'
    path.write_text('name,price,rating\nApple,100,4.5\nBanana,50,3.0\nCherry,150,4.8\n')
    filter_csv(str(path), 'price>200')
    captured = capsys.readouterr()
    assert 'Нет данных' in captured.out

def test_aggregate_csv_min(capsys, tmp_path):
    path = tmp_path / 'test.csv'
    path.write_text('name,price,rating\nApple,100,4.5\nBanana,50,3.0\nCherry,150,4.8\n')
    aggregate_csv(str(path), 'price=min')
    captured = capsys.readouterr()
    assert '50' in captured.out

def test_aggregate_csv_avg(capsys, tmp_path):
    path = tmp_path / 'test.csv'
    path.write_text('name,price,rating\nApple,100,4.5\nBanana,50,3.0\nCherry,150,4.8\n')
    aggregate_csv(str(path), 'rating=avg')
    captured = capsys.readouterr()
    assert any(x in captured.out for x in ['4.1', '4.10', '4.13'])

def test_print_table(capsys, tmp_path):
    path = tmp_path / 'test.csv'
    path.write_text('name,price,rating\nApple,100,4.5\nBanana,50,3.0\nCherry,150,4.8\n')
    print_table(str(path))
    captured = capsys.readouterr()
    assert 'Apple' in captured.out
    assert 'Banana' in captured.out
    assert 'Cherry' in captured.out

def test_print_table_empty(capsys, tmp_path):
    path = tmp_path / 'empty.csv'
    path.write_text('name,price,rating\n')
    print_table(str(path))
    captured = capsys.readouterr()
    assert 'Файл пустой' in captured.out

def test_filter_and_aggregate_csv(capsys, tmp_path):
    path = tmp_path / 'test.csv'
    path.write_text('name,price,rating\nApple,100,4.5\nBanana,50,3.0\nCherry,150,4.8\n')
    filter_and_aggregate_csv(str(path), 'price>50', 'rating=max')
    captured = capsys.readouterr()
    assert '4.8' in captured.out

def test_filter_and_aggregate_csv_no_filtered_data(capsys, tmp_path):
    path = tmp_path / 'test.csv'
    path.write_text('name,price,rating\nApple,100,4.5\nBanana,50,3.0\nCherry,150,4.8\n')
    filter_and_aggregate_csv(str(path), 'price>200', 'rating=max')
    captured = capsys.readouterr()
    assert 'Нет данных после фильтрации' in captured.out

def test_filter_and_aggregate_csv_aggregation_error(capsys, tmp_path):
    path = tmp_path / 'bad.csv'
    path.write_text('name,price\nA,\nB,\n')
    filter_and_aggregate_csv(str(path), 'price>0', 'price=avg')
    captured = capsys.readouterr()
    assert 'Нет данных после фильтрации' in captured.out
