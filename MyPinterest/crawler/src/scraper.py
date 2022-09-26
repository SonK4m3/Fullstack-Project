import requests
import json
import os
import urllib

PATH = 'd:\\Python\\Flask\\MyPinterest\\crawler'
URL = None

'''
d is list or dictionary
if d has json objects, we find object has format "orig" : { ... 
                                                            "url" : ..... }
we repeat search in elements of object
return image url 
'''
def search(d):
    global URL
    if isinstance(d, dict):
        for k, v in d.items():
            if isinstance(v, dict):
                if k == "orig":
                    URL = v["url"]
                    print(URL)
                else:    
                    search(v)
            elif isinstance(v, list):
                for item in v:
                    search(item)
        
def find_file(name):
    current_path = __file__.replace(__file__.split('\\')[-1], name)
    return current_path

class Scraper:
    def __init__(self, config, image_urls=[]):
        self.config = config
        self.image_urls = image_urls

    # Set config for bookmarks (next page)
    def setConfig(self, config):
        self.config = config

    # Download images
    def download_images(self, output_path):
        # prev get links
        results = self.get_urls()
        
        #debug
        print('--------------------')
        print('created get_urls.json')
        filename = PATH + '/debug/get_urls.json'
        write_json(filename, results)


        try:
            os.makedirs(output_path)
            print("Directory ", output_path, " Created ")
        except FileExistsError:
            pass
        
        number = 0
        listdir = os.listdir(output_path)

        if results != None:
            for i in results:
                #get image path
                file_name = i.split("/")[-1]
                if file_name not in listdir:
                    try:
                        number += 1
                        #debug
                        # print("Download ::: ", i)

                        #download image from browser
                        urllib.request.urlretrieve(i, os.path.join(output_path, file_name))
                    except Exception as e:
                        print("Error:", e)

        return number

    # get_urls return array
    def get_urls(self):
        global URL

        SOURCE_URL = self.config.source_url,
        DATA = self.config.image_data,
        URL_CONSTANT = self.config.search_url

        #get html file
        r = requests.get(URL_CONSTANT, params={
                         "source_url": SOURCE_URL, "data": DATA})
        #convert to json
        jsonData = json.loads(r.content)
        #select elements
        resource_response = jsonData["resource_response"]
        data = resource_response["data"]
        results = data["results"]

        #debug

        print('-------------------')
        print('created resource_response.json')
        write_json(PATH + '/debug/resource_response.json', resource_response)

        print('-------------------')
        print('created data.json')
        write_json(PATH + '/debug/data.json', data)

        print('-------------------')
        print('created result.json')
        write_json(PATH + '/debug/results.json', results)

        #get image url
        for i in results:
            try:
                #select elements has "url"
                self.image_urls.append(i["objects"][0]["cover_images"][0]["originals"]["url"])
            except:
                #if i hasn't has "url" we find in subelement
                URL = None
                #search algorithm
                search(i)
                if URL != None:
                    self.image_urls.append(URL)

        #return number of url under file_length
        if len(self.image_urls) < int(self.config.file_length):
            try:
                print("Creating links", len(self.image_urls))
                return self.image_urls[0:self.config.file_length]
            except:
                pass

def write_json(filename, data):
    if not os.path.exists(filename):
        with open(filename, 'w', encoding='utf8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)