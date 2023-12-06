from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime

URL = "https://scraping-for-beginner.herokuapp.com/udemy"
# data = requests.get(URL)
# print(data.text)

# soup = BeautifulSoup(data.text, "html.parser")

# name = soup.select(".card-title")[0].string
# num_of_student = soup.select(".subscribers")[0].string
# num_of_student = int(num_of_student.split("：")[1])
# print(type(num_of_student), num_of_student)

# num_of_reviews = soup.select(".reviews")[0].string
# num_of_reviews = int(num_of_reviews.split("：")[1])
# print(type(num_of_reviews), num_of_reviews)

# results = {
#     "name": name,
#     "num_of_students": num_of_student,
#     "num_of_reviews": num_of_reviews,
# }
# print(results)

# df = pd.read_csv("assets/data.csv")
# print(df.tail())

# date = datetime.datetime.today().strftime("%Y/%-m/%-d")

# subscribers = results["num_of_students"]
# reviews = results["num_of_reviews"]

# results = pd.DataFrame([[date, subscribers, reviews]], columns=["date", "subscribers", "reviews"])
# print(results)

# df = pd.concat([df, results])
# print(df.tail())

# df.to_csv("assets/data.csv", index=False)

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