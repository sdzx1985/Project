import requests
res = requests.get("http://naver.com")
print("response : ", res.status_code) #200 - normal

if res.status_code == requests.codes.ok:
    print("Works")
else:
    print("Does not work" )