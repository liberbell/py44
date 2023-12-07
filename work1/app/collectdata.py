from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime

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
    df = pd.read_csv("assets/data.csv")
    _results = get_udemy_info()

    date = datetime.datetime.today().strftime("%Y/%-m/%-d")
    subscribers = _results["num_of_students"]
    reviews = _results["num_of_reviews"]

    results = pd.DataFrame([[date, subscribers, reviews]], columns=["date", "subscribers", "reviews"])
    df = pd.concat([df, results])

    df.to_csv("assets/data.csv", index=False)


df = pd.read_csv("assets/data.csv")
# print(df.head())
# print(type(df["date"][0]))

date = datetime.datetime.strptime(df["date"][0], "%Y/%m/%d").date()
print(date)
print(type(date))