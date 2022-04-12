import imp
from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__) # this file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' # three /// are a relative path, four absloute.
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Task {self.id}>'

# to be created from python shell (or by checking existance)

#hello world

@app.route('/', methods=['POST', 'GET']) # make interactions with DB
def index():
    # the return indicates what will visualized on screen
    if request.method == 'POST':
        task_content = request.form['content'] # get input
        new_task = Todo(content=task_content)
        try: # push to database
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'An error has occurred processing your request'
    else:

        # query
        tasks = Todo.query.order_by(Todo.date_created).all()
        # pass to template
        return render_template('DB_App.html', tasks=tasks) # from index.html (load an html page)

@app.route('/delete/<int:id>') # as a sort of webpage
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        # except redirect...
        return 'An error has occurred deleting your entry'

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)

    if request.method == 'POST':
        task_content = request.form['content'] # get input
        task.content = task_content
        try: # push to database
            db.session.commit()
            return redirect('/')
        except:
            return 'An error has occurred processing your request'
    else:
        # pass to template
        return render_template('update.html', task=task) # from index.html (load an html page)
    


if __name__ == "__main__":
    app.run(debug=True)