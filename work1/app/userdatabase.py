from assets.database import db_session
from assets.database import init_db
from assets.models import Data
import datetime

# init_db()
date = datetime.date.today()
# print(date)

row = Data(date=date, subscribers=3500, reviews=200)
# print(row.date)

# db_session.add(row)
# db_session.commit()

row1 = Data(date=date, subscribers=3700, reviews=210)
row2 = Data(date=date, subscribers=3900, reviews=190)

# db_session.add(row1, row2)
# db_session.commit()

datam = db_session.query(Data).all()[1]
print(datam)
datam.subscribers = 13500
print(datam.subscribers)
db_session.add(datam)
db_session.commit()