from flask import Flask,render_template

import statist.views as action

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello')
def hello_world():
    return 'Hello World!'

@app.route('/stock')
def getStock():
	 return action.getStock()

@app.route('/curr')
def getCurrency():
	 return action.getCurrency()

@app.route('/debt')
def getDebt():
	 return action.getDebt()

@app.route('/debt/family')
def getDebtFamily():
	 return action.getDebtFamily()

@app.route('/house/trade')
def getTrade():
	 return action.getTrade()

@app.route('/house/charter')
def getCharter():
	 return action.getCharter()


if __name__ == '__main__':
    app.run(host="0.0.0.0")
    # app.run()