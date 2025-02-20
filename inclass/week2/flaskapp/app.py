from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        'user': 'elonmusk',
        'text': 'The sun is a thermonuclear explosion fyi'
    },
    {
        'user': 'john',
        'text': 'Excited for school!!!!'
    }
]

# @app.route()
@app.route('/')
def index_route():
    return render_template('index.html', posts=posts)

# @app.route()
# def user_route(user):
#     user_posts = [post for post in posts if post['user'] == user]
#     return render_template('user.html', user=user, user_posts=user_posts)


# @app.route()
# def test_route():
#     var = 'Hello, World! from var'
#     return render_template('test.html', var=var)


# @app.route()
# def test_route2():
#     return 'testing 123'
