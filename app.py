from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    details = db.Column(db.String(100))

#@app.route("/")
#def index():
#    tasks = Todo.query.all()
#    return render_template("index.html", tasks = tasks) 


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        tasks = Todo.query.all()
        return render_template('index.html', tasks = tasks)

    else:
        title = request.form.get('title')
        details = request.form.get('details')

        new_task = Todo(title = title, details = details)

        db.session.add(new_task)
        db.session.commit()
        return redirect('/')


@app.route('/create')
def create():
    return render_template('create.html')

#@app.route("/create", methods=["POST"])
#def create():
#    title = request.form.get("title")
#    details = request.form.get("details")
#   new_task = Todo(title = title, details = details)

#    db.session.add(new_task)
#    db.session.commit()
#    return redirect("/")

#@app.route("/create", methods=['GET', "POST"])
#def create():
#    render_template('create.html')
#    if request.method == 'GET':
#        task = Todo.query.all()
#        return render_template('index.html', task = task)

#    else:
#       title = request.form.get('title')
#        details = request.form.get('details')

#        new_task = Todo(title=title, details=details)

 #       db.session.add(new_task)
  #      db.session.commit()
   #     return redirect('/')


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    update_task = Todo.query.get(id)
    if request.method == 'GET':
        return render_template('update.html', task = update_task)
    else:
        update_task.title = request.form.get('title')
        update_task.details = request.form.get('details')

        db.session.commit()
        return redirect('/')


@app.route('/delete/<int:id>')
def delete(id):
    delete_task = Todo.query.get(id)

    db.session.delete(delete_task)
    db.session.commit()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)