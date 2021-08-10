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

    return render_template('abc.html', output=f'{response}')

@app.route('/model2',methods=['POST'])
def model2():
    model = pickle.load(open('model_JINI.pkl', 'rb'))
    final_data = np.array([[3049.22,1.00,390.00,390.00,0.00,5876.87,9,1,3200.0,6537.91,2729.08,0.00,12]])
    # final_data = [np.array([x for x in request.form.values()])]
    prediction = model.predict(final_data)

    if (prediction[0] == 0):
        response = "Their Balance is very less but still they purchase without taking much cash advance and prefer installments to do the purchases.They make sure to repay the intallments on time. \nBusiness Insights : These are good customers and even with less balance are managing to purchase So we should give them schemes where they can have discounts on some expensive products so that they are attracted to buy more stuff since they are frequent buyers.They are quite a number of people in this group so the company should definitely focus more on them."
    elif (prediction[0] == 1):
        response = "They are rich people with a lot of balance but not frquent buyers.Even with a lot of balance they still take a lot of cash advance to purchase suggesting that they buy expensive items.They are new customers and a few in quantity. \nBusiness Insights: In order to make them shell their money we need to provide them schemes for expensive items as well as the ordinary ones which they are not buying using the credit card. If through the schemes they can spend money on that as well then they have the capacity to bring a lot of profit."
    elif (prediction[0] == 2):
        response = "These are the cream customers who have been for a long time now and even do a lot of purachases. They take minimal cash adance and installments to do purchases.They even have a good balance and can afford their buy. \nBuisness Insights : Make sure not to lose them."
    elif (prediction[0] == 3):
        response = "Their balance is less and dont do purchases.They only buy the necessities and dont take the cash advance and installments to do so.they are a lot in number and have also been there for a good time. \nBusiness Insights: Focus a lot on them as they are a lot in number and aren't giving much profits.Come up with the schhemes that make them comfortable to make purchases in installments and by taking cash advances."
    else:
        response = "Error"

    return render_template('abc.html', output=f'Belongs to cluster {response}')

if __name__ == "__main__":
    app.run(debug=True)