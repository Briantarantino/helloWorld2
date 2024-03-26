from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Brian Tarantino! I am adding my first code change.'

@app.route('/hello')
def hello():
    return render_template('hello.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/aboutcss')
def aboutcss():
    return render_template('about-css.html')

@app.route('/favoritecourse')
def favoritecourse():
    print('You entered your favorite course as: ' + request.args.get('subject') + ' ' + request.args.get('course_number'))

    return render_template('favorite-course.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run()