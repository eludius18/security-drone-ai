import pytest
from src.alerts.telegram_alert import send_alert

def test_send_alert(mocker):
    """
    Mock the Telegram API request to test the alert function.
    """
    mock_requests = mocker.patch("requests.post")
    send_alert("test.jpg")
    mock_requests.assert_called_once()