from assets.database import db_session
from assets.database import init_db
from assets.models import Data
import datetime

# init_db()
date = datetime.date.today()
# print(date)

row = Data(date=date, subscribers=3500, reviews=200)
# print(row.date)

db_session.add(row)
db_session.commit()