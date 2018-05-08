# coding:utf-8
import requests

from utils.service import WeixinServer


def create_menu():
    menu = {
        "button": [
            {
                "name": "Daily!",
                "sub_button": [
                    {
                        "type": "view",
                        "name": "阅读往期",
                        "url": "https://mp.weixin.qq.com/mp/profile_ext?action=home&scene=114&__biz=MzA5NjUzNDM2Nw==#wechat_redirect"
                    },
                    {
                        "type": "view",
                        "name": "搜索文章",
                        "url": "http://data.newrank.cn/m/s.html?s=NzEvOi89PD89"
                    },
                    {
                        "type": "view",
                        "name": "纸条社区",
                        "url": "https://mp.weixin.qq.com/s/YzA_o-1eAS5I20wR2A_6vg"
                    },
                    {
                        "type": "view",
                        "name": "有事专栏",
                        "url": "http://mp.weixin.qq.com/s/8QfaqT1jhmGdYlv-yOBzNA"
                    }
                ]
            },
            {
                "name": "特色栏目",
                "sub_button": [
                    {
                        "type": "view",
                        "name": "历史上的留学生",
                        "url": "http://mp.weixin.qq.com/s?__biz=MzA5NjUzNDM2Nw==&mid=510525545&idx=1&sn=007cdc9b03f4506a16d0a48a9641040b&chksm=0b340a593c43834feab79b1a31e1b1fe0de726af659b847955b87ec9356e797db69aff64a0da#rd"
                    },
                    {
                        "type": "view",
                        "name": "求打CALL",
                        "url": "http://mp.weixin.qq.com/s?__biz=MzA5NjUzNDM2Nw==&mid=510525565&idx=1&sn=fe8de04dd98c73da59a15e2b3d01783b&chksm=0b340a4d3c43835b43a783da113e2cf2697421cffc9c4468d192a43dd9f37c7cf6d22a518e46#rd"
                    },
                    {
                        "type": "view",
                        "name": "小黄报告",
                        "url": "http://mp.weixin.qq.com/s?__biz=MzA5NjUzNDM2Nw==&mid=510525560&idx=1&sn=46f2682a4d281c002c06709d33131d93&chksm=0b340a483c43835ea04b1741b1e6d731e21829105aef52bc4e489c722991e3e3b61569d7b1be#rd"
                    },
                    {
                        "type": "view",
                        "name": "本月热文",
                        "url": "http://mp.weixin.qq.com/mp/homepage?__biz=MzA5NjUzNDM2Nw==&hid=3&sn=43f9e2980c26c2f10facb756fc266ca9&scene=18#wechat_redirect"
                    },
                ]
            },
            {
                "name": "联系我们",
                "sub_button": [
                    {
                        "type": "view",
                        "name": "合作转载",
                        "url": "http://mp.weixin.qq.com/s/wxJ8njULs_w2LUnaTX7wWQ"
                    },
                    {
                        "type": "click",
                        "name": "投稿爆料",
                        "key": "submission_001"
                    },
                    {
                        "type": "view",
                        "name": "修仙大作战",
                        "url": "https://open.weixin.qq.com/connect/oauth2/authorize?appid=wxddf82dc1f4c6b5e0&redirect_uri=http%3a%2f%2fsleep.lxhelper.com%2f&response_type=code&scope=snsapi_userinfo&state=STATE&wechat_redirect"
                    },
                ]
            }
        ]
    }
#     access_token = WeixinServer.get_access_token()
#     posturl = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=" + access_token
#     response = requests.post(posturl, data=menu)
#     print(response.content)
#
#
# create_menu()
