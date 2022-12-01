import requests

payload={
    "name": "Dushyant",
    "Job": "QA Engineer"
    }

resp=requests.post("https://reqres.in/api/users",data=payload)
print(resp)
print(resp.json())
assert resp.json()['Job']=='QA Engineer', "Job is not matched"
