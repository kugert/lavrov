from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/login/', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        attempted_username = request.form['username']
        attempted_password = request.form['password']
        if (attempted_username == 'user') and (attempted_password == 'pass'):
            return redirect(url_for('homepage'))
    return render_template('login.html')


if __name__ == '__main__':
    app.run()
