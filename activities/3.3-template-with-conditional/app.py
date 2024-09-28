from flask import Flask, render_template

app = Flask(__name__)

@app.route('/status/<status>')
def status(status):
    return render_template('status.html', status=status)

if __name__ == '__main__':
    app.run(debug=False)