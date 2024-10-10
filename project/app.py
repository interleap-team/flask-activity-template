from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

class ToDoItem:
    def __init__(self, content):
        self.content = content
        self.is_completed = False

task_list = []

@app.route('/')
def index():
    return render_template('home.html', tasks=task_list)

@app.route('/add_task', methods=['POST'])
def add_task():
    new_task_content = request.form['task']
    if new_task_content:  # Ensure the task is not empty
        task_list.append(ToDoItem(new_task_content))
    return redirect(url_for('index'))

@app.route('/remove/<int:item_id>', methods=['POST'])
def remove_task(item_id):
    if 0 <= item_id < len(task_list):
        task_list.pop(item_id)
    return redirect(url_for('index'))

@app.route('/mark_complete/<int:item_id>', methods=['POST'])
def mark_as_complete(item_id):
    if 0 <= item_id < len(task_list):
        task_list[item_id].is_completed = True
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)