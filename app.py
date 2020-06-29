from flask import Flask, render_template, url_for, request
from flask_bootstrap import Bootstrap
import pickle


filename = 'emotion.sav'
loaded_model = pickle.load(open(filename, 'rb'))


app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST', "GET"])
def predict():
    if request.method == 'POST':
        textquery = request.form['text']
        data = [textquery]
        result = loaded_model.predict(data)[0]
    return (result)


if __name__ == '__main__':
    app.run(debug=True)
