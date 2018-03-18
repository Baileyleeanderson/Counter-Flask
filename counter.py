from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'The matrix has You'
@app.route('/')
def index():
    if not 'click' in session:
        session['click'] = 0  
    return render_template("index.html")

@app.route('/index')
def process():
    session['click'] += 2
    print "I counting it"
    return redirect('/')
app.run(debug=True)

@app.route('/reset')
def resetter():
    session['click'] = 1
    print "You are now 1"
    return redirect('/')
app.run(debug=True)

