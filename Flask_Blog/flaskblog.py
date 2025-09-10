from flask import Flask, render_template, url_for

app = Flask(__name__)

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
def hello_world():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about_page():
    return render_template('about.html', title = 'About')

if __name__ == '__main__':
    app.run(debug=True)

