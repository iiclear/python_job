import requests
from bs4 import BeautifulSoup
import threading
from queue import Queue
pic_info_q=Queue()
url_list_q =Queue()
def weburl():
    api = 'http://www.doutula.com/photo/list/?page='
    for i in range(1,3):
        url = api+str(i)
        url_list_q.put(url)

    pass
def parse_pic():
    url =url_list_q.get()
    res = requests.get(url)
    webdata = BeautifulSoup(res.text, 'lxml')
    pics_data = webdata.select('#pic-detail > div > div.col-sm-9 > div.random_picture > ul > li > div > div > a')
    for pic in pics_data:
        name = pic.select('a > p')[0].get_text()
        uri = pic.select('a > img')[0].get('data-original')
        item = []
        if uri:
            item.append(name)
            item.append(uri)
            pic_info_q.put(item)





def download():
    while True:
        item = pic_info_q.get()
        name = item[0]
        uri = item[1]
        back = item[1].split('.')
        print(back)
        with open('./pics/' + name + '.' +back[3], 'wb') as f:
            res = requests.get(uri)
            f.write(res.content)
        f.close()



if __name__ == '__main__':
    threads = []
    t1 = threading.Thread(target=weburl)
    t1.start()
    threads.append(t1)

    for i in range(5):
        t = threading.Thread(target=parse_pic)
        threads.append(t)
        t.start()


    for i in range(10):
        t = threading.Thread(target=download)
        t.setDaemon(True)
        t.start()
        threads.append(t1)

    for t in threads:
        t.join()
    print('well done')