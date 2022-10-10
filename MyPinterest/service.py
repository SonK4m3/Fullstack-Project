from flask import Flask, render_template, url_for, redirect, request, jsonify, session
from markupsafe import escape
from backend.pinterest import get_image, get_list_image, get_set_image, get_list_public_image
app = Flask(__name__)

_DEFAULT_TOPIC = 'pokemon'
_TOPPICS = ['pokemon', 'naruto', 'hero', 'badminton']
_DEFAULT_LIMIT_IMAGE = 6
@app.route('/', methods=['POST', 'GET'])
@app.route('/home', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        topic = request.form['select-topic']
        if topic:
            return redirect(url_for('image', topic=topic))
    return render_template('basic.html', list_topics=_TOPPICS, topic=_DEFAULT_TOPIC)
  
@app.route('/image/<topic>', methods=['POST', 'GET'])
def image(topic=_DEFAULT_TOPIC):
    if request.method == 'POST':
        topic = request.form['select-topic']
        if (request.form['button'] == 'other-image' or request.form['button'] == 'submit-topic'):
            return redirect(url_for('image', topic=topic))

    return render_template('image.html', topic=topic, list_topics = _TOPPICS,url_image = get_image(topic))


@app.route('/list/<topic>', methods=['POST', 'GET'])
def list_image(topic=_DEFAULT_TOPIC):
    if request.method == 'POST':
        if request.form['button'] == 'submit-topic':
            topic = request.form['select-topic']
            if topic:
                return redirect(url_for('list_image', topic=topic))    
    return render_template('list_image.html', list_topics = _TOPPICS, topic=topic, list_image = get_list_image(topic), number_limit = _DEFAULT_LIMIT_IMAGE)

@app.route('/random-list/<topic>', methods=['POST', 'GET'])
def set_image(topic=_DEFAULT_TOPIC):
    if request.method == 'POST':
        if request.form['button'] == 'submit-topic':
            topic = request.form['select-topic']
            if topic:
                return redirect(url_for('set_image', topic=topic))
        if request.form['button'] == 'another-list':
            number = int(request.form["limit-number"])
            if number:
                return render_template('set_image.html', list_topics = _TOPPICS, set_image = get_set_image(topic,number), topic=topic)
    return render_template('set_image.html', list_topics = _TOPPICS, set_image = get_set_image(topic,_DEFAULT_LIMIT_IMAGE), topic=topic)
 
@app.route('/public', methods=['POST', 'GET'])
def public_image():
    if request.method == 'POST':
        return redirect(url_for('public_image'))
    return render_template('public_image.html', list_public_image = get_list_public_image(), list_topics=_TOPPICS, topic=_DEFAULT_TOPIC)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4040, debug=True)