import os
import random
import argparse
from itertools import combinations
from src import PinterestScraper, PinterestConfig

PATH = 'D:/Python/Flask/MyPinterest/backend/topics'
OUT_PUT = 'D:\Python\Flask\MyPinterest\crawler\photos'

def remove_dir(filename):
    if os.path.exists(filename):
        os.remove(filename)

def make_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        
def find_file(name):
    current_path = __file__.replace(__file__.split('\\')[-1], name)
    return current_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--keywords", default="keywords.txt", help="path to input image")
    parser.add_argument('--output', help='output dir', default=PATH, type=str)
    parser.add_argument("-nw", '--number-of-words', help='number of keywords for search', default=2, type=int)
    args = parser.parse_args()

    #debug
    print('----------------------')
    print(args)

    file = open(find_file(args.keywords), "r")
    keywords = file.read().split('\n')
    keywords = [keyword.strip() for keyword in keywords]

    #debug
    print('-------------------')
    print(keywords)


    # print("start crawling...")
    random.shuffle(keywords)
    counter = 0
    if len(keywords)==1:args.number_of_words=1
    for item in combinations(keywords, args.number_of_words):

        keyword = " ".join(word for word in item)

        while True:
            configs = PinterestConfig(search_keywords=keyword,  # Search word
                                    file_lengths=5000,  # total number of images to download (default = "100")
                                    image_quality="originals",  # image quality (default = "orig")
                                    bookmarks="",  # next page data (default= "")
                                    scroll=1000)

            PinterestScraper(configs).download_images(OUT_PUT)  # download images directly
            print('done')