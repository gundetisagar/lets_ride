import requests
import json

# valid details
print("user log in with valid datails")
url = "http://127.0.0.1:8080/api/lets_ride_auth/login/v1/"
headers = {"Content-Type": "application/json"}
data = '{"username":"test_1","password":"tesr@1234", "name":"test", "mobile_number":"9876543210"}'
response = requests.post(url=url, headers=headers, data=data)
print(response.content)
token_details = json.loads(response.content)
access_token = str(token_details["access_token"])
print(access_token)
print("\n")

# ---------------------------------------------------------------------------->
# create share travel info
print("create share travel info with flexible timings true")
url = "http://127.0.0.1:8080/api/lets_ride/share_travel_info/v1/"
headers = {"content-type": "application/json", \
           "Authorization": f"Bearer {access_token}"}
data = {
    "user_id": 8, "from_place": "Hyderabad",
    "to_place": "Visakhaptnam", "date_time": None,
    "flexible_timings": True,
    "start_date_time": "2020-08-27 05:06:27",
    "end_date_time": "2020-08-30 05:06:29",
    "travel_medium": "CAR", "assets_quantity": 1,
}
data = json.dumps(data)
response = requests.post(url=url, headers=headers, data=data)
print(response.content)
print("created successfully\n")

#-------------------create share travel info with flexible timings false------->
print("create share travel info with flexible timings false")
url = "http://127.0.0.1:8080/api/lets_ride/share_travel_info/v1/"
headers = {"content-type": "application/json", \
           "Authorization": f"Bearer {access_token}"}
data = {
    "user_id": 8, "from_place": "Hyderabad",
    "to_place": "Visakhaptnam", "date_time": "2020-08-27 05:06:27",
    "flexible_timings": False,
    "start_date_time": None,
    "end_date_time": None,
    "travel_medium": "CAR", "assets_quantity": 1,
}
data = json.dumps(data)
response = requests.post(url=url, headers=headers, data=data)
print(response.content)
print("created successfully\n")

print("create share travel info with assets quantity negative")
url = "http://127.0.0.1:8080/api/lets_ride/share_travel_info/v1/"
headers = {"content-type": "application/json", \
           "Authorization": f"Bearer {access_token}"}
data = {
    "user_id": 8, "from_place": "Hyderabad",
    "to_place": "Visakhaptnam", "date_time": "2020-08-27 05:06:27",
    "flexible_timings": False,
    "start_date_time": None,
    "end_date_time": None,
    "travel_medium": "CAR", "assets_quantity": -1,
}
data = json.dumps(data)
response = requests.post(url=url, headers=headers, data=data)
print(response.content)
