import requests

payload={
    "name": "Dushyant",
    "Job": "zion resident"
    }

resp=requests.patch("https://reqres.in/api/users/2",data=payload)
print(resp)
print(resp.json())
assert resp.json()['Job']=='zion resident', "Job is not matched"