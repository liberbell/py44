from bs4 import BeautifulSoup
import requests

URL = "https://scraping-for-beginner.herokuapp.com/udemy"
data = requests.get(URL)
print(data.status_code)