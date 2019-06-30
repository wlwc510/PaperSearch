import requests
from bs4 import BeautifulSoup
import socket
import time
url = "https://www.nature.com/subjects/physical-sciences/ncomms?searchType=journalSearch&sort=PubDate&page=2"
# url = "https://www.nature.com/ncomms/"
response = requests.get(url)
requests.DEFAULT_RETRIES = 5
t_default=20
socket.setdefaulttimeout(t_default)
sleep_download_time = 10
time.sleep(sleep_download_time)
soup = BeautifulSoup(response.text,'lxml')
print(soup.prettify())
response.close()