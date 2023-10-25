# from flask import Flask
# # from decouple import config 
# app = Flask(__name__)

# # #passing password as environment variable
# # password = config('PASSWORD')

# #password in plain text
# password = "xyz"

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


import sqlite3

def get_user_data(username):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    #Correct code without vulnerability
    # query = "SELECT * FROM users WHERE username = ?"

    #Directly concatenating user input into SQL query -CVE-2018-6829
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)

    user_data = cursor.fetchall()
    conn.close()
    return user_data

username = input("Enter a username: ")
user_data = get_user_data(username)
print(user_data)
