import sqlite3

_DATABASE = "D:/Python/Flask/MyPinterest/my_database/data/my_pinterest_database.db"    
 
def con_cur(database):
        con = sqlite3.connect(database)
        cur = con.cursor()
        return con, cur 
    
    
def get_list_urls(topic, table='IMAGE', database=_DATABASE):
    con, cur = con_cur(database)
        
    query = "SELECT url FROM {} WHERE topic='{}'".format(table, topic)
    cur.execute(query)
        
    list_urls = [url[0] for url in cur.fetchall()]
    return list_urls
        
        
def get_random_url(topic, number=1, database=_DATABASE):
    con, cur = con_cur(database)

    query = "SELECT url FROM IMAGE WHERE topic='{}' ORDER BY random() LIMIT {}".format(topic, number)
    cur.execute(query)
        
    set_urls = [url[0] for url in cur.fetchall()]
    return set_urls[0] if len(set_urls) == 1 else set_urls  


def get_all_topics(database=_DATABASE):
    con, cur = con_cur(database)
        
    query = "SELECT topic FROM TOPIC"
    cur.execute(query)
        
    all_topics = [topic[0] for topic in cur.fetchall()]
    return all_topics


def remove_url_image(url, table='IMAGE', database=_DATABASE):
    con, cur = con_cur(database)
    
    query = "DELETE FROM {} WHERE url='{}'".format(table, url)
    cur.execute(query)
    con.commit()
    #check in database
    # cur.execute("SELECT url FROM {} WHERE url='{}'".format(table, url))
    # print(cur.fetchall())
   
    
def add_url_image(topic, url, table='IMAGE', database=_DATABASE):
    con, cur = con_cur(database)
    
    query = "INSERT INTO {}(topic, url) VALUES ('{}', '{}')".format(table, topic, url)
    try:
        cur.execute(query)
    except Exception as e:
        print("Data is existed, ", e)
    con.commit()
    #check url is added
    # cur.execute("SELECT topic, url FROM {} WHERE url='{}'".format(table, url))
    # print(cur.fetchall())  
   
def remove_url_from_image_to_public(topic, url, database=_DATABASE):
    remove_url_image(url)
    add_url_image(topic, url, 'PUBLIC')
    
def get_list_urls_public(database=_DATABASE):
    con, cur = con_cur(database)
        
    query = "SELECT url FROM PUBLIC"
    cur.execute(query)
        
    list_urls = [url[0] for url in cur.fetchall()]
    return list_urls
    
if __name__ == '__main__':
    topic = 'pokemon'
    # print(get_list_urls('pokemon'))
    # url = get_random_url(topic)
    # url = 'son'
    # print(url)
    
    # remove_url_image(url, 'PUBLIC')

    # print(get_all_topics())
    
    # add_url_image(topic, url, 'PUBLIC')
    
