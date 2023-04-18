import pandas as pd
import datetime

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route("/index")
def index_test():
    return "helloworld index"


if __name__ == '__main__':
    print(__name__)
    app.run(host="localhost", port=8088)
# connection = pymysql.connect(user='root',
#                              password='helloworld',
#                              database='EssayChecker',
#                              host='localhost')

# start_date = datetime.datetime(2017, 11, 15)
# end_date = datetime.datetime(2017, 11, 16)

# try:
#     with connection.cursor() as cursor:
#         query = "SELECT * FROM EssayChecker"

#         cursor.execute(query)

#         print(cursor.description)
#         df = pd.DataFrame(data=cursor.fetchall())
# finally:
#     connection.close()

# print(df)