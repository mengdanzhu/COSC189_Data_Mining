import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
from boilerpipe.extract import Extractor
import nltk
import random
id = pd.read_csv("D:\Program\OneDrive\Attachment\Work Space\Data Mining\Project\SteamWeb\\id_score.csv")
id = id['AppID']
random.shuffle(id)
id = list(map(lambda x:'%d' %x,id))
id = id[0:500]
#####
import re
fun = 'https://steamcommunity.com/app/{}/homecontent/?userreviewsoffset=20&p=3&workshopitemspage=3&readytouseitemspage=3&mtxitemspage=3&itemspage=3&screenshotspage=3&videospage=3&artpage=3&allguidepage=3&webguidepage=3&integratedguidepage=3&discussionspage=3&'
len(re.findall(r'=\d+',fun))
deft = 'numperpage=10&browsefilter=toprated&browsefilter=toprated&appid={}&appHubSubSection=10&appHubSubSection=10&l=english&filterLanguage=default&searchText=&forceanon=1'
flx = re.sub(r'=\d+','={}',fun)
#url = flx+deft
help = []
vote = []
hour = []
text = []
nmae = []
count = 0
for game in id:
    default = deft.format(game)
    par = [game] + [(1-1)*10] + [1]*12
    for i in range(1,30):
        par = [game] + [(i-1)*10] + [i]*12
        flexible = flx.format(*par)
        #flexible = flx.format(game,(i-1)*10,i,i,i,i,i,i,i,i,i,i,i,i)
        url = flexible + default
        page = requests.get(url)
        soup = BeautifulSoup(page.content,'lxml')
        reviews = soup.find_all('div', class_='apphub_Card')
        for review in reviews:
            #name.append(tit)
            help.append(review.find('div', class_='found_helpful').get_text())
            vote.append(review.find('div', class_='title').get_text())
            rev = review.find('div', class_='apphub_CardTextContent')
            if rev is not None:
                text.append(rev.get_text())
            else:
                text.append("None")
    count += 1
    print(count)
        #name = [tit]**len(reviews)
#Build a dictionary
dic = {'text':text,'vote':vote,'help':help}
text4cls = pd.DataFrame(dic)
text4cls.to_csv('D:\\Program\\OneDrive\\Attachment\\Work Space\\Data Mining\\Project\\text4cls.csv')

import json
with open('D:\Program\OneDrive\Attachment\Work Space\Data Mining\Project\data.json','w') as fp:
    json.dump(dic,fp)


#Load the data
with open('D:\Program\OneDrive\Attachment\Work Space\Data Mining\Project\data.json','r') as fp:
    data = json.load(fp)
#Normalization












for game in ['548570','931280','271590']:
    default = deft.format(game)
    par = [game] + [(1-1)*10] + [1]*12
    #titlelink = flx.format(*par) + default
    #title = BeautifulSoup(requests.get(titlelink).content,'lxml')
    #tit = title.find('div',class_="apphub_AppName ellipsis")[1]
    for i in range(1,100):
        par = [game] + [(i-1)*10] + [i]*12
        flexible = flx.format(*par)
        #flexible = flx.format(game,(i-1)*10,i,i,i,i,i,i,i,i,i,i,i,i)
        url = flexible + default
        page = requests.get(url)
        soup = BeautifulSoup(page.content,'lxml')
        reviews = soup.find_all('div', class_='apphub_Card')
        for review in reviews:
            #name.append(tit)
            help.append(review.find('div', class_='found_helpful').get_text())
            vote.append(review.find('div', class_='title').get_text())
            hour.append(review.find('div', class_='hours').get_text())
            rev = review.find('div', class_='apphub_CardTextContent')
            if rev is not None:
                text.append(rev.get_text())
            else:
                text.append("None")
        #name = [tit]**len(reviews)
#Build a dictionary
dic = {'text':text,'vote':vote,'hour':hour,'help':help}
import json
with open('D:\\Program\\OneDrive\\Attachment\\Work Space\\Data Mining\\Project\\val.json','w') as fp:
    json.dump(dic,fp)