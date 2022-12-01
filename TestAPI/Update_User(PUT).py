import requests

payload={
    "name": "Dushyant",
    "Job": "Tester"
    }

resp=requests.put("https://reqres.in/api/users/2",data=payload)
print(resp)
print(resp.json())
assert resp.json()['Job']=='Tester', "Job is not matched"