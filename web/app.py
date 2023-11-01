from flask import Flask, render_template

app = Flask(__name__)

# @app.route("/")
# def test_window():
#     return "<p>ЭТО ТЕСТОВОЕ ОКНО!</p>"

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('base.html')