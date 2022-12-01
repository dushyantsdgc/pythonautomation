import json
import requests

payload=open("data.json","r").read()

resp=requests.post("https://reqres.in/api/users",data=json.loads(payload))
print(resp)
print(resp.json())
print(resp.headers)

assert resp.json()['job']=="trainee", "Job is not matching"