from flask import render_template, request, redirect, url_for
from . import db
from .models import Task

@app.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    title = request.form.get('title')
    new_task = Task(title=title)
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/complete/<id>')
def complete(id):
    task = Task.query.get(id)
    task.complete = not task.complete
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<id>')
def delete(id):
    task = Task.query.get(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))
