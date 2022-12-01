import requests

resp = requests.get("https://reqres.in/api/users?page=2")
print(resp)
code=resp.status_code
print(code)
assert code == 200, "Status code not matched"

# print(resp.text)
# print(resp.content)

# print(resp.json())
# http://jsonviewer.stack.hu/

# print(resp.headers)
# print(resp.cookies)
# print(resp.encoding)
# print(resp.url)

json_response = resp.json()
print(json_response['total'])
assert json_response['total']==12, "Total pages are not matching"
print(json_response['total_pages'])
assert json_response['total_pages']==2, "Total user count is not matching"
print(json_response['data'][0]['email'])
assert json_response['data'][0]['email'].endswith("reqres.in"), "Email is not matching"
print(json_response['data'][2]['last_name'])
assert json_response['data'][2]['last_name']!='none'







