# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 17:33:45 2018

@author: ARJ
"""
from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import urljoin
import json
import time

#genFile = open("JUM/gen.html","w+")
#genFile.write("""<!DOCTYPE html>
#<html>
#<head>
#<style>
#.outer{border:5px solid black;}
#.tag{color:orange;}
#</style>
#</head>
#<body>""")
"""
enter base http://www.theotown.com/forum/viewforum.php?f=43
	look for links with class forumtitle
		open eg http://www.theotown.com/forum/viewforum.php?f=76
		look for links with class topictitle
			get text set as title
			eg open http://www.theotown.com/forum/viewtopic.php?f=76&t=5047
				get username with text of class username
				get images with class postimage
				get all resources with class postlink
"""

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
#
#link = "http://www.theotown.com/forum/viewforum.php?f=43"
#content = str(urllib.request.urlopen(link).read().decode('utf8'))
#soup = BeautifulSoup(content,"html.parser")
#
#for L in soup.find_all("a", class_="forumtitle"):
#    if L.has_attr('href'):
#        print(' '*10,'entered forum title')
#        title_link = urljoin(base, L['href'])
#        forum_links.append([title_link, L.string])
#        
#for f_link in forum_links:
#    link = f_link[0]
#    content = str(urllib.request.urlopen(link).read().decode('utf8'))
#    soup = BeautifulSoup(content,"html.parser")
#    for L in soup.find_all("a", class_="topictitle"):
#        if L.has_attr('href'):
#            title_link = urljoin(base, L['href'])
#            topic_links.append([title_link, L.string, f_link[1]])
#            
#print(forum_links)
#print(topic_links)
#json_1 = {'forum':forum_links, 'topic':topic_links}
#j_ = json.dumps(json_1, indent=4)
#with open('data/collected_'+str(int(time.time()))+'.json', 'w+') as f:
#    f.write(j_)

x = {}
with open('data/collected.json', 'r') as f:
    x = json.load(f)

topic_links = x['topic']            
for data in topic_links:
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
with open('data/plug_100_'+str(int(time.time()))+'.json', 'w+') as f:
    f.write(j1)
    
                        
                
                    
            
        



"""
{
     name:{
             link: <link here>,
             
     }
}
"""