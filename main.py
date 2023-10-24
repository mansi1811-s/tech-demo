from flask import Flask
app = Flask(__name__)

password = "xyz"

@app.route("/")
def hello():
    print(password)
    return "Hello, This is CodeQL demo!"

if __name__ == "__main__":
    app.run()
