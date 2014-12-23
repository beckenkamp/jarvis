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

@app.errorhandler(404)
def page_not_found(e):
    return 'Sorry, Nothing found here.', 404


@app.errorhandler(500)
def page_not_found(e):
    return 'Sorry, internal server error: {}'.format(e), 500