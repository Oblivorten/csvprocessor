import pytest
from aggregator import parse_aggregate, apply_aggregate

def test_parse_aggregate():
    assert parse_aggregate('rating=min') == ('rating', 'min')
    assert parse_aggregate('rating=max') == ('rating', 'max')
    assert parse_aggregate('score=avg') == ('score', 'avg')


def test_apply_aggregate_min():
    data = [{'price': '100'}, {'price': '200'}, {'price': '150'}]
    assert apply_aggregate(data, 'price', 'min') == 100

def test_apply_aggregate_max():
    data = [{'price': '100'}, {'price': '200'}, {'price': '150'}]
    assert apply_aggregate(data, 'price', 'max') == 200

def test_apply_aggregate_avg():
    data = [{'rating': '4.5'}, {'rating': '3.5'}, {'rating': '5.0'}]
    assert apply_aggregate(data, 'rating', 'avg') == pytest.approx(4.33, rel=1e-2)

def test_apply_aggregate_empty_column():
    data = [{'rating': ''}, {'rating': ''}]
    with pytest.raises(ValueError):
        apply_aggregate(data, 'rating', 'avg')

def test_apply_aggregate_unknown_operation():
    data = [{'rating': 'meow'}]
    with pytest.raises(ValueError):
        apply_aggregate(data, 'rating', 'sum')
