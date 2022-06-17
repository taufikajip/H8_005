#from crypt import methods
from unittest import result
import flask
import numpy as np
import pickle

from distutils.log import debug
from re import template

model = pickle.load(open('model/classifier_model.pkl','rb'))

app = flask.Flask(__name__, template_folder='templates')

@app.route('/')
def main():
    return(flask.render_template('main.html'))

@app.route('/predict',methods=['POST'])
def process():
    features = [float(x) for x in flask.request.form.values()]
    final_features = [np.array(features)]
    result = model.predict(final_features)

    output = {0:'(Middle Ground) Memiliki balance dan limit kartu kredit paling tinggi. Lebih sering membeli dengan metode sekali bayar(one off purchases). Sering melakukan transaksi belanja. Hampir tidak pernah membeli dengan uang tunai dimuka. Memiliki limit kartu kredit moderat.', 
    1:'(High Cash Advance Users) Tipe user yang memiliki balance tinggi dan sering melakukan transaksi pembelian. Jumlah transaksi dengan uang tunai dimuka, hampir sama dengan melakukan pembelian metode mencicil. Memiliki limit kartu kredit paling tinggi.',
    2:'(Frugal Credit Users) Memiliki balance paling rendah diantara cluster lain, frekuensi pembelian cukup tinggi dan sering melakukan pembelian dengan metode pembayaran mencicil, memiliki limit kartu kredit paling rendah.',
    3:'(High Credit Frequent Purchasers) Memiliki balance moderat, sangat jarang melakukan transaksi pembelian. Lebih sering melakukan transaksi dengan uang tunai dimuka. Hampir tidak pernah melakukan pembelian dengan metode mencicil. Tipe user ini memiliki limit kartu kredit medium.'}
    return flask.render_template('main.html',result_text='{}'.format(output[result[0]]))

if __name__=='__main__':
    app.run(debug=True)