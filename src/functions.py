# coding: utf-8
import json
import logging

import datetime
from utils.service import BaseHttpServer
import requests

from utils.service import WeixinServer

logger = logging.getLogger('info')


def call_func(access_token, openid):
    articles = [
        {
            "title": "求打CALL | 北美留学生专栏",
            "description": "你好无聊哦，我看着看着就想睡。",
            "url": "http://mp.weixin.qq.com/s?__biz=MzA5NjUzNDM2Nw==&mid=510525565&idx=1&sn=fe8de04dd98c73da59a15e2b3d01783b&chksm=0b340a4d3c43835b43a783da113e2cf2697421cffc9c4468d192a43dd9f37c7cf6d22a518e46#rd",
            "picurl": "http://apply.chinasummer.org/media/auto_reply/call.png"
        }
    ]
    WeixinServer.img_content_send(access_token=access_token, openid=openid, articles=articles)
    return


def baogao_func(access_token, openid):
    articles = [
        {
            "title": "小黄报告 | 北美留学生专栏",
            "description": "用数据看北美",
            "url": "http://mp.weixin.qq.com/s?__biz=MzA5NjUzNDM2Nw==&mid=510525560&idx=1&sn=46f2682a4d281c002c06709d33131d93&chksm=0b340a483c43835ea04b1741b1e6d731e21829105aef52bc4e489c722991e3e3b61569d7b1be#rd",
            "picurl": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1525868855814&di=8a35702fa0a57de2dd064aa9e8a6bb13&imgtype=0&src=http%3A%2F%2Fimg761.ph.126.net%2F_h_u6CHDuDYn6XCLO3PnsA%3D%3D%2F4805903752357751721.jpg"
        }
    ]
    WeixinServer.img_content_send(access_token=access_token, openid=openid, articles=articles)
    return


def cp_func(access_token, openid):
    articles = [
        {
            "title": "小哥哥网恋吗？48小时CP活动报名中",
            "description": "我铁观音",
            "url": "https://mp.weixin.qq.com/s?__biz=MzI0NTA2OTAxNg==&mid=2649178385&idx=1&sn=282b163e4538993ee5196a49edd40ea4&chksm=f147c4a6c6304db05ab00c8742afa1fa7eee1a8402fd7584ed222d171639092f25e09c35b114#rd",
            "picurl": "https://cp1.lxhelper.com/media/auto_reply/north_american.jpg"
        }
    ]
    WeixinServer.img_content_send(access_token=access_token, openid=openid, articles=articles)
    return


def secret_weapon_func(access_token, openid):
    articles = [
        {
            "title": "北美留学生情人节彩蛋",
            "description": "拜个早年！",
            "url": "http://mp.weixin.qq.com/s?__biz=MzA5NjUzNDM2Nw==&mid=510526931&idx=1&sn=3216e8680b2682387291d5ada8cabc51&chksm=0b340fe33c4386f5e17bd477ef99c65e27ba7c852997543a045fed9d64a0f8adb8b5a3c48dfe#rd",
            "picurl": "http://apply.chinasummer.org/media/auto_reply/secret_weapon.png"
        }
    ]
    WeixinServer.img_content_send(access_token=access_token, openid=openid, articles=articles)
    return


def emoji_func(access_token, openid):
    articles = [
        {
            "title": "北美留学生EMOJI答案",
            "description": "我就知道你肯定没找去全",
            "url": "http://mp.weixin.qq.com/s?__biz=MzA5NjUzNDM2Nw==&mid=510526672&idx=1&sn=52ba27f1d97637048fbd7cf4f16f0e81&chksm=0b340ee03c4387f6ab30a34af32f70bb41d0db98a717e0a47916cca442c6666f30697186aa21#rd",
            "picurl": "http://apply.chinasummer.org/media/auto_reply/emoji.png"
        }
    ]
    WeixinServer.img_content_send(access_token=access_token, openid=openid, articles=articles)
    return


def history_func(access_token, openid):
    articles = [
        {
            "title": "历史上的留学生 | 北美留学生专栏",
            "description": "我心匪石，不可转也。",
            "url": "http://mp.weixin.qq.com/s?__biz=MzA5NjUzNDM2Nw==&mid=510525545&idx=1&sn=007cdc9b03f4506a16d0a48a9641040b&chksm=0b340a593c43834feab79b1a31e1b1fe0de726af659b847955b87ec9356e797db69aff64a0da#rd",
            "picurl": "http://apply.chinasummer.org/media/auto_reply/history.png"
        }
    ]
    WeixinServer.img_content_send(access_token=access_token, openid=openid, articles=articles)
    return


