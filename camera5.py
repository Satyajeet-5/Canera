from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def camera():
    return render_template('camera5.html')

if __name__ == '__main__':
    app.run(debug=True)