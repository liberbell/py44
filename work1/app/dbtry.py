from assets import models
import pandas as pd

from assets.database import db_session
import datetime

df = pd.read_csv("assets/data.csv")
print(df.head())

print(type(df.iloc[0,0]))
date = datetime.datetime.strptime(df.iloc[0,0], "%Y/%m/%d").date()
print(date)
print(type(date))

for index, _df in df.iterrows():
    date = datetime.datetime.strptime(_df["date"], "%Y/%m/%d").date()
    row = models.Data(date=date, subscribers=_df["subscribers"], reviews=_df["reviews"])