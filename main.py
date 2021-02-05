#importing the necessary dependencies
from flask import Flask, render_template, request,jsonify
from flask_cors import cross_origin
import pickle
import numpy as np
import sklearn

app = Flask(__name__) # initializing a flask app
model=pickle.load(open("customerchurn.pkl","rb"))

@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")
@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        int_value= [float(x) for x in request.form.values()]
        final_value= [np.array(int_value)]
        result= model.predict(final_value)
        if int(result) == 1:
            prediction = "Going to terminate your Subscription"
        else:
            prediction = 'satisfied with your service'
        return render_template("results.html", prediction=prediction)
if __name__ == "__main__":
    app.run(debug=True)
