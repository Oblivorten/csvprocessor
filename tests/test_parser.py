import pytest
import sys
from parser import parse_args

def test_parse_args_file(monkeypatch):
    monkeypatch.setattr(sys, 'argv', ['prog', '--file', 'data.csv'])
    args = parse_args()
    assert args.file == 'data.csv'
    assert args.where is None
    assert args.aggregate is None

def test_parse_args_where(monkeypatch):
    monkeypatch.setattr(sys, 'argv', ['prog', '--file', 'data.csv', '--where', 'price>100'])
    args = parse_args()
    assert args.file == 'data.csv'
    assert args.where == 'price>100'
    assert args.aggregate is None

def test_parse_args_aggregate(monkeypatch):
    monkeypatch.setattr(sys, 'argv', ['prog', '--file', 'data.csv', '--aggregate', 'avg=price'])
    args = parse_args()
    assert args.file == 'data.csv'
    assert args.where is None
    assert args.aggregate == 'avg=price'

def test_parse_args_without_file(monkeypatch):
    monkeypatch.setattr(sys, 'argv', ['prog'])
    with pytest.raises(SystemExit):
        parse_args()
