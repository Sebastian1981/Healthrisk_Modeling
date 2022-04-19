from flask import Flask, request

app = Flask(__name__)
@app.route('/')
def home():
    return "<h1>We are running Flask!</h1>"  

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


app.run()  