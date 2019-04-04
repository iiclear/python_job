import requests
from bs4 import BeautifulSoup
pic_info=[]
def weburl():
    api = 'http://www.doutula.com/photo/list/?page='
    url_list=[]
    for i in range(1,2):
        url = api+str(i)
        url_list.append(url)
    return url_list
    pass
def parse_pic(url_list):
    for url in url_list:
        res = requests.get(url)
        webdata = BeautifulSoup(res.text,'lxml')
        pics_data = webdata.select('#pic-detail > div > div.col-sm-9 > div.random_picture > ul > li > div > div > a')
        for pic in pics_data:
            name = pic.select('a > p')[0].get_text()
            uri = pic.select('a > img')[0].get('data-original')
            item = []
            if uri:
                item.append(name)
                item.append(uri)
                pic_info.append(item)




def download(pic_info):
    for item in pic_info:
        name = item[0]
        uri = item[1]
        with open('./pics/'+name+'.jpg','wb') as f:
            res =requests.get(uri)
            f.write(res.content)

if __name__ == '__main__':
    urls = weburl()
    parse_pic(urls)
    download(pic_info)
