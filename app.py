from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_
from datetime import datetime

app = Flask(__name__)
# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Task Model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    due_date = db.Column(db.String(10), nullable=True) # YYYY-MM-DD
    status = db.Column(db.String(50), nullable=False, default='Pending') # Pending, In Progress, Completed
    remarks = db.Column(db.Text, nullable=True)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)
    updated_on = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    created_by = db.Column(db.String(100), nullable=True)
    updated_by = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return f'<Task {self.id} - {self.title}>'

@app.route('/', methods=['GET'])
def index():
    query_string = request.args.get('q', '')
    status_filter = request.args.get('status', '')
    
    sort_by = request.args.get('sort', '')
    
    tasks_query = Task.query
    
    if query_string:
        search_term = f"%{query_string}%"
        tasks_query = tasks_query.filter(
            or_(
                Task.title.ilike(search_term),
                Task.description.ilike(search_term),
                Task.remarks.ilike(search_term),
                Task.created_by.ilike(search_term),
                Task.updated_by.ilike(search_term)
            )
        )
    
    if status_filter:
        tasks_query = tasks_query.filter(Task.status == status_filter)
        
    if sort_by == 'date_asc':
        tasks_query = tasks_query.order_by(Task.due_date.asc())
    elif sort_by == 'date_desc':
        tasks_query = tasks_query.order_by(Task.due_date.desc())
    else:
        tasks_query = tasks_query.order_by(Task.created_on.desc())
        
    tasks = tasks_query.all()
    
    return render_template('index.html', tasks=tasks, q=query_string, status=status_filter, sort=sort_by)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        due_date = request.form.get('due_date')
        status = request.form.get('status')
        remarks = request.form.get('remarks')
        created_by = request.form.get('created_by')
        
        new_task = Task(
            title=title,
            description=description,
            due_date=due_date,
            status=status,
            remarks=remarks,
            created_by=created_by,
            updated_by=created_by
        )
        
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('index'))
        
    return render_template('add.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    task = Task.query.get_or_404(id)
    
    if request.method == 'POST':
        task.title = request.form.get('title')
        task.description = request.form.get('description')
        task.due_date = request.form.get('due_date')
        task.status = request.form.get('status')
        task.remarks = request.form.get('remarks')
        task.updated_by = request.form.get('updated_by')
        
        db.session.commit()
        return redirect(url_for('index'))
        
    return render_template('edit.html', task=task)

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
