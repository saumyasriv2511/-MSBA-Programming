# -*- coding: utf-8 -*-
# importing libraries
import matplotlib.pyplot as plt
from wordcloud import WordCloud,STOPWORDS
from stop_words import get_stop_words
import numpy as np
from PIL import Image
import csv
import json
import random 

# Created a generalized function which can be called
def cloud_of_words(filename):
    text=""
    if filename.endswith('txt'):
        text = open(filename).read()
    elif filename.endswith('json'):
        # list of dictionaries with 'News' as key
        with open(filename,'r') as f:
            data = json.load(f)    
        for i in range(len(data)):
            for j in range(len(data[i]['News'])):
                text+=data[i]['News'][j]
    
       
 
    img_mask = np.array(Image.open(filename.split('.')[0]+".png"))
    
    stoplist = []

    with open('stopwords.txt','r') as f:
        for row in csv.reader(f):
                stoplist+=row 
    
    stoplist = [x.lower() for x in stoplist] 
    
    wordcloud = WordCloud(background_color="white",min_font_size=1,max_font_size=100,stopwords=stoplist,mask=img_mask,max_words=1000).generate(text)

    plt.imshow(wordcloud.recolor(color_func=grey_color_func,random_state=3), interpolation="bilinear")
    plt.axis("off")

    
    plt.show()

def grey_color_func(word, font_size, position, orientation, random_state=None,**kwargs):
    return "hsl(%d, %d%%, %d%%)" % (random.randint(120, 140),random.randint(0, 50),random.randint(0, 50))
   
    
    # Hue-Saturation-Lightness (HSL) functions, given as “hsl(hue, saturation%, lightness%)” 
    # where hue is the colour given as an angle between 0 and 360 (red=0, green=120, blue=240), 
    # saturation is a value between 0% and 100% (gray=0%, full color=100%), and 
    # lightness is a value between 0% and 100% (black=0%, normal=50%, white=100%). 
    # For example, “hsl(0,100%,50%)” is pure red.
    # color = 'hsl(%d, %d%%, %d%%)' % (hue, saturation, luminance)