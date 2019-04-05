from fake_useragent import UserAgent
import requests
import tkinter
import pymongo
from bs4 import BeautifulSoup
class mongo():
    def conn_db(self):
        client = pymongo.MongoClient(host='localhost', port=27017)
        db = client.learnbyhard
        col = db.translate
        return col

    def save_to_local(self,word_list, col):
        for word in word_list:
            col.insert(word)

    def select(self,col,query):
        data ={
            "en":query
        }
        visable=['cn']
        res = col.find(data, projection=visable)
        for i in res:
            print(i['cn'])


class spider_online():
    url = 'https://mp.weixin.qq.com/s?__biz=MjM5MTY3MDIyMA%3D%3D&idx=1&mid=2651843517&sn=00efb2e7f23df5840ca35355e02b379b'
    def __init__(self,url):
        self.url = url
        pass
    def get_page(self):
        pass
    def parse_page(self):
        pass

    def spider(self):
        word_list = []
        ua = UserAgent()
        res = requests.get(self.url)
        data = BeautifulSoup(res.content, 'lxml')
        items = data.select('#js_content > section > section:nth-child(5) > section > section > p')
        for item in items:
            en = item.get_text().split(' ')[1]
            cn = item.get_text().split(' ')[2]
            word = {
                "en": en,
                "cn": cn
            }
            word_list.append(word)
        return word_list



def main():
    #爬取单词并存储
    # s=spider_online()
    # t = mongo()
    # conn = t.conn_db()
    # spider = s.spider()
    # t.save_to_local(spider,conn)

    #查询单词翻译
    t= mongo()
    s = input('输入单词:\n')
    t.select(t.conn_db(),s)



if __name__ == '__main__':
    main()