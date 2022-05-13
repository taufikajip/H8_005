import flask
import numpy as np
import pickle
import warnings
warnings.filterwarnings("ignore")

model = pickle.load(open('model/svm_model_predict.pkl','rb'))

app = flask.Flask(__name__, template_folder='templates')

@app.route('/')
def main():
    return(flask.render_template('main.html'))

@app.route('/predict',methods=['POST'])
def predict():
    features = [float(x) for x in flask.request.form.values()]
    final_features = [np.array(features)]
    prediction = model.predict(final_features)

    output = {0.0:'Tidak Akan Hujan', 1.0:'Akan Hujan'}
    return flask.render_template('main.html',prediction_text='Kemungkinan Besok {}'.format(output[prediction[0]]))

if __name__=='__main__':
    app.run(debug=True)