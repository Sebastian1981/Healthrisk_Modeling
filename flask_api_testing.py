import requests

url = 'http://127.0.0.1:5000/predict'

data = {
        "Pregnancies": 1.0,
        "PlasmaGlucose": 120.0,
        "DiastolicBloodPressure": 74.0,
        "TricepsThickness": 24.0,
        "SerumInsulin": 21.0,
        "BMI": 23.0,
        "DiabetesPedigree": 1.4,
        "Age": 22.0
        }

# send post request
r = requests.post(url, json=data)
print('response status: ', r)
print('-----------------------')
print('The model predicted the label: ', r.text)
print('-----------------------')
