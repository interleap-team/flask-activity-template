# TODO Build the app.py file along with the template.html file to create a simple To-Do List app
# The app should have routes for adding a task, and should show a list of tasks
# Everything you have learned above will be useful for this task

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

class TodoItem:
    def __init__(self, content):
        self.content = content
        self.is_completed = False

task_list = []

@app.route('/')
def index():
    return render_template('home.html', tasks=task_list)

@app.route('/add', methods=['POST'])
def add_todo():
    item_content = request.form['task']
    task_list.append(TodoItem(item_content))
    return redirect(url_for('index'))

@app.route('/delete/<int:item_id>', methods=['POST'])
def remove_todo(item_id):
    if 0 <= item_id < len(task_list):
        task_list.pop(item_id)
    return redirect(url_for('index'))

@app.route('/complete/<int:item_id>', methods=['POST'])
def mark_complete(item_id):
    if 0 <= item_id < len(task_list):
        task_list[item_id].is_completed = True
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
