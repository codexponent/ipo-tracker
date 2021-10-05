import requests
import nepali_datetime
from bs4 import BeautifulSoup

URL = "https://merolagani.com/Ipo.aspx?type=upcoming"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
elements = soup.find_all("div", class_="media-body")
title_element = elements[0].find("a")
print(title_element.text.strip()+ ". Today is "+nepali_datetime.date.today().strftime("%d %B %Y"))