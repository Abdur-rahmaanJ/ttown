# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 17:16:15 2018

@author: arj
"""
from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import urljoin
import json
import time

class Plugin:
    def __init__(self, name, author, description, images, resources, tag):
        self.name = name
        self.author = author
        self.description = description
        self.images = images
        self.resources = resources
        self.tag = tag
        
data = {}

forum_links = []
topic_links = []
plugins = []

json_data = {}

base = "http://www.theotown.com/forum/"
x = {}
with open('data/collected.json', 'r') as f:
    x = json.load(f)

topic_links = x['topic']            
data = topic_links[0]
link = data[0]
name = data[1]
tag = data[2]
images = []
res = []
descrip = []
username = 0

content = str(urllib.request.urlopen(link).read().decode('utf8'))
soup = BeautifulSoup(content,"html.parser")


body = soup.find("div", class_="post")
author_c = body.find("p", class_="author")
try:
    user = author_c.find("a", class_="username")
    username = user.string
except:
    pass

for L in body.find_all("img", class_="postimage"):
    if L.has_attr('src'):
        i_link = urljoin(base, L['src'])
        images.append(i_link)
        
for L in body.find_all("a", class_="postlink"):
    if L.has_attr('href'):
        i_link = urljoin(base, L['href'])
        res.append(i_link)
        
T = body.find("div", class_="content")
print("\nthe content of div is\n", T.text)
plugins.append(Plugin(name, username, str(T.text), images, res, tag))
# name, author, description, images, resources, tag):



for plugin in plugins:
    json_data[plugin.name] = {
            'author':plugin.author,
             'descrip':plugin.description,
             'images':plugin.images,
             'res':plugin.resources,
             'tag':plugin.tag
             }
    

j1 = json.dumps(json_data, indent=4)
with open('data/plugv5'+str(int(time.time()))+'.json', 'w+') as f:
    f.write(j1)