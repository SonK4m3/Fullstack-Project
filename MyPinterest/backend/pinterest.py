import json
import random
import traceback

PATH = 'D:\Python\Flask\MyPinterest/backend/topics/{}.json'
PUBLIC_PATH = 'D:\Python\Flask\MyPinterest/backend\datas\public_urls.json'
REFUSE_PATH = 'D:\Python\Flask\MyPinterest/backend\datas/refuse_urls.json'

def write_json(filename, data):
    with open(filename, 'w', encoding='utf8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def rewrite_json(filename, data):
    old_data = read_json(filename)
    new_data = old_data + data
    write_json(filename, new_data)

def read_json(path):
    try:
        with open(path, 'r') as f:
            data = json.load(f)
            return data
    except Exception as e:
        with open(path, 'w', encoding='utf8') as f:
            json.dump([], f, indent=4, ensure_ascii=False)
        return []

def get_image(topic):
    data = read_json(PATH.format(topic))
    return random.choice(data)

def get_list_image(topic):
    data = read_json(PATH.format(topic))
    return data

def get_list_public_image():
    data = read_json(PUBLIC_PATH)
    return data

def get_set_image(topic, number):
    data = read_json(PATH.format(topic))
    number = int(number)
    if number > len(data):
        number = len(data)
    elif number < 0:
        number = 1
    return random.sample(data, number)

def add_json(filename, data):
    datas = read_json(filename)
    datas.append(data)
    write_json(filename, datas)

def pop_json(filename):
    datas = read_json(filename)
    datas.pop()
    write_json(filename, datas)
    
if __name__ == '__main__':
    path = 'D:\Python\Flask\MyPinterest/backend/topics/test.json'