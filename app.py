import pickle
import flask
from  flask import Flask,request,app,jsonify
import numpy as np
import pandas as pd
from flask import Response
from flask_cors import CORS

#start app
app=Flask(__name__)
model=pickle.load(open('model.pkl', 'rb'))
@app.route('/predict_api',methods=['POST'])
def predict_api():
    
    data=request.json['data']
    print(data)
    #to pass data as 2D array
    new_data =[list(data.values())]
    output=model.predict(new_data)[0]
    return jsonify(output)

if __name__=='__main__':
    app.run(debug=True)