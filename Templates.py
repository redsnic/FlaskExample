from flask import Flask, render_template

app = Flask(__name__) # this file

#hello world

@app.route('/')
def index():
    return render_template('using_first_template.html') # from index.html (load an html page)

if __name__ == "__main__":
    app.run(debug=True)