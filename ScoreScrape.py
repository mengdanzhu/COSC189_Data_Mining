import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
from boilerpipe.extract import Extractor
import nltk
import pickle
import re
fun = 'https://steamcommunity.com/app/{}/homecontent/?userreviewsoffset=20&p=3&workshopitemspage=3&readytouseitemspage=3&mtxitemspage=3&itemspage=3&screenshotspage=3&videospage=3&artpage=3&allguidepage=3&webguidepage=3&integratedguidepage=3&discussionspage=3&'
len(re.findall(r'=\d+',fun))
deft = 'numperpage=10&browsefilter=toprated&browsefilter=toprated&appid={}&appHubSubSection=10&appHubSubSection=10&l=english&filterLanguage=default&searchText=&forceanon=1'
flx = re.sub(r'=\d+','={}',fun)
#url = flx+deft
help = []
vote = []
hour = []
rev4id = []
with open('D:\\Program\\OneDrive\\Attachment\\Work Space\\Data Mining\\Project\\SteamWeb\\outfile.txt','rb') as fp:
    usefulid = pickle.load(fp)
mscore=[]
count = 0
for game in usefulid:
    url = "https://store.steampowered.com/app/{}/".format(game)
    page = requests.get(url)
    soup = BeautifulSoup(page.content,"lxml")
    score = soup.find('div', class_='score high')
    if score is not None:
        score = score.get_text()
        score = int(re.findall(r'\d+',score)[0])
    else:
        score = np.nan
    mscore.append(score)
    count += 1
    print(count)
    
with open('D:\\Program\\OneDrive\\Attachment\\Work Space\\Data Mining\\Project\\SteamWeb\\mscore.txt','wb') as fp:
    pickle.dump(mscore,fp)
    
with open('D:\\Program\\OneDrive\\Attachment\\Work Space\\Data Mining\\Project\\SteamWeb\\mscore.txt','rb') as fp:
    test = pickle.load(fp)