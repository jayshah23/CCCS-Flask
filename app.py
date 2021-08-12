from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/model',methods=['POST'])
def model():
    model1 = pickle.load(open('Model_Jay.pkl', 'rb'))
    model2 = pickle.load(open('model_JINI.pkl', 'rb'))
    
    final_data = [np.array([x for x in request.form.values()])]
    prediction1 = model1.predict([final_data[0][:7]])
    prediction2 = model2.predict(final_data)

    if (prediction1[0] == 0):
        response1 = "Customers of cluster 0 have a pretty good credit limit and balance but these customers have a very low oneoff purchase and purchases in comparison to cash advance. This means they take more cash advance and spend less through purchasing."
        insight1 = "These customers should be given schemes accordingly to increase their purchase which will indirectly increase oneoff purchase and installment purchases."
    elif (prediction1[0] == 1):
        response1 = "Credit limit of customers of cluster 1 is lowest amongst all. These customers have a low balance but they have quite high purchase and installment purchases."
        insight1 = "These customers have a very low oneoff purchase and cash advance."
    elif (prediction1[0] == 2):
        response1 = "These customers have a good credit limit but their balance, oneoff urchase, purchases, installment purchases is very low."
        insight1 = "These customers should be encouraged by giving schemes to spend more and to increase the balance by keeping a minimum balance."
    elif (prediction1[0] == 3):
        response1 = "These customers have the highest credit limit and oneoff purchase followed by purchases and installment purchases. They have highest payment of all clusters."
        insight1 = "These customers should be encouraged to keep decent balance in their account by keeping a minimum balance rule."
    else:
        response1 = "Error"

    if (prediction2[0] == 0):
        response2 = "Their Balance is very less but still they purchase without taking much cash advance and prefer installments to do the purchases.They make sure to repay the intallments on time."
        insight2 = "These are good customers and even with less balance are managing to purchase So we should give them schemes where they can have discounts on some expensive products so that they are attracted to buy more stuff since they are frequent buyers.They are quite a number of people in this group so the company should definitely focus more on them"
    elif (prediction2[0] == 1):
        response2 = "They are rich people with a lot of balance but not frquent buyers.Even with a lot of balance they still take a lot of cash advance to purchase suggesting that they buy expensive items.They are new customers and a few in quantity."
        insight2 = "In order to make them shell their money we need to provide them schemes for expensive items as well as the ordinary ones which they are not buying using the credit card. If through the schemes they can spend money on that as well then they have the capacity to bring a lot of profit."
    elif (prediction2[0] == 2):
        response2 = "These are the cream customers who have been for a long time now and even do a lot of purachases. They take minimal cash adance and installments to do purchases.They even have a good balance and can afford their buy."
        insight2 = "Make sure not to lose them."
    elif (prediction2[0] == 3):
        response2 = "Their balance is less and dont do purchases.They only buy the necessities and dont take the cash advance and installments to do so.they are a lot in number and have also been there for a good time."
        insight2 = "Focus a lot on them as they are a lot in number and aren't giving much profits.Come up with the schhemes that make them comfortable to make purchases in installments and by taking cash advances."
    else:
        response2 = "Error"

    return render_template('index.html',prediction1=f'This customer belongs to cluster {prediction1[0]}', insight1=insight1, output1=response1, prediction2=f'This customer belongs to cluster {prediction2[0]}', insight2=insight2, output2=response2)

if __name__ == "__main__":
    app.run(debug=True)