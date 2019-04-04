import requests
import time
import threading
from queue import Queue
from bs4 import BeautifulSoup

page_u = Queue(10)
page_d = Queue(250)
class CrawlerPageurl(threading.Thread):

    def run(self):
        url = 'https://movie.douban.com/top250?start='

        for i in range(20):
            time.sleep(0.2)
            u = url + str(i*25)
            page_u.put(u)
        print(time.time())



class CrawlerPagedata(threading.Thread):
    def run(self):

        while True:
            res = requests.get(page_u.get())

            soup = BeautifulSoup(res.text, 'lxml')
            for content in soup.select('#content > div > div.article > ol > li > div'):
                page_d.put(content)
            page_u.task_done()

class ParseInfo(threading.Thread):
    def run(self):
        global count
        count =0
        while True:
            count += 1
            info = page_d.get()

            title = info.select(' div.info > div.hd > a > span:nth-child(1)')[0].get_text()
            link = info.select('div.info > div.hd > a')[0].get('href')
            print(count,title, link)
            page_d.task_done()

def main():
    threads = []
    t1 = CrawlerPageurl()
    threads.append(t1)
    # for i in range(20):
    #     t2 = CrawlerPagedata()
    #     threads.append(t2)
    t2 = CrawlerPagedata()
    threads.append(t2)

    t3 = ParseInfo()
    threads.append(t3)
    # t1.start()
    #
    # t2.start()
    # t3.start()
    # threads.append(t1)
    # threads.append(t2)
    # threads.append(t3)
    for t in threads:
        # t.setDaemon(True)
        t.start()
    print('主线程结束')



if __name__ == '__main__':
    main()