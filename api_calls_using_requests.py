import requests
import json

# invalid username
print("user login with invalid username")
url = "http://127.0.0.1:8080/api/lets_ride_auth/login/v1/"
headers = {"Content-Type": "application/json"}
data = '{"username":"test","password":"test", "name":"test", "mobile_number":"9876543210"}'
response = requests.post(url=url, headers=headers, data=data)
print(response.content)
print("\n\n")

# invalid password
print("user login with invalid password ")
url = "http://127.0.0.1:8080/api/lets_ride_auth/login/v1/"
headers = {"Content-Type": "application/json"}
data = '{"username":"test_1","password":"test", "name":"test", "mobile_number":"9876543210"}'
response = requests.post(url=url, headers=headers, data=data)
print(response.content)
print("\n\n")

# valid details
print("user log in with valid datails")
url = "http://127.0.0.1:8080/api/lets_ride_auth/login/v1/"
headers = {"Content-Type": "application/json"}
data = '{"username":"test_1","password":"tesr@1234", "name":"test", "mobile_number":"9876543210"}'
response = requests.post(url=url, headers=headers, data=data)
print(response.content)
print("\n\n")


print(" create ride request with flexible timings true")
url = "http://127.0.0.1:8080/api/lets_ride/ride_request/v1/"
headers={"content-type":"application/json",\
         "Authorization": "Bearer kAP4c5XzmTJW9E8X1tDNJY6b3BPrvX"}
data = {
        "user_id":8,"from_place": "Hyderabad",
        "to_place":"Visakhaptnam","date_time": None,
        "luggage_quantity":2,"no_of_seats":1,"flexible_timings":True,
        "start_date_time":"2020-07-27 05:06:27",
        "end_date_time":"2020-08-30 05:06:29"
        }
data = json.dumps(data)
response = requests.post(url=url, headers=headers, data=data)
print(response.content)
print("created successfully\n\n")

print("create ride request with flexible timings false")

url = "http://127.0.0.1:8080/api/lets_ride/ride_request/v1/"
headers={"content-type":"application/json",\
         "Authorization": "Bearer kAP4c5XzmTJW9E8X1tDNJY6b3BPrvX"}

data = {
        "user_id":8,"from_place": "Hyderabad",
        "to_place":"Visakhaptnam","date_time": "2020-07-27 05:06:27",
        "luggage_quantity":2,"no_of_seats":1,"flexible_timings":False,
        "start_date_time":None,
        "end_date_time":None
        }
data = json.dumps(data)
response = requests.post(url=url, headers=headers, data=data)
print(response.content)
print("created succeessfully\n\n")


# create ride request with invalid date_time
url = "http://127.0.0.1:8080/api/lets_ride/ride_request/v1/"
headers={"content-type":"application/json",\
         "Authorization": "Bearer kAP4c5XzmTJW9E8X1tDNJY6b3BPrvX"}

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

# # create ride request with invalid start date time
url = "http://127.0.0.1:8080/api/lets_ride/ride_request/v1/"
headers={"content-type":"application/json",\
         "Authorization": "Bearer kAP4c5XzmTJW9E8X1tDNJY6b3BPrvX"}

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


# # create ride request with luggage quantity is -1
url = "http://127.0.0.1:8080/api/lets_ride/ride_request/v1/"
headers={"content-type":"application/json",\
         "Authorization": "Bearer kAP4c5XzmTJW9E8X1tDNJY6b3BPrvX"}

data = {
        "user_id":8,"from_place": "Hyderabad",
        "to_place":"Visakhaptnam","date_time": None,
        "luggage_quantity":-1,"no_of_seats":1,"flexible_timings":True,
        "start_date_time":"2020-07-27 05:06:27",
        "end_date_time":"2020-07-27 05:06:27"
        }
data = json.dumps(data)
response = requests.post(url=url, headers=headers, data=data)
print(response.content)


# # create ride request with no of seats is 0
url = "http://127.0.0.1:8080/api/lets_ride/ride_request/v1/"
headers={"content-type":"application/json",\
         "Authorization": "Bearer kAP4c5XzmTJW9E8X1tDNJY6b3BPrvX"}

data = {
        "user_id":8,"from_place": "Hyderabad",
        "to_place":"Visakhaptnam","date_time": None,
        "luggage_quantity":0,"no_of_seats":0,"flexible_timings":True,
        "start_date_time":"2020-07-27 05:06:27",
        "end_date_time":"2020-07-27 05:06:27"
        }
data = json.dumps(data)
response = requests.post(url=url, headers=headers, data=data)
print(response.content)


# # create ride request with no of seats is -1
url = "http://127.0.0.1:8080/api/lets_ride/ride_request/v1/"
headers={"content-type":"application/json",\
         "Authorization": "Bearer kAP4c5XzmTJW9E8X1tDNJY6b3BPrvX"}

data = {
        "user_id":8,"from_place": "Hyderabad",
        "to_place":"Visakhaptnam","date_time": None,
        "luggage_quantity":0,"no_of_seats":-1,"flexible_timings":True,
        "start_date_time":"2020-07-27 05:06:27",
        "end_date_time":"2020-07-27 05:06:27"
        }
data = json.dumps(data)
response = requests.post(url=url, headers=headers, data=data)
print(response.content)


# create share ride with flexible timings true
url = "http://127.0.0.1:8080/api/lets_ride/share_ride/v1/"
headers={"content-type":"application/json",\
         "Authorization": "Bearer kAP4c5XzmTJW9E8X1tDNJY6b3BPrvX"}

data = {
        "user_id":8,"from_place": "Hyderabad",
        "to_place":"Visakhaptnam","date_time": None,
        "assets_quantity":0,"no_of_seats_available":1,"flexible_timings":True,
        "start_date_time":"2020-07-27 05:06:27",
        "end_date_time":"2020-07-27 05:06:27"
        }
data = json.dumps(data)
response = requests.post(url=url, headers=headers, data=data)
print(response.content)


# create share ride with flexible timings flase
url = "http://127.0.0.1:8080/api/lets_ride/share_ride/v1/"
headers={"content-type":"application/json",\
         "Authorization": "Bearer kAP4c5XzmTJW9E8X1tDNJY6b3BPrvX"}

data = {
        "user_id":8,"from_place": "Hyderabad",
        "to_place":"Visakhaptnam","date_time": "2020-07-27 05:06:27",
        "assets_quantity":0,"no_of_seats_available":1,"flexible_timings":False,
        "start_date_time":None,
        "end_date_time":None
        }
data = json.dumps(data)
response = requests.post(url=url, headers=headers, data=data)
print(response.content)