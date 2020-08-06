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

print("get user profile")
url = "http://127.0.0.1:8080/api/lets_ride_auth/user_profile/v1/"
headers={"content-type":"application/json",\
         "Authorization": f"Bearer {access_token}"}
# data = '{"username":"test_1","password":"tesr@1234", "name":"test", "mobile_number":"9876543210"}'
response = requests.post(url=url, headers=headers)
print(response.content)
# token_details = json.loads(response.content)
# access_token = str(token_details["access_token"])
# print(access_token)
print("\n")
