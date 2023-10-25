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

# import mysql.connector

# with mysql.connector.connect(user='user', password='password', host='host', database='database') as conn:
#     cursor = conn.cursor()
    
#     name = "John"
#     query = "SELECT * FROM users WHERE name = %s"
#     cursor.execute(query, (name,))
#     rows = cursor.fetchall()


import mysql.connector

with mysql.connector.connect(user='user', password='password', host='host', database='database') as conn:
    cursor = conn.cursor()

    name = "John"

    # Sanitize and validate user input
    if "'" in name:  # Check for single quotes (') in the input
        raise ValueError("Invalid input")

    query = "SELECT * FROM users WHERE name = %s" % name  # Directly incorporate sanitized input
    cursor.execute(query)
    rows = cursor.fetchall()