def handle_text_message(message):
    content = message.content
    openid = message.source

    if content in ['报告', '小黄', '小黄报告']:
        access_token = WeixinServer.get_access_token()
        baogao_func(access_token=access_token, openid=openid)
    # if content in ['历史', '历史上的留学生']:
    #     access_token = WeixinServer.get_access_token()
    #     history_func(access_token=access_token, openid=openid)
    #
    # if content in ['求打CALL', '求打call', '打CALL', '打call']:
    #     access_token = WeixinServer.get_access_token()
    #     call_func(access_token=access_token, openid=openid)
    #     return """哈哈哈，你来啦！
    # 请点击下方蓝字投稿
    # <a href="https://www.wenjuan.in/s/6nuIfm/">给北美留学生一个为你疯狂打call的机会</a>"""
    #
    # if content in ['秘密武器']:
    #     access_token = WeixinServer.get_access_token()
    #     secret_weapon_func(access_token=access_token, openid=openid)
    #
    # if content in ['emoji']:
    #     access_token = WeixinServer.get_access_token()
    #     emoji_func(access_token=access_token, openid=openid)
    #
    # if content in ['离家']:
    #     return """请输入你离开家的年月日哦，如：2017年8月30日即为20170830。"""
    #
    # if content == '名企':
    #     access_token = WeixinServer.get_access_token()
    #     picture_url = '/root/project/NorthAmericaStuWeixinRobot/media/mingqi_code.jpg'
    #     WeixinServer.upload_medias('image', picture_url, openid, access_token)
    #     return """欢迎加入留学生Offer群！请扫描下方二维码，进入公众号【留学生求职报】，回复【名企】，即可参与活动哦！"""

    # CP活动馆用户输入邀请码事件
    # if len(content) == 5 or len(content) == 6:
    #     try:
    #         access_token = WeixinServer.get_access_token()
    #         user_info = WeixinServer.get_base_user_info(openid=openid, access_token=access_token)
    #         code = int(content)
    #         resp = requests.get('https://cp1.lxhelper.com/api/v1/invitation/code/',
    #                             {'code': code, 'other_open_id': openid, 'nickname': user_info.get('nickname'),
    #                              'type': 2}, verify=False)
    #         data = json.loads(resp.content)
    #         if data['code'] != 0:
    #             return data['msg']
    #         else:
    #             return "因为你的助力，TA又可以解锁一枚男/女神啦。回复「CP」，一起参与该活动，解锁你的小哥哥和小姐姐吧。"
    #     except Exception as e:
    #         print('Exception')
    #         print(e)

    # CP活动馆通过优惠券码添加new币
    # if str(content).find('福利') != -1 and len(content) > 2:
    #     coupon = str(content)[2:]
    #     try:
    #         access_token = WeixinServer.get_access_token()
    #         user_info = WeixinServer.get_base_user_info(openid=openid, access_token=access_token)
    #         resp = requests.get('https://cp1.lxhelper.com/api/v1/activity/corn/',
    #                             {'coupon': coupon, 'other_open_id': openid, 'nickname': user_info.get('nickname')},
    #                             verify=False)
    #         data = json.loads(resp.content)
    #         if data['code'] != 0:
    #             return data['msg']
    #         else:
    #             return "优惠码使用成功"
    #     except Exception as e:
    #         print('Exception')
    #         print(e)

    # if content == 'CP':
    #     access_token = WeixinServer.get_access_token()
    #     cp_func(access_token=access_token, openid=openid)

#     if content == '睡眠报告':
#         access_token = WeixinServer.get_access_token()
#         user_info = WeixinServer.get_base_user_info(openid=openid, access_token=access_token)
#         union_id = user_info.get('unionid')
#         text = """<a href="http://sleep.lxhelper.com/#/stu_statistical?union_id=%s">我的睡眠报告</a>""" % union_id
#         return text
#
#     if content in ['测试', '睡眠', '修仙', '报告']:
#         text = """您回复的关键词有误。
# 回复【修仙大作战】，测测你长期修仙原因？你的入睡时间在北美留学生中是早还是晚？
# 回复【睡眠报告】，即可获取你的测试结果。"""
#         return text
#
#     if content in ['睡眠测试', '修仙大作战']:
#         text = """https://open.weixin.qq.com/connect/oauth2/authorize?appid=wxddf82dc1f4c6b5e0&redirect_uri=http%3a%2f%2fsleep.lxhelper.com%2f&response_type=code&scope=snsapi_userinfo&state=STATE&wechat_redirect"""
#         return '<a href="%s">修仙大作战</a>'%text

    if content == '好友六位码':
        text = '抱歉，你输入的格式不正确。请具体输入你的好友领福利时的专用六位数字码，如628083，来帮助Ta完成身份真实性验证，通过验证后即可免费领卡。'
        return text

    if content == '福利':
        media_file = r'/root/project/RobotTest/media/fuli.jpg'
        media_type = 'image'
        access_token = WeixinServer.get_access_token()
        res = WeixinServer.upload_medias(media_type, media_file, openid, access_token)
        print(res)
        # return res

    if str(content).isdigit() and len(content) >= 5:
        try:
            access_token = WeixinServer.get_access_token()
            user_info = WeixinServer.get_base_user_info(openid=openid, access_token=access_token)
            logger.info(user_info)
            resp = requests.get('https://welfare.lxhelper.com/api/v1/record/invitation/',
                                {'invite_code': str(content), 'unionid': user_info.get('unionid'),
                                 'invitee_nickname': user_info.get('nickname'),
                                 'invitee_avatar_url': user_info.get('headimgurl')},
                                verify=False)
            data = json.loads(resp.content)
            return data['msg'] if data['code'] != 0 else data['data']
        except Exception as e:
            print('X' * 70)
            print(e)
            print('X' * 70)
    return


def handle_image_message(message):
    return


def subscribe_message_func(message):
#     text = """你终于赶来，我大喜过望。
#
# 欢迎来到北美留学生的聚集地，关注我们自己的话题。
#
# 回复【修仙大作战】，测测你长期修仙原因？你的入睡时间在北美留学生中是早还是晚？"""

    text = """你终于赶来，我大喜过望。

欢迎来到北美留学生的聚集地，北美第一网黄@君君将和你一起关注我们留学生自己的话题。

当前我们正在免费发放「北美留学生2018全新电话卡福利」，凡留学美国或加拿大的小伙伴均可领取，人在中国即可提前免费快捷领卡，出国落地后可以立即向家人朋友报平安，首月免费使用，同时赠送更多话费供后续使用。

回复【福利】，立即进入小程序参与领取；回复【好友六位码】，立即帮助好友进行身份真实性核查。
    """
    return text
