from flask import Flask, render_template, url_for, redirect, request, session, json
from flask_session import Session
from flask_paginate import Pagination, get_page_args
from markupsafe import escape
import math

import sys
import os
# import module printerest database
myDir = os.getcwd()
sys.path.append(myDir)

from pathlib import Path
path = Path(myDir)
a=str(path.parent.absolute())

sys.path.append(a)
from my_database.pinterest_database import *
###

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

_DEFAULT_TOPIC = 'pokemon'
_TOPPICS = get_all_topics()
_DEFAULT_LIMIT_IMAGE = 6

@app.route('/', methods=['POST', 'GET'])
@app.route('/home', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        #run to image when click choose topic image
        topic = request.form['select-topic']
        if topic:
            return redirect(url_for('image', topic=topic))
    return render_template('basic.html', list_topics=_TOPPICS, topic=_DEFAULT_TOPIC)
  
@app.route('/image/<topic>', methods=['POST', 'GET'])
def image(topic=_DEFAULT_TOPIC):
    if request.method == 'POST':
        #select topic -> reload image following topic
        topic = request.form['select-topic']
        if (request.form['button'] == 'other-image' or request.form['button'] == 'submit-topic'):
            return redirect(url_for('image', topic=topic))

    return render_template('image.html', topic=topic, list_topics=_TOPPICS, url_image=get_random_url(topic))


@app.route('/list/<topic>', methods=['POST', 'GET'])
def list_image(topic=_DEFAULT_TOPIC):    
    if not session.get('number'):
        number = _DEFAULT_LIMIT_IMAGE
    else:
        number = session.get('number')
    
    if request.method == 'POST':
        if request.form['button'] == 'submit-topic':
            topic = request.form['select-topic']
            if topic:
                session['number'] = None
                return redirect(url_for('list_image', topic=topic))
        elif request.form['button'] == 'another-list':
            number = int(request.form["limit-number"])
            session['number'] = number
            page, per_page, offset = get_page_args(page_parameter='page', per_page=number)       
            #rechange start index and page number when select number out of page
            list_image = get_list_urls(topic)
            total = len(list_image)
            page = math.ceil(total/per_page) if page > math.ceil(total/per_page) else page
            offset = per_page * (page - 1)
            
            pagination = Pagination(page=page, per_page=per_page, total=total,
                                    css_framework='bootstrap4')
            return render_template('list_image.html', list_topics=_TOPPICS, topic=topic, list_image=list_image,
                           offset = offset,
                           page=page,
                           per_page=per_page,
                           pagination=pagination)
            
        #add a and b into start value to differentiate 
        elif request.form['button'][0] == 'a':
            url = request.values['button'][1::]
            if url:
                print(url)
                # remove image from image to public
                remove_url_from_image_to_public(topic, url)
                # reload page
                number = int(request.form["limit-number"])
                session['number'] = number
                page, per_page, offset = get_page_args(page_parameter='page', per_page=number)       
                #rechange start index and page number when select number out of page
                list_image = get_list_urls(topic)
                total = len(list_image)
                page = math.ceil(total/per_page) if page > math.ceil(total/per_page) else page
                offset = per_page * (page - 1)
                
                pagination = Pagination(page=page, per_page=per_page, total=total,
                                        css_framework='bootstrap4')
                return render_template('list_image.html', list_topics=_TOPPICS, topic=topic, list_image=list_image,
                           offset = offset,
                           page=page,
                           per_page=per_page,
                           pagination=pagination)
        
        if request.form['button'][0] == 'b':
            url = request.values['button'][1::]
            if url:
                # print(url)
                return redirect(url_for('list_image', topic=topic))
        
    page, per_page, offset = get_page_args(page_parameter='page', per_page=number)       
    list_image = get_list_urls(topic)
    total = len(list_image)
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')
    return render_template('list_image.html', list_topics=_TOPPICS, topic=topic, list_image=list_image,
                           offset = offset,
                           page=page,
                           per_page=per_page,
                           pagination=pagination)

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
                return render_template('set_image.html', list_topics=_TOPPICS, set_image=get_random_url(topic,number), topic=topic)
    return render_template('set_image.html', list_topics=_TOPPICS, set_image=get_random_url(topic,_DEFAULT_LIMIT_IMAGE), topic=topic)
 
@app.route('/public', methods=['POST', 'GET'])
def public_image():
    if request.method == 'POST':
        return redirect(url_for('public_image'))
    return render_template('public_image.html', list_public_image = get_list_urls_public(), list_topics=_TOPPICS, topic=_DEFAULT_TOPIC)

@app.route('/get-image/<topic>', methods=['GET'])
def get_json_image(topic):
    db_images = get_list_urls(topic)
    json_images = json.jsonify(db_images)
    
    return json_images

@app.route('/get-public-image', methods=['GET'])
def move_image_public():
    url = request.args.get('url', default="", type=str)
    topic = request.args.get('topic', default="", type=str)
    if url:
        # print(topic,url)
        # remove image from image to public
        remove_url_from_image_to_public(topic, url)
    return [topic, url]
    
@app.route('/show', methods=['GET', 'POST'])
def show_image():
    return render_template('show_image.html', list_topics=_TOPPICS, topic=_DEFAULT_TOPIC)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4040, debug=True)