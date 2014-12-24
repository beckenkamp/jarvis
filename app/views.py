from flask import render_template, request, jsonify
from app import app, k

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/talk', methods=['GET'])
def talk():
    question = request.args.get('question')
    answer = k.respond(question)
    return jsonify(question=question, answer=answer)

@app.errorhandler(404)
def page_not_found(e):
    return 'Sorry, Nothing found here.', 404


@app.errorhandler(500)
def page_not_found(e):
    return 'Sorry, internal server error: {}'.format(e), 500