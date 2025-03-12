import os
import pymongo
from datetime import datetime

# Load MongoDB URL from environment variables
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
DB_NAME = "security_drone"

class Database:
    """
    Handles event logging in MongoDB.
    """
    def __init__(self):
        self.client = pymongo.MongoClient(MONGO_URI)
        self.db = self.client[DB_NAME]
        self.events = self.db["events"]

    def log_event(self, event_type, details):
        """
        Stores an event log in the database.

        :param event_type: Type of event (e.g., 'intruder_detected', 'drone_patrol')
        :param details: Additional details about the event
        """
        event = {
            "event_type": event_type,
            "timestamp": datetime.utcnow(),
            "details": details
        }
        self.events.insert_one(event)

    def get_recent_events(self, limit=10):
        """
        Fetches recent events.

        :param limit: Number of events to retrieve
        :return: List of event documents
        """
        return list(self.events.find().sort("timestamp", -1).limit(limit))

# Example usage
if __name__ == "__main__":
    db = Database()
    db.log_event("intruder_detected", {"confidence": 95, "location": "north_entrance"})
    print(db.get_recent_events())