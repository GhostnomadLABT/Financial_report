# test_web_report.py
import pytest
from patterns.web_report import create_content, create_file
from patterns.csv_utils import Ride
from datetime import datetime
from unittest.mock import patch, mock_open

# Datos de prueba
rides = [
    Ride(
        error="",
        taxi_id=1,
        pick_up_time=datetime(2023, 1, 1, 10, 0),
        drop_of_time=datetime(2023, 1, 1, 10, 15),
        passenger_count=2,
        trip_distance=3.5,
        tolls_amount=15.00
    ),
    Ride(
        error="",
        taxi_id=2,
        pick_up_time=datetime(2023, 1, 1, 11, 0),
        drop_of_time=datetime(2023, 1, 1, 11, 20),
        passenger_count=1,
        trip_distance=5.0,
        tolls_amount=20.00
    )
]

def test_create_content():
    html_content = create_content(rides)
    assert "<h1>Taxi Report</h1>" in html_content
    assert "2023-01-01T10:00:00" in html_content
    assert "<td>15.0</td>" in html_content

@pytest.fixture
def mock_file():
    with patch('builtins.open', mock_open()) as mock:
        yield mock

def test_create_file(mock_file):
    content = "Sample HTML content"
    create_file(content)
    mock_file.assert_called_with("financial-report.html", "w")
    mock_file().write.assert_called_once_with(content)
