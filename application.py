import pickle
from flask import Flask , request, render_template, jsonify
import numpy as np 
import pandas as pd
from sklearn.preprocessing import StandardScaler


application=Flask(__name__)

## import xgboost regressor and Standard scaler
XG_Boost_model= pickle.load(open('models/XGBoost.pkl','rb'))
standard_scaler = pickle.load(open('models/scaler.pkl','rb'))

app=application

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])

class CustomData:
    def __init__(self,
                 carat:float,
                 depth:float,
                 table:float,
                 cut:str,
                 color:str,
                 clarity:str):
        
        self.carat=carat
        self.depth=depth
        self.table=table
        self.cut = cut
        self.color = color
        self.clarity = claritydef predict_datapoint():
        
    if request.method=='GET':
        return render_template('form.html')
    
    else:
        data=CustomData(
            carat=float(request.form.get('carat')),
            depth = float(request.form.get('depth')),
            table = float(request.form.get('table')),
            cut = request.form.get('cut'),
            color= request.form.get('color'),
            clarity = request.form.get('clarity')

            
        )
        final_new_data=standard_scaler.transform([['carat','depth','table','cut','colour','clarity']])
        pred=predict_pipeline.predict(final_new_data)

        results=round(pred[0],2)

        return render_template('form.html',final_result=results)
    

if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)