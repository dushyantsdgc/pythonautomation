import requests

resp = requests.get("http://httpbin.org/delay/5",timeout=3)
print(resp)
print(resp.status_code)

