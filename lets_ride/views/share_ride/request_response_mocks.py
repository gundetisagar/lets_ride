

REQUEST_BODY_JSON = """
{
    "from_place": "string",
    "to_place": "string",
    "date_time": "string",
    "flexible_timings": true,
    "start_date_time": "string",
    "end_date_time": "string",
    "no_of_seats_available": 1,
    "assets_quantity": 1
}
"""


RESPONSE_400_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "InvalidToPlace"
}
"""

