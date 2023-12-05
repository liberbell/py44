from bs4 import BeautifulSoup
import requests

URL = "https://scraping-for-beginner.herokuapp.com/udemy"
data = requests.get(URL)
# print(data.text)

soup = BeautifulSoup(data.text, "html.parser")

print(soup.select(".card-title")[0].string)