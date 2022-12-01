import requests

resp = requests.get("https://the-internet.herokuapp.com/basic_auth",auth=("admin","admin"))
print(resp)
print(resp.status_code)
print(resp.headers)
print(resp.cookies)

