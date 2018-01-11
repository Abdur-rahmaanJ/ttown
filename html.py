# -*- coding: utf-8 -*-
import json
import time
import io
"""
Created on Tue Jan  9 18:24:17 2018

@author: arj


<div class="flow plugin">
  <div class="plugin-author">
   ***author***
  </div>
  <div class="plugin-note">
    <div class="plugin-note-title">
    ***name***
    </div>
    <div class="plugin-pic">
     <img class= "plugin-img" src="***imglink***">
     </div>
    <div class="plugin-note-div">
      
    </div> 
  </div>
  <a href="">
  <div class="plugin-download">
    download <i class="fa fa-download"></i>
  </div> 
    </a><br>
</div><!--plugin end -->
    """
    
temp = '''
<div class="flow plugin">
  <div class="plugin-author">
   ***author***
  </div>
  <div class="plugin-note">
    <div class="plugin-note-title">
    ***name***
    </div>
    <div class="plugin-pic">
     <img class= "plugin-img" src="***imagelink***">
     </div>
    <div class="plugin-note-div">
      ***descrip***
    </div> 
  </div>
  <div class="plugin-resolve"></div>
  ***atemp***
</div><!--plugin end -->
'''
atemp = '''
  <a href="***link***">
  <div class="plugin-download">
    download <i class="fa fa-download"></i>
  </div> 
    </a>
'''
a2temp = '''
  <a href="***link***">
  <div class="plugin-download">
    see <i class="fa fa-search"></i>
  </div> 
    </a>
'''
x = {}
with open('data/data_.json', 'r') as f:
    x = json.load(f)

file = io.open('html/misc_'+str(int(time.time()))+'.html', 'w', encoding="utf-8")
    
plugins = [] 
for key in x:
    author, descrip, images, name, res = '', '', '#', '', []
    if x[key]['tag'] == 'Miscellaneous':
        ress = ''
        name = key
        author = x[key]['author']
        descrip = x[key]['descrip']
        res = x[key]['res']
        if author == 0:
            author = 'unretrieved'
        if x[key]['images'] != []:
            images = x[key]['images'][0]
        for link in res:
            print(link)
            if 'download' in link:
                temp_now = atemp.replace('***link***',link)
                ress += temp_now+'\n'
            else:
                temp_now = a2temp.replace('***link***',link)
                ress += temp_now+'\n'
                
        print(ress)
        temp_now = temp.replace('***author***', author).replace('***name***', name).replace('***descrip***', descrip).replace('***imagelink***', images).replace('***atemp***', ress)
        file.write(temp_now)
        file.flush()
file.close()
print('term ...')
            

    
            
        











