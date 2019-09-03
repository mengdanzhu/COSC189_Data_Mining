from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import torch
import pandas as pd
from bs4 import BeautifulSoup
import os
driver = webdriver.Firefox(executable_path=r'D:\\Program\\OneDrive\\Desktop\\geckodriver-v0.24.0-win64\\geckodriver.exe')
#driver.get('https://steamdb.info/stats/gameratings/')
driver.get("https://steamdb.info/graph/")

select_dropdown = driver.find_element_by_id('table-apps_length')
for option in select_dropdown.find_elements_by_tag_name('option'):
    if option.text == 'All':
        option.click() 
        break

soup_level1=BeautifulSoup(driver.page_source, 'lxml')

class HTMLTableParser:
   
    def parse_url(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        return [(table['id'],self.parse_html_table(table))\
                for table in soup.find_all('table')]  
    
    def parse_soup(self, soup):
        return [(table['id'],self.parse_html_table(table))\
                for table in soup.find_all('table')]  

    def parse_html_table(self, table):
        n_columns = 0
        n_rows=0
        column_names = []
        for row in table.find_all('tr'):
            td_tags = row.find_all('td')
            if len(td_tags) > 0:
                n_rows+=1
                if n_columns == 0:
                    n_columns = len(td_tags)
            th_tags = row.find_all('th') 
            if len(th_tags) > 0 and len(column_names) == 0:
                for th in th_tags:
                    column_names.append(th.get_text())

        if len(column_names) > 0 and len(column_names) != n_columns:
            raise Exception("Column titles do not match the number of columns")

        columns = column_names if len(column_names) > 0 else range(0,n_columns)
        df = pd.DataFrame(columns = columns,
                          index= range(0,n_rows))
        row_marker = 0
        for row in table.find_all('tr'):
            column_marker = 0
            columns = row.find_all('td')
            for column in columns:
                df.iat[row_marker,column_marker] = column.get_text()
                column_marker += 1
            if len(columns) > 0:
                row_marker += 1
                
        for col in df:
            try:
                df[col] = df[col].astype(float)
            except ValueError:
                pass
        
        return df


hp = HTMLTableParser()
steam_users_table = hp.parse_soup(soup_level1)[0][1]
steam_users_table.head()
steam_users_table.shape
steam_users_table = steam_users_table.drop([' '], axis=1)
steam_users_table.drop(index=0)
steam_users_table.to_csv("D:\\Program\\OneDrive\\Attachment\\Work Space\\Data Mining\\Project\\SteamWeb\\id_score.csv")

app_id = steam_users_table["AppID"].to_list()
tostr = lambda x: '%d' %x
id = list(map(tostr,app_id))

steam_users_table = pd.read_csv("D:\\Program\\OneDrive\\Attachment\\Work Space\\Data Mining\\Project\\SteamWeb\\id_score.csv")
app_id = steam_users_table.drop(index=0)["AppID"].head(500).to_list()
tostr = lambda x: '%d' %x
id = list(map(tostr,app_id))























