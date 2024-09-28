from flask import Flask

app = Flask(__name__)

@app.route('/')
def custom_port():
    return 'Running on a custom port!'

port = 8080

if __name__ == '__main__':
    app.run(port=port)