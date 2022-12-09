from requests import get
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
Options.add_argument("--no-sandbox")
Options.add_argument("--disable-dev-shm-usage")

browser = webdriver.Chrome(options=options)

browser = get("https://www.indeed.com/jobs?q=python&limit=50")


print(browser.text)
# if response.status_code != 200:
#     print("Cant request page")
# else:
#     soup = BeautifulSoup(response.text, "html.parser")
#     job_list = soup.find("ul", class_="jobsearch-ResultsList")
#     jobs = job_list.find_all("li", recursive=False)
#     print(len(jobs))
