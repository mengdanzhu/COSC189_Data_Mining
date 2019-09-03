steam_users_table = pd.read_csv("D:\\Program\\OneDrive\\Attachment\\Work Space\\Data Mining\\Project\\SteamWeb\\id_score.csv")
#from sklearn.utils import shuffle
#df = shuffle(steam_users_table)
app_id = steam_users_table.drop(index=0)["AppID"].to_list()
tostr = lambda x: '%d' %x
id = list(map(tostr,app_id))

usefulid = []
for game in id:
    url = "https://store.steampowered.com/app/{}/".format(game)
    page = requests.get(url)
    soup = BeautifulSoup(page.content,"lxml")
    score = soup.find('div', class_='score high')
    if score is not None:
        usefulid.append(game)
    if len(usefulid)>=500:
        break
    print(len(usefulid))

import pickle
with open('D:\\Program\\OneDrive\\Attachment\\Work Space\\Data Mining\\Project\\SteamWeb\\outfile.txt','wb') as fp:
    pickle.dump(usefulid,fp)

with open('D:\\Program\\OneDrive\\Attachment\\Work Space\\Data Mining\\Project\\SteamWeb\\outfile.txt','rb') as fp:
    test = pickle.load(fp)
