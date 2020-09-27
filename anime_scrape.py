# noornee
import requests
from bs4 import BeautifulSoup
import pprint as p
import webbrowser as wb


raw = 'http://takanimelist.live/?s='
query = input('anime: ')
url = raw + query
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')
content = soup.find_all('div', attrs={'class': 'featured-thumb'})

main_url = []  # an important list!-goes all the way down

####################Start########################################Start####################
new_req = str(content)
new_soup = BeautifulSoup(new_req, 'html.parser')
new_content = new_soup.find_all('a')
values = []

for i in new_content:
    link = i['href']
    title = i['title']
    values.append({'title': title, 'link': link})

titles = []
for i in range(len(values)):
    titles.append(values[i]['title'])


# A function to list the results
def query_results():
    print('here are the result(s): ')
    index = []
    for i, val in enumerate(titles):
        print(f'{i}) {val}')
        index.append(i)
        continue
    n = input('input the number that matches what you want: ')
    num = int(n)
    if num in index:
        for i in range(len(values)):
            if titles[num] == values[i]['title']:
                main_url.append(values[i]['link'])


query_results()  # calling the function

####################End########################################End###############

####################Start########################################Start##########
####################Getting anime list##########################################

def get_anime_list():
    url = main_url[0]
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    links = soup.select("a[href*=mkv]")
    val = []  # very important list!

    for i, link in enumerate(links):
        text = link.get_text()
        # href = link['href']
        print(f'{text} ===> {i}')
        continue
    n = input('pick the number after ===> that matches the episode you want: ')
    num = int(n)
    for i in links:
        val.append(i['href'])
    print('opening browser to download... ')
    wb.open(val[num])
    # continue


get_anime_list()

####################End########################################End####################
