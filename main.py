# from flask import Flask
# from decouple import config 
# app = Flask(__name__)

# #passing password as environment variable
# password = config('PASSWORD')

# # #password in plain text
# # password = "xyz"

# @app.route("/")
# def hello():
#     print(password)
#     return "Hello, This is CodeQL demo!"

# if __name__ == "__main__":
#     app.run()

import mysql.connector

with mysql.connector.connect(user='user', password='password', host='host', database='database') as conn:
    cursor = conn.cursor()
    
    name = "John"
    query = "SELECT * FROM users WHERE name = %s"
    cursor.execute(query, (name,))
    rows = cursor.fetchall()
