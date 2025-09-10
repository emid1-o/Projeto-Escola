from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '0a6666ca7be09ffc36e16fe5ed2ce898'

posts = [

        {
            'author': 'Corey Schafer',
            'title': 'Jaws',
            'content': 'first post content',
            'date_posted': 'April 20, 2018'
        },
        {
            'author': 'Emidio Neto',
            'title': 'Jaws 3',
            'content': 'Second post content',
            'date_posted': 'April 18, 2018'
        },

]


@app.route("/")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about_page():
    return render_template('about.html', title = 'About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Acoount created for { form.username.data }!', 'success')
        return redirect(url_for('home'))

    return render_template('register.html', title = 'Register', form=form)

@app.route("/login", methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'admin':
            flash('You have been logged in', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check your username ands password', 'danger')
    return render_template('login.html', title = 'Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)

