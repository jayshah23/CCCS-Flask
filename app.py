from flask import Flask, render_template
import pickle
import numpy as np

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/model1',methods=['POST'])
def model1():
    modelA = pickle.load(open('Model_Jay.pkl', 'rb'))
    final_data = np.array([[1854.03, 1013.50, 1243.09, 2000.0, 654.47, 1524.38, 0.00]])
    # final_data = np.array([[1854.03, 1.00, 1013.50, 576.00, 437.50, 1243.09, 0.50, 0.08, 0.33, 0.08, 5, 15, 2000.0, 654.47, 
    #                  1524.38, 0.00, 12, 20]])
    prediction = modelA.predict(final_data)

    return render_template('index.html', output=f'Belongs to cluster {prediction}')

if __name__ == "__main__":
    app.run(debug=True)