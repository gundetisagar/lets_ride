
#Invalid Username
curl -d '{"username":"test_","password":"test@1234"}' -H "Content-type: application/json" http://127.0.0.1:8080/api/lets_ride_auth/login/v1/


# Invalid Password
curl -d '{"username":"test_2","password":"test1234"}' -H "Content-type: application/json" http://127.0.0.1:8080/api/lets_ride_auth/login/v1/


# valid username and password
curl -d '{"username":"test_2","password":"test@1234"}' -H "Content-type: application/json" http://127.0.0.1:8080/api/lets_ride_auth/login/v1/


