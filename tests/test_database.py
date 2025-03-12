import pytest
from src.database.database import Database

@pytest.fixture
def db():
    """
    Creates a test instance of the Database class.
    """
    return Database()

def test_log_event(db, mocker):
    """
    Test if an event is logged correctly.
    """
    mock_insert = mocker.patch.object(db.events, "insert_one")
    db.log_event("intruder_detected", {"confidence": 90})
    mock_insert.assert_called_once()

def test_get_recent_events(db, mocker):
    """
    Test retrieving recent events from the database.
    """
    mocker.patch.object(db.events, "find", return_value=[])
    events = db.get_recent_events()
    assert isinstance(events, list)