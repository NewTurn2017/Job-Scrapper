from bs4 import BeautifulSoup
import requests


def extract_remoteok_jobs(term):
    url = f"https://remoteok.com/remote-{term}-jobs"
    request = requests.get(url, headers={"User-Agent": "Kimchi"})
    if request.status_code == 200:
        soup = BeautifulSoup(request.text, "html.parser")
        table_body = soup.find("table", id="jobsboard")
        jobs = table_body.find_all("tr", class_="job")
        results = []
        for job in jobs:
            td = job.find_all("td", class_="company")
            anchor = td[0].find(["a"])
            link = anchor["href"]
            job_url = f"https://remoteok.com{link}"
            company = job.find("h3", itemprop="name")
            position = job.find("h2", itemprop="title")
            location = job.find("div", class_="location")

            if company:
                company = company.string.strip().replace(",", " ")
            if position:
                position = position.string.strip().replace(",", " ")
            if location:
                location = location.string.strip().replace(",", " ")

            if company and position and location:
                job_data = {
                    "link": job_url,
                    "company": company,
                    "location": location,
                    "position": position,
                }
                results.append(job_data)
        return results
    else:
        return "Can't get jobs."
