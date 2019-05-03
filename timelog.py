from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'John Doe',
        'title': 'Blog Post 1',
        'date': 'March 1, 2018',
        'content': 'first content'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'date': 'March 2, 2019',
        'content': 'hello content'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html', posts = posts)

@app.route("/about")
def about():
    return render_template('about.html', title='about')


if __name__ == '__main--':
    app.run(debug=True)
