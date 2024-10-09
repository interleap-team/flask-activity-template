from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

tasks = []

@app.route('/')
def home():
    return render_template('home.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task_description = request.form['task']
    tasks.append(Task(task_description))
    return redirect(url_for('home'))

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for('home'))

@app.route('/complete/<int:task_id>', methods=['POST'])
def complete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id].completed = True
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
