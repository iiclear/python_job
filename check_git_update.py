import requests
import webbrowser
import time
api = "https://api.github.com/repos/huge-success/sanic"
web_page = 'https://github.com/huge-success/sanic'
all_info = requests.get(api).json()
cur_time = all_info['updated_at']
last_time = '2019-03-31T09:30:42Z'

while 1:
    if not last_time:
        last_time = cur_time
    if str(last_time) < str(cur_time):
        last_time = cur_time
        webbrowser.open(web_page)
    time.sleep(600)