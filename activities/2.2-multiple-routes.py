from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Home Page"

@app.route('/about')
def about():
    return "About Page"

if __name__ == '__main__':
    app.run(debug=False)