import requests
import pandas as pd
import time
from bs4 import BeautifulSoup
from tqdm import tqdm
import concurrent.futures
import urllib.request

PACKAGES = []

URLS = []


def download_q_reports():
    global URLS
    df = pd.read_csv('courses.csv')
    urls = df.link.tolist()
    URLS = df.link.tolist()
    fas_codes = df.fas_code.tolist()
    for i in range(len(urls)):
        PACKAGES.append([urls[i], fas_codes[i]])
    # enrolled = []
    # with requests.Session() as s:
    #     for url in tqdm(urls):
    #         page = s.get(url)
    #         # soup = BeautifulSoup(page.text, 'html.parser')
    #         # enrolled.append(soup.find_all('td')[1].text)
    #         time.sleep(10)
    # df['enrolled'] = enrolled
    # pd.to_csv('course_enrollment.csv')


download_q_reports()

RESULTS = {}
# PACKAGES= PACKAGES[:10]
global_count = 0


# Retrieve a single page and report the URL and contents
def load_url(package, timeout):
    global global_count
    url = package[0]
    fas_code = package[1]
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    result = soup.find_all('td')[1].text
    RESULTS[fas_code] = result
    global_count += 1
    print(global_count / 1300 * 100)


# We can use a with statement to ensure threads are cleaned up promptly
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    # Start the load operations and mark each future with its URL
    future_to_url = {executor.submit(load_url, url, 60): url for url in PACKAGES}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
        except Exception as exc:
            print('%r generated an exception: %s' % (url, exc))
        else:
            pass
            # print('%r page is %d bytes' % (url, len(data)))
    print("done")
    pd.DataFrame(RESULTS.items()).to_csv('reported_enrolment.csv', index=False)
