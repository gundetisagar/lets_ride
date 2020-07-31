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

# create share ride with flexible timings true
print("create share ride with flexible timings true")
url = "http://127.0.0.1:8080/api/lets_ride/share_ride/v1/"
headers={"content-type":"application/json",\
         "Authorization": f"Bearer {access_token}"}

data = {
        "user_id":8,"from_place": "Hyderabad",
        "to_place":"Visakhaptnam","date_time": None,
        "assets_quantity":0,"no_of_seats_available":1,"flexible_timings":True,
        "start_date_time":"2020-08-27 05:06:27",
        "end_date_time":"2020-08-27 05:06:27"
        }
data = json.dumps(data)
response = requests.post(url=url, headers=headers, data=data)
print(response.content, "created successfully\n")


# create share ride with flexible timings flase
print("create share ride with flexible timings flase")
url = "http://127.0.0.1:8080/api/lets_ride/share_ride/v1/"
headers={"content-type":"application/json",\
         "Authorization": f"Bearer {access_token}"}

data = {
        "user_id":8,"from_place": "Hyderabad",
        "to_place":"Visakhaptnam","date_time": "2020-08-27 05:06:27",
        "assets_quantity":0,"no_of_seats_available":1,"flexible_timings":False,
        "start_date_time":None,
        "end_date_time":None
        }
data = json.dumps(data)
response = requests.post(url=url, headers=headers, data=data)
print(response.content,"created successfully", "\n")