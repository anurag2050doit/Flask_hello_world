from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == "POST":
        if valid_login(
            request.form.get('username'),
            request.form.get('password')
        ):
            return redirect(url_for('welcome',username=request.form.get('username')))
        else:
            error = "Incorrect Username and password"
    return render_template('login.html', error=error)

@app.route('/welcome/<username>')
def welcome(username):
    return render_template('welcome.html',username=username)

def valid_login(username, password):
    # checks on the db if the username and password are correct
    if len(password)>5 and username:
        return True
    else:
        return False

if __name__ == '__main__':
    app.debug = True
    app.run()
