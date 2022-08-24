from datetime import datetime
from turtle import title
from flask import Flask, redirect, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.before_first_request
def create_tables():
    db.create_all()

datetime_obj = datetime.now()

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(50), nullable = False)
    desc = db.Column(db.String(200), nullable = False)
    date = db.Column(db.DateTime, default = datetime_obj)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/services')
def serv():
    return render_template('services.html')

@app.route('/contact')
def cont():
    return render_template('contact.html')

# @app.route('/tasks', methods=['GET', 'POST'])
@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
    if request.method == 'POST':
        title  = request.form['title']
        desc  = request.form['descr']
        todo = Todo(title=title, desc=desc)
        try:
            db.session.add(todo)
            db.session.commit()
            return redirect('/tasks')
        except:
            return 'Error adding new task. Please try again.'
    else:
        allTodo = Todo.query.order_by(Todo.date).all()
        return render_template('tasks.html', allTodo = allTodo)

@app.route('/tasks/delete/<int:sno>')
def delete(sno):
    # dlt_task = Todo.query.get_or_404(sno)
    dlt_task = Todo.query.filter_by(sno = sno).first()

    try:
        db.session.delete(dlt_task)
        db.session.commit()
        return redirect('/tasks')
    except:
        return 'Error deleting the task. Please try again.'


@app.route('/tasks/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    upd_task = Todo.query.get_or_404(sno)

    if request.method == 'POST':
        upd_task.title = request.form['title']
        upd_task.desc = request.form['descr']
        try:
            db.session.commit()
            return redirect('/tasks')
        except:
            return 'Error updating task. Please try again.'
    else:
        return render_template('update.html', upd_task = upd_task)


@app.route('/account/<string:name>')
def acc(name):
    return render_template('account.html', usrname = name)

if __name__ == '__main__':
    app.run(debug=True, port=100)
