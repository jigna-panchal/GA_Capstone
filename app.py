from collections import Counter
from flask import Flask, request, render_template
import pickle
app = Flask(__name__)

with open("model.pkl","rb") as pkl_file:
    model = pickle.load(pkl_file)


def dict_to_html(d):
    return '<br>'.join('{0}: {1}'.format(k, d[k]) for k in sorted(d))


# Form page to submit text
@app.route('/')
def submission_page():
    return render_template('index.html')

characters = {0:'Chandler', 1:'Joey', 2:'Monica', 3:'Phoebe', 4:'Rachel', 5:'Ross', 6:'Not a Friend'}


# My word counter app
@app.route('/predict', methods=['POST'] )
def word_counter():
    text = str(request.form['user_input'])
    if text == '':
        pred = [6]
    else: 
        pred = model.predict([text])
    character = characters[pred[0]]
    
    name = f'{character}'
    return render_template('predict.html',name = name)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
