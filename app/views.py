from flask import render_template, request
from app import app, k

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        question = request.form['chat']
        response = k.respond(question)
        return render_template('form.html',
        						resp=response)
    else:
    	return render_template('form.html')