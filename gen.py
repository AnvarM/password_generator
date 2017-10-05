from flask import Flask, render_template, request, url_for
import random as r
import math

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/passw', methods=['POST'])    
def passw():
    symbols = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','Q','X','Y','Z','1','2','3','4','5','6','7','8','9','0','!','@','#','$','%','^','&','*','(',')','~']
    digits = ['1','2','3','4','5','6','7','8','9','0']
    length = request.form['length']
    if(length[0] not in digits):
        password = "Длина измеряется числами"
    elif(int(length) == 0):
        password = "Ну и где ты видел пароль нулевой длины?!"   
    elif (int(length) > 20):
        password = "Тебе не нужен такой длинный пароль"
    else:
        length = int(length)        
        password = []
        for i in range(length):
            password += r.choice(symbols)
        password = "".join(password)
    return render_template('passw.html', password = password)
    
if __name__ == "__main__":
	app.run(host = '0.0.0.0', port = 8080)
