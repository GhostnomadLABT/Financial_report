# test_csv_utils.py
import pytest
from patterns.csv_utils import parse_file, Ride
from unittest.mock import patch, mock_open
from datetime import datetime

@pytest.fixture
def mock_csv_file():
    csv_content = """TaxiID,lpep_pickup_datetime,lpep_dropoff_datetime,passenger_count,trip_distance,total_amount
1,2023-01-01 10:00:00,2023-01-01 10:15:00,2,3.5,15.00
2,2023-01-01 11:00:00,2023-01-01 11:20:00,1,5.0,20.00
"""
    with patch('builtins.open', mock_open(read_data=csv_content)) as mock_file:
        yield mock_file

def test_parse_file(mock_csv_file):
    rides = parse_file("taxi_data.csv")
    assert len(rides) == 2
    assert isinstance(rides[0], Ride)
    assert rides[0].pick_up_time == datetime(2023, 1, 1, 10, 0)
    assert rides[0].tolls_amount == 15.00


