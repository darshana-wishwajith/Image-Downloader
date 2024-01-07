import requests
from urllib import request
from bs4 import BeautifulSoup

def check_connection():
    try:
        request.urlopen('https://www.google.com/', timeout = 5)
        print("\nConnected!")

    except:
        print("Check your internet connection !")
        exit()

check_connection()

page_link_input = input("\n\nEnter a Web page link : ")
url_file = 'urls.txt'
link_list = []
page_link = requests.get(page_link_input)

bsoup = BeautifulSoup(page_link.content, 'html.parser')
links = bsoup.find_all('a')

for link in links:
    if "href" in link.attrs and link['href'].endswith('jpg'):
        link_list.append(link)
        #print(str(link.attrs['href']) + "\n") 

with open(url_file, 'w') as urls:
    for link in link_list :
        urls.write(str(link.attrs['href']) + "\n")
        urls.write("\n")


