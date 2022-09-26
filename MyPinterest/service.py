from flask import Flask, render_template, url_for, redirect, request, jsonify
from markupsafe import escape
from backend.pinterest import get_image, get_list_image, get_set_image, get_list_public_image
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('basic.html')
  
@app.route('/image')
def image():
    return render_template('image.html', url_image = get_image())
  
@app.route('/list-all')
def list_image():
    return render_template('list_image.html', list_image = get_list_image())

@app.route('/list', methods=['POST', 'GET'])
def set_image():
    if request.method == 'POST':
        number = request.form["number"]
        if number:
            return render_template('set_image.html', set_image = get_set_image(number))
    return render_template('set_image.html', set_image = get_set_image(5))
 
@app.route('/public', methods=['POST', 'GET'])
def public_image():
    if request.method == 'POST':
        return redirect(url_for('public_image'))
    return render_template('public_image.html', list_public_image = get_list_public_image())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4040, debug=True)