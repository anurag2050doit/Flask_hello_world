from flask import Flask, request, render_template, redirect, url_for, flash, session
import logging
from logging.handlers import RotatingFileHandler


app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == "POST":
        if valid_login(
            request.form.get('username'),
            request.form.get('password')
        ):
            flash("Sucedfully logged in")
            session['username'] = request.form.get('username')
            return redirect(url_for("welcome"))
        else:
            error = "Incorrect Username and password"
            app.logger.warning("Incorrect username and password for user (%s)", request.form.get('username'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect( url_for("login"))

@app.route('/')
def welcome():
    if "username" in session:
        return render_template('welcome.html',username=session['username'])
    else:
        return redirect(url_for("login"))

def valid_login(username, password):
    # checks on the db if the username and password are correct
    if len(password)>5 and username:
        return True
    else:
        return False

if __name__ == '__main__':
    app.secret_key = '\xe2\xcf\x96\x8a+\xa4\x81\xf9\xb7\xe6\x90\x96\xe0j$\x14j\x8f\xae\x83\x13\x95\x9dq'
    # logging
    handler = RotatingFileHandler('error.log', maxBytes=1000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler (handler)
    app.debug = True
    app.run()
