from flask import Flask
app = Flask(__name__)

#password in plain text
password = "xyz"

@app.route("/")
def hello():
    print(password)
    return "Hello, This is CodeQL demo!"

if __name__ == "__main__":
    app.run()
