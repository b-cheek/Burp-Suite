import requests
from bs4 import BeautifulSoup

# r=requests.get('https://google.com')
# for i in r.headers:
#     print (i)
#     print(r.headers[i])


response = requests.get('https://acef1f7b1fa70c4280b012dc00ad00c2.web-security-academy.net/login')
soup = BeautifulSoup(response.text, 'lxml')
csrf_token = soup.find('input', {'name':'csrf'})['value']
print("CSRF TOKEN:", csrf_token)
# for i in response.headers:
#    print (i)
#    print("---------------")
#    print(response.headers[i])
#    print()

payload = {"csrf": csrf_token, "username": "carlos", "password": "montoya"}
print(payload)
response = requests.post('https://acef1f7b1fa70c4280b012dc00ad00c2.web-security-academy.net/login', data=payload)
print(response.text)
