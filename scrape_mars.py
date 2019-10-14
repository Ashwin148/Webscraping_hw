#!/usr/bin/env python
# coding: utf-8

# In[51]:


import pandas as pd
import os
import requests
from bs4 import BeautifulSoup as bs
from splinter import Browser


# # Scrape everything
# 

# In[52]:


# this dictionary will hold everything we pull from all the sites
scraped_data = {}


# In[53]:


# site 1 -
news_url = "https://mars.nasa.gov/news/" # probably need to replace this since it redirects
longlink = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"

#with open(longlink, encoding='utf-8') as file:
  #  html = file.read()
# use beautiful soup to parse the url above
response = requests.get(longlink)

soup = bs(response.text, 'html.parser')
#def OutputSoup(soup):
 #  with open('myout.html','w',encoding='utf-8') as file:
  #     file.write(str(soup))
#OutputSoup
soup


# In[57]:


#example_title_div = '<div class="content_title"><a href="/news/8522/nasas-curiosity-rover-finds-an-ancient-oasis-on-mars/" target="_self">NASA's Curiosity Rover Finds an Ancient Oasis on Mars</a></div>'
#example_paragraph_div = '<div class="article_teaser_body">New evidence suggests salty, shallow ponds once dotted a Martian crater — a sign of the planet's drying climate.</div>'

# use bs to find() the example_title_div and filter on the class_='content_title'
#news_title = soup.find_all('div', class_="content_title")
nt_level1 = soup.find_all('div',class_='content_title')
news_title = nt_level1[0].text.strip()

#news_title = "FILL IN THE TITLE"
scraped_data['news_title'] = news_title

# use bs to find() the example_title_div and filter on the class_='article_teaser_body'
#news_p = soup.find_all('div', class_="rollover_description_inner")
np_level1 = soup.find_all('div',class_='rollover_description_inner')
news_p = np_level1[0].text.strip()
#scraped_data['news_p'] = news_p
#news_p = "FILL IN THE PARAGRAPH"
scraped_data['news_p'] = news_p
scraped_data


# In[70]:


import time
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)
browser.visit(url)
time.sleep(2)
html = browser.html
soup = bs(html, "html.parser")
result = soup.find_all('a',class_='fancybox')
print(result[0]) #look at the first result


# In[86]:


marsimage = soup.find('a',class_='fancybox')['data-fancybox-href']
print(marsimage)


# In[87]:


part1 = 'https://www.jpl.nasa.gov'
featured_image_url = part1 + marsimage
featured_image_url


# In[88]:


scraped_data['featured_image_url'] = featured_image_url
scraped_data


# In[94]:


html3 = 'https://twitter.com/marswxreport?lang=en'
response2 = requests.get(html3)

soup = bs(response2.text, 'html.parser')
# grab the latest tweet and be careful its a weather tweet
soup
# Example:
#mars_weather = 'Sol 1801 (Aug 30, 2017), Sunny, high -21C/-5F, low -80C/-112F, pressure at 8.82 hPa, daylight 06:09-17:55'


# In[98]:


twitter1 = soup.find_all('p',class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text')
twitter = twitter1[0].text.strip()
twitter


# In[99]:


scraped_data['twitter'] = twitter
scraped_data


# In[100]:


# site 4 - 
facts_url = 'https://space-facts.com/mars/'
response3 = requests.get(facts_url)

soup = bs(response3.text, 'html.parser')
soup
# use pandas to parse the table

#facts_df = pd.read_html(facts_url)[0]

# convert facts_df to a html string and add to dictionary.


# In[105]:


marsfacts1 = soup.find_all('table',class_='tablepress tablepress-id-p-mars')
#twitter = twitter1[0].text.strip()
marsfacts = marsfacts1[0].text.strip()
marsfacts


# In[108]:


facts_df = pd.read_html(facts_url)[0]
facts_df


# In[112]:


facts_html = pd.DataFrame.to_html(facts_df)
facts_html


# In[114]:


scraped_data['facts_df'] = facts_html
scraped_data


# In[115]:


marshemisphere = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

response4 = requests.get(marshemisphere)

soup = bs(response4.text, 'html.parser')
soup
# use bs4 to scrape the title and url and add to dictionary

# Example:


# In[135]:


title1 = soup.find_all('div',class_='description')
title2 = title1[0].find('h3').text
print(title2)


# In[ ]:





# In[150]:


url1 = soup.find_all('img',class_='item')
#url2 = url1[0].find('src')
print(url1)


# In[ ]:


hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/7cf2da4bf549ed01c17f206327be4db7_valles_marineris_enhanced.tif_full.jpg"},
    {"title": "Cerberus Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/cfa62af2557222a02478f1fcd781d445_cerberus_enhanced.tif_full.jpg"},
    {"title": "Schiaparelli Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/3cdd1cbf5e0813bba925c9030d13b62e_schiaparelli_enhanced.tif_full.jpg"},
    {"title": "Syrtis Major Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/ae209b4e408bb6c3e67b6af38168cf28_syrtis_major_enhanced.tif_full.jpg"},
]

scraped_data['hemisphereimage'] = hemisphere_image_urls
scraped_data
# In[ ]:


# File-> download as python into a new module called scrape_mars.py


# In[ ]:


# use day 3 09-Ins_Scrape_And_Render/app.py as a blue print on how to finish the homework.

# replace the contents of def index() and def scraper() appropriately.

# change the index.html to render the site with all the data.

from splinter import Browser

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    longlink = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    html3 = 'https://twitter.com/marswxreport?lang=en'
    facts_url = 'https://space-facts.com/mars/'
    marshemisphere = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    scraped_data["news_title"]
    scraped_data["news_p"]
    scraped_data["marsimage"]
    scraped_data["twitter"]
    scraped_data["facts_df"]
    scraped_data["hemisphereimage"]

     

    return scraped_data