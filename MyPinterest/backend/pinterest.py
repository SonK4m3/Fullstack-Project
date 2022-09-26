import json
import random
import traceback

PATH = 'D:\Python\Flask\MyPinterest\crawler\debug\get_urls.json'
PUBLIC_PATH = 'D:\Python\Flask\MyPinterest/backend\datas\public_urls.json'
REFUSE_PATH = 'D:\Python\Flask\MyPinterest/backend\datas/refuse_urls.json'

def write_json(filename, data):
    with open(filename, 'w', encoding='utf8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def read_json(path):
    try:
        with open(path, 'r') as f:
            data = json.load(f)
            return data
    except Exception as e:
        # print('Error while loading {}'.format(path), e)
        # traceback.print_exc()
        return []

def get_image():
    data = read_json(PATH)
    return random.choice(data)

def get_list_image():
    data = read_json(PATH)
    return data

def get_list_public_image():
    data = read_json(PUBLIC_PATH)
    return data

def get_set_image(number):
    data = read_json(PATH)
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
    url = get_image()
    # add_json(PUBLIC_PATH, url)
    pop_json(PUBLIC_PATH)