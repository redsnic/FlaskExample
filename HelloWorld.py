from flask import Flask

app = Flask(__name__) # this file

#hello world

@app.route('/')
def index():
    return "Hello world!"

if __name__ == "__main__":
    app.run(debug=True)