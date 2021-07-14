from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<name>')
def home(name):
    return render_template('home_page.html', name=name)


@app.route('/looping/<int:number>')
def looping(number):
    return render_template('loopy.html', number=number)


@app.route('/times/<int:number>')
def times(number):
    return render_template('times_table.html', number=number)


@app.route('/my_picture')
def pic():
    return render_template('picture.html')


if __name__ == '__main__':
    app.debug = True
    app.run()

