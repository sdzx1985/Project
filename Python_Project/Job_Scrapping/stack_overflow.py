import requests
from bs4 import BeautifulSoup


url = "https://stackoverflow.com/jobs?q=python&l=Springfield%2C+VA%2C+USA&d=20&u=Miles"
# url = f"https://stackoverflow.com/jobs?q=python&sort=i"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"}


def get_last_pages():
    result = requests.get(url, headers=headers)
    soup = BeautifulSoup(result.text, 'html.parser')
    pages = soup.find("div", attrs={"class": "s-pagination"}).find_all("a")
    last_page = pages[-2].get_text(strip=True)
    return int(last_page)


def extract_job(job_info):
    title = job_info.find("h2", attrs={"class": "mb4"}).find("a")["title"]
    company, location = job_info.find(
        "h3", attrs={"class": "fc-black-700"}).find_all("span", recursive=False)
    company = company.get_text(strip=1)
    location = location.get_text(strip=1)
    job_id = job_info['data-jobid']

    return {'title': title, 'company': company, 'location': location, 'apply_link': f"https://stackoverflow.com/jobs/{job_id}"}


def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping Stack Overflow Pages {page+1}")
        result = requests.get(f"{url}&pg={page+1}", headers=headers)
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", attrs={"class": "-job"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs


def get_jobs():
    last_page = get_last_pages()
    jobs = extract_jobs(last_page)
    return jobs
