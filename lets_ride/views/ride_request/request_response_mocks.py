

REQUEST_BODY_JSON = """
{
    "from_place": "string",
    "to_place": "string",
    "datetime": "string",
    "flexible_timings": true,
    "start_datetime": "string",
    "end_datetime": "string",
    "no_of_seats": 1,
    "luggage_quantity": 1
}
"""


RESPONSE_400_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "INVALIDNOOFSEATS"
}
"""

