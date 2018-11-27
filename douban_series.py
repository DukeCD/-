# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 16:33:06 2018

@author: Duke
"""
import requests
import time
from bs4 import BeautifulSoup
import re
import json

def get_page(i):
    url='https://movie.douban.com/j/new_search_subjects?sort=U&range=9,10&tags=%E7%94%B5%E8%A7%86%E5%89%A7&start='+str(i*20)
    headers={'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36'}
    response=requests.get(url,headers=headers)    
    json_data=json.loads(response.text)
    return json_data
def save_data(json_data):
    with open('高分电视剧.txt','a') as f:
        for data in json_data['data']:
            f.write(data['title']+'\t'+data['rate']+'\n')
def main():
    for i in range(100):       
        json_data=get_page(i)
        save_data(json_data)
        time.sleep(0.01)
        
        
if __name__=="__main__":
    main()
        