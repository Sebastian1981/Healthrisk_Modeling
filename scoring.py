# script for scoring new data using the pre-built data-preprocessing and modeling pipeline

import os
import joblib
import numpy as np


# set paths
ROOTDIR = 'H:\Andere Computer\Mein Computer\GoogleDrive\Beruf\Freelancing\Code_Repo\Healthrisk_Modeling'
DATAPATH = "H:\Andere Computer\Mein Computer\GoogleDrive\Beruf\Freelancing\Code_Repo\Healthrisk_Modeling\data"
MODELPATH = "H:\Andere Computer\Mein Computer\GoogleDrive\Beruf\Freelancing\Code_Repo\Healthrisk_Modeling\model"


# define features and target
features = ['Pregnancies', 'PlasmaGlucose', 'DiastolicBloodPressure', 'TricepsThickness', 'SerumInsulin', 'BMI', 'DiabetesPedigree', 'Age']
target = 'Diabetic'

if __name__ == '__main__':
    print(MODELPATH)
    # Load the model from the file
    filename = '/diabetes_model.pkl'
    model_loaded = joblib.load(MODELPATH + filename)
    print('loaded trained model \n')
    print('------------------------')
    print(model_loaded)
    print('------------------------')
    
    # predict on a new sample
    X_new = np.array([[2,180,74,24,21,23,1.4,22]])
    print ('New sample: {}'.format(list(X_new[0])))

    # Get a prediction
    pred = model_loaded.predict(X_new)
    print('Predicted class is {}'.format(pred[0]))