from flask import Flask, redirect, url_for, render_template, request, session, flash
from flask_sqlalchemy import SQLAlchemy
import hashlib
from datetime import timedelta


app = Flask(__name__)
app.secret_key = 'hello'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:12345678@localhost/flask_python11'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(minutes=10)

db = SQLAlchemy(app)

class Users(db.Model):
    _id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(100))
    password = db.Column('password', db.String(100))
    email = db.Column('email', db.String(100))

    def __init__(self, name, password, email):
        self.name = name
        self.password = password
        self.email = email

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        session.permanent = True
        user_name = request.form["usernm"]
        user_pass = hashlib.md5(request.form["userpass"].encode()).hexdigest()
        user_in_db = Users.query.filter_by(name=user_name).first()
        if user_in_db:
            if user_pass == user_in_db.password:
                session['user_name'] = user_name
                session['email'] = user_in_db.email
                flash('Login successful')
                return redirect(url_for('user', name=user_name, email=user_in_db.email))
            else:
                flash('Wrong password!')
                return render_template('login.html')
        else:
            new_user = Users(user_name, user_pass, '')
            db.session.add(new_user)
            db.session.commit()
            session['user_name'] = user_name
            session['email'] = ''
            flash('User was created.')
            return redirect(url_for('user', name=user_name))
    else:
        if 'user_name' in session:
            flash('Already logged in.')
            return redirect(url_for('user', name=session['user_name']))
        else:
            return render_template('login.html')

@app.route('/user', methods=['POST', 'GET'])
def user():
    if 'user_name' in session:
        user_name = session['user_name']
        if request.method == 'POST':
            email = request.form['usermail']
            session['email'] = email
            user_in_db = Users.query.filter_by(name=user_name).first()
            user_in_db.email = email
            db.session.commit()
            flash('Email was saved.')
        else:
            if 'email' in session:
                email = session['email']
            else:
                email = ''
        return render_template('user.html', name=user_name, email=email)
    else:
        flash('You are not logged in.')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    if 'user_name' in session:
        session.pop('user_name', None)
        session.pop('email', None)
        flash('Logged out.')
    return redirect(url_for('login'))

@app.route('/delete')
def delete():
    user_name = session['user_name']
    Users.query.filter_by(name=user_name).delete()
    db.session.commit()
    session.pop('user_name', None)
    session.pop('email', None)
    return redirect(url_for('login'))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)