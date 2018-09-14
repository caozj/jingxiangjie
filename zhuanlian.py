
import requests
from urllib.parse import quote


class ZhuanLian:
    def __init__(self,content):
        self.url = "http://qwd.jd.com/cps/zl"
        self.content=content
        self.headers = {
            'Accept-Encoding': 'gzip',
            'Cookie': 'client_type=android;app_id=161;login_mode=2;jxjpin=zhangyinping526;tgt=AAFbi2IAAECysQtKLoN02qXtqJphAzagnL2K88TlePeS4t53dNXfj9oY22Wjn4HpJ5V-Pj_BNzP7AD9fpdWn2gC-c17tKC1y;qwd_chn=99;qwd_schn=1'
        }

    def zhuan(self,url_content):

        url ="http://qwd.jd.com/cps/zl?shareSource=1_2_1&content="+url_content
        new_lian=requests.get(url,headers=self.headers)
        my_contetn=new_lian.json().get("content")
        return my_contetn

    def urlTransform(self):
        # print(self.content.text)
        url_content = quote(self.content.text, 'utf-8')
        return url_content

if __name__ == "__main__":
    test=ZhuanLian("抢券+下单：http://union-click.jd.com/jdc?d=IsODWY")
    n=test.urlTransform()
    print(test.zhuan(n))