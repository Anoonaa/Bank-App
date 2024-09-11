from flask import Flask, render_template, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from models.models import User  
from forms import LoginForm  

app = Flask(__name__)
app.secret_key = 'secretkey'  # Key for test usage

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'  # to set the login view for @login_required

# User loader callback for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.get_user(user_id)  #  get the user object by username

@app.route('/')
@login_required
def index():
    return f'Hello, {current_user.id}. You are logged in.'

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        if User.verify_password(username, password):
            user = User.get_user(username)
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password')

    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)

