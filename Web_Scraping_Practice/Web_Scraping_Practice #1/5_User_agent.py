import requests
url = "http://naver.com"
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"}
res = requests.get(url, headers = headers)
res.raise_for_status()
with open("Practice.html", "w", encoding="utf8") as f:
    f.write(res.text)