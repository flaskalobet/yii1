from bs4 import BeautifulSoup
import urllib2

def mysoup(link):

    url = urllib2.Request(link, headers={ 'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:33.0) Gecko/20100101 Firefox/33.0' })
    #html = urllib2.urlopen(req).read()

    #url= 'http://clip.vn'
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page.read())
    return soup

soup = mysoup("http://vtv.vn/truyen-hinh-truc-tuyen.htm")
videos_new = soup.find("div",{"class":"video-news-box"}).find("ul",{"class":"list-item"}).find_all("li")

links = []

for video in videos_new:
    link = "http://vtv.vn"+video.find("a").get("href")
    links.append(link)


for link in links:
    getinfos = mysoup(link).find("div",{"class":"inner"})
    title = getinfos.find("h1",{"class":"news-title"}).string.replace("''","'").replace('"','\'')
    desc = getinfos.find("h2",{"class":"news-sapo"}).string.replace("''","'").replace('"','\'')
    link_key = mysoup(link).find("div",{"class":"clearfix inner"}).find("param",{"name":"movie"}).get("value")

    keyw = "nettv"
    tags = mysoup(link).find("div",{"class":"tag"}).find_all("li")
    for tag in tags:
        if len(tag.string) < 30:
            keyw += ","+ tag.string

    print title, desc, keyw
    print link_key

