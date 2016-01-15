from yunity.utils.tests.comparison import ANY_INT, DATETIME_AROUND_NOW
from .initial_data import before_messages

response = {
    "http_status": 200,
    "response": {
        "messages": [
            {
                "content": _.content,
                "sender": _.sent_by.id,
                "created_at": DATETIME_AROUND_NOW,
                "id": ANY_INT,
            } for _ in reversed(before_messages)
        ]
    }
}