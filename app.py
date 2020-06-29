from flask import Flask, render_template, url_for, request
from flask_bootstrap import Bootstrap
import pickle
import string
from nltk.corpus import stopwords


def text_process(mess):
    """
    Takes in a string of text, then performs the following:
    1. Remove all punctuation
    2. Remove all stopwords
    3. Returns a list of the cleaned text
    """
    # Check characters to see if they are in punctuation
    nopunc = [char for char in mess if char not in string.punctuation]

    # Join the characters again to form the string.
    nopunc = ''.join(nopunc)

    # Now just remove any stopwords
    return [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]
#     return [word for word in nopunc.split()]


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
