import pytest
from filter import parse_filter, apply_filter

def test_parse_filter():
    assert parse_filter('price>100') == ('price', '>', '100')
    assert parse_filter('price<100') == ('price', '<', '100')
    assert parse_filter('price=100') == ('price', '=', '100')

def test_apply_filter_numbers():
    row = {'price': '150'}
    assert apply_filter(row, 'price', '>', '100') is True
    assert apply_filter(row, 'price', '<', '200') is True
    assert apply_filter(row, 'price', '=', '150') is True
    assert apply_filter(row, 'price', '=', '100') is False

def test_apply_filter_string():
    row = {'brand': 'Xiaomi'}
    assert apply_filter(row, 'brand', '=', 'xiaomi') is True
    assert apply_filter(row, 'brand', '=', '100') is False