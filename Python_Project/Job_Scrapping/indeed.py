import requests
from bs4 import BeautifulSoup

limit = 50
url = f"https://www.indeed.com/jobs?q=python&l=Springfield%2C+VA&limit={limit}&radius=25"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"}


def get_last_pages():

    result = requests.get(url, headers=headers)
    soup = BeautifulSoup(result.text, 'html.parser')

    pagination = soup.find("div", attrs={"class": "pagination"})
    links = pagination.find_all("a")

    pages = []

    for link in links[:-1]:
        pages.append(int(link.string))

    max_page = pages[-1]
    return max_page


def extract_job(job_info):

    title = job_info.find(
        "h2", attrs={"class": "title"}).find("a")["title"]
    company = job_info.find(
        "span", attrs={"class": "company"})

    company_anchor = company.find("a")

    if company:
        if company_anchor is not None:
            company = company_anchor.string
        else:
            company = company.string
        company = company.strip()
    else:
        company = None

    location = job_info.find("div", attrs={"class": "recJobLoc"})[
        "data-rc-loc"]
    job_id = job_info["data-jk"]
    link = f"https://www.indeed.com/viewjob?jk={job_id}&q=python&l=Springfield%2C+VA&tk=1f7p7rd5rs9v5802&from=web&vjs=3"

    return {
        'title': title,
        'company': company,
        'location': location,
        'link': link
    }


def extract_indeed_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping Indeed Pages {page+1}")
        result = requests.get(f"{url}&start={page*limit}")
        soup = BeautifulSoup(result.text, 'html.parser')

        job_lists = soup.find_all(
            "div", attrs={"class": "jobsearch-SerpJobCard"})

        for job_list in job_lists:
            job = extract_job(job_list)
            jobs.append(job)

    return jobs


def get_jobs():
    last_page = get_last_pages()
    jobs = extract_indeed_jobs(last_page)
    return jobs
