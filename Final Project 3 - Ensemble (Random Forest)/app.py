from distutils.log import debug
from re import template
import flask

import numpy as np
import pickle

model = pickle.load(open('model/RF_model_smote_predict_hyp.pkl', 'rb'))

app = flask.Flask(__name__, template_folder='templates')

@app.route('/')
def main():
    return(flask.render_template('index.html'))

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    # int_features = [int(x) for x in flask.request.form.values()]
    int_features = [x for x in flask.request.form.values()]
    final_features = [np.array(int_features)]
    
    prediction = model.predict(final_features)

    #output = {0: 'NOT LIKELY', 1: 'LIKELY'}

    #return f'##### {prediction}'
    #return flask.render_template('index.html', prediction_text='THE PATIENT IS {} TO HAVE A HEART FAILURE'.format(output[prediction[0]]))
    return flask.render_template('results.html',pred=prediction)


if __name__ == "__main__":
    app.run(debug = True)
