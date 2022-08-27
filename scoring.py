# script for scoring new data using the pre-built data-preprocessing and modeling pipeline

import os
import joblib
import numpy as np
import pandas as pd

# set paths
ROOTDIR = os.getcwd()
DATAPATH = os.path.join(ROOTDIR, 'data')
MODELPATH = os.path.join(ROOTDIR, 'model')

if __name__ == '__main__':
    # Load the model 
    filename = '\diabetes_model.pkl'
    model_loaded = joblib.load(MODELPATH + filename)
    print('loaded trained model \n')
    print('------------------------')
    print(model_loaded)
    print('------------------------')
    
    # predict on a new sample
    # make up some new data as dictionary as provided later in the rest api
    data = {
        "Pregnancies": 5.0,
        "PlasmaGlucose": 100.0,
        "DiastolicBloodPressure": 74.0,
        "TricepsThickness": 24.0,
        "SerumInsulin": 21.0,
        "BMI": 23.0,
        "DiabetesPedigree": 1.4,
        "Age": 22.0
    }
    print(data)

    # turn data into dataframe
    X_new = pd.DataFrame.from_dict(data, orient='index').T
    print(X_new.head())

    # Get a prediction
    pred = model_loaded.predict(X_new)
    print('Predicted class is {}'.format(pred[0]))