from flask import Flask
from flask import render_template
from flask import abort, redirect, url_for
from flask import request
from flask import make_response\

app = Flask(__name__)

password="bluemarks"

@app.route('/', methods=['POST', 'GET'])
def games():
    if request.method == 'POST':
        if (request.form['password'] == password):
            resp = make_response(redirect("/games.html"))
            resp.set_cookie('password', request.form['password'])
            return resp
        else:
            return redirect("/")
    return render_template('index.html')
@app.route('/games.html')
def GAMES_IDK():
    if (request.cookies.get('password') == password):
        return render_template('games.html')
    else:
        return redirect("/")
@app.route('/floodrunner4.html')
def GAMES_IDK2():
    if (request.cookies.get('password') == password):
        return render_template('floodrunner4.html')
    else:
        return redirect("/")
@app.route('/bloxorz.html')
def GAMES_IDK3():
    if (request.cookies.get('password') == password):
        return render_template('bloxorz.html')
    else:
        return redirect("/")
@app.route('/1v1lol.html')
def GAMES_IDK4():
    if (request.cookies.get('password') == password):
        return render_template('1v1lol.html')
    else:
        return redirect("/")
@app.route('/Roblox.html')
def GAMES_IDK7():
    if (request.cookies.get('password') == password):
        return render_template('Roblox.html')
    else:
        return redirect("/")
@app.route('/test.js')
def GAMES_IDK8():
    if (request.cookies.get('password') == password):
        return render_template('test.js')
    else:
        return redirect("/")
@app.route('/bigneontowervstinysquare.html')
def GAMES_IDK10():
    if (request.cookies.get('password') == password):
        return render_template('bigneontowervstinysquare.html')
    else:
        return redirect("/")
@app.route('/baldisbasics.html')
def GAMES_IDK11():
    if (request.cookies.get('password') == password):
        return render_template('baldisbasics.html')
    else:
        return redirect("/")
@app.route('/Retrobowl.html')
def GAMES_IDK12():
    if (request.cookies.get('password') == password):
        return render_template('Retrobowl.html')
    else:
        return redirect("/")
@app.route('/Slope.html')
def GAMES_IDK13():
    if (request.cookies.get('password') == password):
        return render_template('Slope.html')
    else:
        return redirect("/")
@app.route('/OvO.html')
def GAMES_IDK14():
    if (request.cookies.get('password') == password):
        return render_template('OvO.html')
    else:
        return redirect("/")
@app.route('/Fnaf1.html')
def GAMES_IDK15():
    if (request.cookies.get('password') == password):
        return render_template('Fnaf1.html')
    else:
        return redirect("/")
@app.route('/CookieClicker.html')
def GAMES_IDK16():
    if (request.cookies.get('password') == password):
        return render_template('CookieClicker.html')
    else:
        return redirect("/")
app.run(host='0.0.0.0',port=8080)
