from flask import Flask, url_for
app = Flask(__name__)



@app.route('/profile/<username>')
def show_user_profile(username):
    return "User: %s" % username

@app.route('/')
def index():
    return url_for('show_user_profile', username='anurag')

if __name__ == '__main__':
    app.debug = True
    app.run()
