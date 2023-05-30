from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    date = request.args.get('date')
    if date == "now":
        now = datetime.now()
        formatted_date = now.strftime("%Y. %m. %d. %H:%M")
        date = formatted_date 
    else:
        date = date 
    name = request.args.get('name')
    sname = request.args.get('sname')
    rname = request.args.get('rname')
    sendaccount = request.args.get('sendaccount')
    receiveaccount = request.args.get('receiveaccount')
    amount = request.args.get('amount')
    return render_template("main.html", date=date, name=name, sname=sname, rname=rname, sendaccount=sendaccount, receiveaccount=receiveaccount, amount=amount)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
