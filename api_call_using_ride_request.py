import requests
import json

# invalid username
print("user login with invalid username")
url = "http://127.0.0.1:8080/api/lets_ride_auth/login/v1/"
headers = {"Content-Type": "application/json"}
data = '{"username":"test","password":"test", "name":"test", "mobile_number":"9876543210"}'
response = requests.post(url=url, headers=headers, data=data)
print(response.content)
print("\n")

# invalid password
print("user login with invalid password ")
url = "http://127.0.0.1:8080/api/lets_ride_auth/login/v1/"
headers = {"Content-Type": "application/json"}
data = '{"username":"test_1","password":"test", "name":"test", "mobile_number":"9876543210"}'
response = requests.post(url=url, headers=headers, data=data)
print(response.content)
print("\n")

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


#---------------------Ride Request--------------------------------------------->
#create ride request
print(" create ride request with flexible timings true")
url = "http://127.0.0.1:8080/api/lets_ride/ride_request/v1/"
headers={"content-type":"application/json",\
         "Authorization": f"Bearer {access_token}"}
data = {
        "user_id":8,"from_place": "Hyderabad",
        "to_place":"Visakhaptnam","date_time": None,
        "luggage_quantity":2,"no_of_seats":1,"flexible_timings":True,
        "start_date_time":"2020-08-27 05:06:27",
        "end_date_time":"2020-08-30 05:06:29"
        }
data = json.dumps(data)
response = requests.post(url=url, headers=headers, data=data)
print(response.content)
print("created successfully\n")

print("create ride request with flexible timings false")

url = "http://127.0.0.1:8080/api/lets_ride/ride_request/v1/"
headers={"content-type":"application/json",\
         "Authorization": f"Bearer {access_token}"}

data = {
        "user_id":8,"from_place": "Hyderabad",
        "to_place":"Visakhaptnam","date_time": "2020-08-27 05:06:27",
        "luggage_quantity":2,"no_of_seats":1,"flexible_timings":False,
        "start_date_time":None,
        "end_date_time":None
        }
data = json.dumps(data)
response = requests.post(url=url, headers=headers, data=data)
print(response.content)
print("created succeessfully\n")

print("create ride request with from place and to place are both same")
url = "http://127.0.0.1:8080/api/lets_ride/ride_request/v1/"
headers={"content-type":"application/json",\
         "Authorization": f"Bearer {access_token}"}

data = {
        "user_id":8,"from_place": "Hyderabad",
        "to_place":"Hyderabad","date_time": "2020-08-27 05:06:27",
        "luggage_quantity":2,"no_of_seats":1,"flexible_timings":False,
        "start_date_time":None,
        "end_date_time":None
        }
data = json.dumps(data)
response = requests.post(url=url, headers=headers, data=data)
print(response.content,"\n")

# create ride request with invalid date_time
print("create ride request date_time is in past")
url = "http://127.0.0.1:8080/api/lets_ride/ride_request/v1/"
headers={"content-type":"application/json",\
         "Authorization": f"Bearer {access_token}"}

data = {
        "user_id":8,"from_place": "Hyderabad",
        "to_place":"Visakhaptnam","date_time": "2020-05-27 05:06:27",
        "luggage_quantity":2,"no_of_seats":1,"flexible_timings":False,
        "start_date_time":None,
        "end_date_time":None
        }
data = json.dumps(data)
response = requests.post(url=url, headers=headers, data=data)
print(response.content)
print("\n")

# # create ride request with invalid start date time
print("create ride request with invalid start date time")
url = "http://127.0.0.1:8080/api/lets_ride/ride_request/v1/"
headers={"content-type":"application/json",\
         "Authorization": f"Bearer {access_token}"}

data = {
        "user_id":8,"from_place": "Hyderabad",
        "to_place":"Visakhaptnam","date_time": None,
        "luggage_quantity":2,"no_of_seats":1,"flexible_timings":True,
        "start_date_time":"2020-05-27 05:06:27",
        "end_date_time":"2020-07-27 05:06:27"
        }
data = json.dumps(data)
response = requests.post(url=url, headers=headers, data=data)
print(response.content)
print("\n")

print("create ride request with invalid start date time")
url = "http://127.0.0.1:8080/api/lets_ride/ride_request/v1/"
headers={"content-type":"application/json",\
         "Authorization": f"Bearer {access_token}"}

data = {
        "user_id":8,"from_place": "Hyderabad",
        "to_place":"Visakhaptnam","date_time": None,
        "luggage_quantity":2,"no_of_seats":1,"flexible_timings":True,
        "start_date_time":"2020-08-27 05:06:27",
        "end_date_time":"2020-07-27 05:06:27"
        }
data = json.dumps(data)
response = requests.post(url=url, headers=headers, data=data)
print(response.content,"\n")


# # create ride request with luggage quantity is -1
print("create ride request with luggage quantity is -1")
url = "http://127.0.0.1:8080/api/lets_ride/ride_request/v1/"
headers={"content-type":"application/json",\
         "Authorization": f"Bearer {access_token}"}

data = {
        "user_id":8,"from_place": "Hyderabad",
        "to_place":"Visakhaptnam","date_time": None,
        "luggage_quantity":-1,"no_of_seats":1,"flexible_timings":True,
        "start_date_time":"2020-08-27 05:06:27",
        "end_date_time":"2020-08-27 05:06:27"
        }
data = json.dumps(data)
response = requests.post(url=url, headers=headers, data=data)
print(response.content, "\n")


# # create ride request with no of seats is 0
print("create ride request with no of seats is 0")
url = "http://127.0.0.1:8080/api/lets_ride/ride_request/v1/"
headers={"content-type":"application/json",\
         "Authorization": f"Bearer {access_token}"}

data = {
        "user_id":8,"from_place": "Hyderabad",
        "to_place":"Visakhaptnam","date_time": None,
        "luggage_quantity":0,"no_of_seats":0,"flexible_timings":True,
        "start_date_time":"2020-08-27 05:06:27",
        "end_date_time":"2020-08-27 05:06:27"
        }
data = json.dumps(data)
response = requests.post(url=url, headers=headers, data=data)
print(response.content, "\n")


# # create ride request with no of seats is -1
print("create ride request with no of seats is -1")
url = "http://127.0.0.1:8080/api/lets_ride/ride_request/v1/"
headers={"content-type":"application/json",\
         "Authorization": f"Bearer {access_token}"}

data = {
        "user_id":8,"from_place": "Hyderabad",
        "to_place":"Visakhaptnam","date_time": None,
        "luggage_quantity":0,"no_of_seats":-1,"flexible_timings":True,
        "start_date_time":"2020-08-27 05:06:27",
        "end_date_time":"2020-08-27 05:06:27"
        }
data = json.dumps(data)
response = requests.post(url=url, headers=headers, data=data)
print(response.content, "\n")

