from flask import Flask, render_template
from parameters import Gameschema

app = Flask(__name__)

@app.route('/')
def model():
    # params = self.params
    return render_template('model.html')

if __name__ == '__main__':
    app.run()