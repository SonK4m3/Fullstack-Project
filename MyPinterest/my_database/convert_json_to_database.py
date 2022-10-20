import sqlite3
import json
import os

_JSON_URL = 'D:/Python/Flask/MyPinterest/backend/topics'
_DATABASE_TABLE = 'D:/Python/Flask/MyPinterest/my_database/data/my_pinterest_database.db'

def read_json(filename):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            return data
    except Exception as e:
        # with open(filename, 'w', encoding='utf8') as f:
        #     json.dump([], f, indent=4, ensure_ascii=False)
        return []
    
def create_table(database=_DATABASE_TABLE):
    con = sqlite3.connect(database)
    cur = con.cursor()
    try:
        query = "CREATE TABLE TOPIC(topic VARCHAR(50) PRIMARY KEY)"
        cur.execute(query)
    except Exception as e:
        print(e)
        
    try:
        query = "CREATE TABLE IMAGE(topic VARCHAR(50), url VARCHAR(200) PRIMARY KEY)"
        cur.execute(query)
    except Exception as e:
        print(e)
     
    try:
        query = "CREATE TABLE PUBLIC(topic VARCHAR(50), url VARCHAR(200) PRIMARY KEY)"
        cur.execute(query)
    except Exception as e:
        print(e)   
    
    cur.execute('SELECT * FROM sqlite_master')
    print(cur.fetchall())
    
def add_topic(topic, database=_DATABASE_TABLE):
    con = sqlite3.connect(database)
    cur = con.cursor()
    #check topic is exited ?
    cur.execute("SELECT * FROM TOPIC WHERE topic = '{}'".format(topic))
    if cur.fetchone() is None:
        #query to insert topic to database
        query = "INSERT INTO TOPIC(topic) VALUES ('{}')".format(topic)
        cur.execute(query)
    #save changed database
    con.commit()
    #debug - check added topic
    cur.execute('SELECT * FROM TOPIC')
    print(cur.fetchall())
    cur.close()
    con.close()
    
    
def add_image(topic, data:list, database=_DATABASE_TABLE):
    con = sqlite3.connect(database)
    cur = con.cursor()
    cnt = 0
    for url in data:
        # url is primary key so when has 2 the same url, program will be error
        #check duplicated url
        cur.execute("SELECT url FROM IMAGE WHERE url='{}'".format(url))
        url_s = cur.fetchone()
        
        if url_s is None:
            cur.execute("INSERT INTO IMAGE(topic, url) VALUES ('{}', '{}')".format(topic, url))
            cnt += 1
      
    #save added data
    con.commit()
    #debug - show table image to check data
    print('add {} urls'.format(cnt))
    cur.execute("SELECT * FROM IMAGE  WHERE topic = '{}' LIMIT 5".format(topic))
    print("topic  | url")
    for info in cur.fetchall():
        print(f"{info[0]} | {info[1]}")
    cur.close()
    con.close()

def get_url(topic, database=_DATABASE_TABLE):
    con = sqlite3.connect(database)
    cur = con.cursor()
    
    query = "SELECT url FROM IMAGE WHERE topic='{}'".format(topic)
    cur.execute(query)
    
    list_url = list(x[0] for x in cur.fetchall())

    print('list url: [' + str(list_url[0]) + ', ...]')
    
    return list_url

def get_number_url_of_topic(topic, database=_DATABASE_TABLE):
    con = sqlite3.connect(database)
    cur = con.cursor()
    
    query = "SELECT count(url) FROM IMAGE WHERE topic='{}' GROUP BY topic".format(topic)
    cur.execute(query)
    
    number = cur.fetchone()[0]
    print(number)
    return number
    

def convert_json_to_database():
    create_table()
    
    list_file = os.listdir(_JSON_URL)
    for file_name in list_file:
        file_path = _JSON_URL + '/' + file_name
        
        data = read_json(file_path)
        topic = file_name.split('.')[0]
    
        print(file_path, topic, len(data))
        
        add_topic(topic)
        add_image(topic, data)

if __name__ == '__main__': 
    # create_table()

    list_file = os.listdir(_JSON_URL)
    for file_name in list_file:
        file_path = _JSON_URL + '/' + file_name
        data = read_json(file_path)
        topic = file_name.split('.')[0]
        
        add_topic(topic)
        add_image(topic, data)
        
    
    
        