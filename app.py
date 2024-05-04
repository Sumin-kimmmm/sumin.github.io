from flask import Flask, render_template # type: ignore

app = Flask(__name__)

@app.route('/')
def basic():
    return render_template("basic.html")

@app.route('/info')
def info():
    return render_template("info.html")

@app.route('/activity')
def activity_page():  # 함수 이름 변경
    return render_template("activity.html")

if __name__ == '__main__':
    app.run(debug=True)

    