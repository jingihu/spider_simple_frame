import requests
import random
from other_config.User_Agent import USER_AGENT_LIST


class HtmlDownload(object):

    def download(self,url):
        if url is None:
            return
        req = requests.Session()
        req.headers['User-Agent'] = random.choice(USER_AGENT_LIST)
        res = req.get(url)

        #判断是正常获取
        if res.status_code == 200:
            res.encoding = 'utf-8'
            res = res.text

            return res
        return None
