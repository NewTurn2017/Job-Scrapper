from bs4 import BeautifulSoup
import requests


def extract_jobs(term):
    url = f"https://remoteok.com/remote-{term}-jobs"
    request = requests.get(url, headers={"User-Agent": "Kimchi"})
    if request.status_code == 200:
        soup = BeautifulSoup(request.text, "html.parser")
        table_body = soup.find("table", id="jobsboard")
        jobs = table_body.find_all("tr", class_="job")
        results = []
        for job in jobs:
            infos = []
            td = job.find_all("td", class_="company")
            anchor = td[0].find(["a"])
            link = anchor["href"]
            job_url = f"https://remoteok.com{link}"
            title = anchor.find("h2").string.strip()
            company = td[0].find("span", class_="companyLink").find("h3").string.strip()
            locations = td[0].find_all("div", class_="location")
            for info in locations:
                infos.append(info.string)

            job_data = {
                "link": job_url,
                "title": title,
                "company": company,
                "infos": infos,
            }
            results.append(job_data)
        print(results)
    else:
        print("Can't get jobs.")


extract_jobs("rust")
