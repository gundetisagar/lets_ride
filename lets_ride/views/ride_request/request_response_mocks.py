

REQUEST_BODY_JSON = """
{
    "from_place": "string",
    "to_place": "string",
    "date_time": "2099-12-31 00:00:00",
    "flexible_timings": true,
    "start_date_time": "2099-12-31 00:00:00",
    "end_date_time": "2099-12-31 00:00:00",
    "no_of_seats": 1,
    "luggage_quantity": 1
}
"""


RESPONSE_400_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "InvalidToPlace"
}
"""

