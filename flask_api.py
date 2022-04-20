from flask import Flask, request
import joblib
import pandas as pd

# start app
app = Flask(__name__)


# import trained model
MODELPATH = "H:\Andere Computer\Mein Computer\GoogleDrive\Beruf\Freelancing\Code_Repo\Healthrisk_Modeling\model"
# Load the model from the file
filename = '/diabetes_model.pkl'
model = joblib.load(MODELPATH + filename)
print('loaded trained model \n')
print('------------------------')
print(model)
print('------------------------')


@app.route('/')
def home():
    return "<h1>We are predicting diabetis!</h1>"  

@app.route('/add', methods=['GET'])
def add_GET():
    a = request.args.get('a')
    b = request.args.get('b')
    return str(int(a) + int(b))


@app.route('/add', methods=['POST'])
def add_POST():
    data = request.get_json()
    a = data['a']
    b = data['b']
    return str(int(a) + int(b))

@app.route('/predict', methods=['POST'])
def predict_POST():
    data = request.get_json()
    # turn data into dataframe
    X_new = pd.DataFrame.from_dict(data, orient='index').T
    # return prediction
    return 'the model predicted the label: ' + str(model.predict(X_new))



app.run()  