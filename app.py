from flask import Flask,request,render_template
from flask_cors import  cross_origin

import pickle
import os

app = Flask(__name__)

@app.route('/',methods=['GET'])
@cross_origin()
def home():

    return render_template("home.html")


@app.route('/prediction',methods=['GET', 'POST'])
@cross_origin()
def result():
    #  reading the inputs given by the user
    gender = int(request.form['Gender'])
    Age = int(request.form['Age'])
    Previously_Insured = int(request.form['Previously_Insured'])
    Vehicle_Age = int(request.form['Vehicle_Age'])
    Vehicle_Damage = int(request.form['Vehicle_Damage'])
    Annual_Premium = int(request.form['Annual_Premium'])
    Policy_Sales_Channel = int(request.form['Policy_Sales_Channel'])


    filename = 'model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))  # loading the model file from the storage
    x=[[gender, Age, Previously_Insured, Vehicle_Age, Vehicle_Damage, Annual_Premium, Policy_Sales_Channel]]

    prediction = loaded_model.predict(x)
    print(prediction)

    if prediction == [1]:
        prediction = "The customer will take the Insurance"

    else:
        prediction = "The customer will not take the Insurance"
    print(prediction)



    return render_template('prediction.html',prediction=prediction)



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
   #app.run(debug=True)