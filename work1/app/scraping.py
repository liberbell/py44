from bs4 import BeautifulSoup
import requests
import datetime
from assets.database import db_session
from assets.models import Data

URL = "https://scraping-for-beginner.herokuapp.com/udemy"

def get_udemy_info():
    data = requests.get(URL)
    soup = BeautifulSoup(data.text, "html.parser")

    name = soup.select(".card-title")[0].string

    num_of_student = soup.select(".subscribers")[0].string
    num_of_student = int(num_of_student.split("：")[1])

    num_of_reviews = soup.select(".reviews")[0].string
    num_of_reviews = int(num_of_reviews.split("：")[1])

    results = {
        "name": name,
        "num_of_students": num_of_student,
        "num_of_reviews": num_of_reviews,
    }
    return results

def write_data():
    _results = get_udemy_info()

    date = datetime.date.today()
    subscribers = _results["num_of_students"]
    reviews = _results["num_of_reviews"]

    row = Data(date=date, subscribers=subscribers, reviews=reviews)

if __name__ == "__main__":
    write_data()