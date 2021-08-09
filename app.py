from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('abc.html')

@app.route('/model1',methods=['POST'])
def model1():
    model = pickle.load(open('Model_Jay.pkl', 'rb'))
    # final_data = np.array([[129.84,1433.99,0.00,4000.0,1363.13,141.65,0.88]])
    final_data = [np.array([x for x in request.form.values()])]
    prediction = model.predict(final_data)

    if (prediction[0] == 0):
        response = "Customers of cluster 0 have a pretty good credit limit and balance but these customers have a very low oneoff purchase and purchases in comparison to cash advance. This means they take more cash advance and spend less through purchasing. These customers should be given schemes accordingly to increase their purchase which will indirectly increase oneoff purchase and installment purchases."
    elif (prediction[0] == 1):
        response = "Credit limit of customers of cluster 1 is lowest amongst all. These customers have a low balance but they have quite high purchase and installment purchases. These customers have a very low oneoff purchase and cash advance."
    elif (prediction[0] == 2):
        response = "These customers have a good credit limit but their balance, oneoff urchase, purchases, installment purchases is very low. So these customers should be encouraged by giving schemes to spend more and to increase the balance by keeping a minimum balance"
    elif (prediction[0] == 3):
        response = "These customers have the highest credit limit and oneoff purchase followed by purchases and installment purchases. They have highest payment of all clusters. These customers should be encouraged to keep decent balance in their account by keeping a minimum balance rule."
    else:
        response = "Error"

    return render_template('abc.html', output=f'Belongs to cluster {response}')

@app.route('/model2',methods=['POST'])
def model2():
    model = pickle.load(open('modelR.pkl', 'rb'))
    final_data = np.array([[1854.03,576.00,0.33,5,15,2000.0,654.47,0.00,20]])
    prediction = model.predict(final_data)

    return render_template('index.html', output=f'Belongs to cluster {prediction}')

if __name__ == "__main__":
    app.run(debug=True)