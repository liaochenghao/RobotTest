# coding: utf-8
import requests
from src.config.settings import APP_ID, APP_SECRET


class BaseHttpServer:
    @staticmethod
    def get(url, params):
        res = requests.get(url=url, params=params)
        return res.json()['data']

    @staticmethod
    def post(url, json_data):
        res = requests.post(url=url, json=json_data)
        return res.json()['data']


class WeixinServer:
    """微信公众号服务"""

    @staticmethod
    def get_access_token():
        """获取access_token"""
        url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s" \
              % (APP_ID, APP_SECRET)
        params = {'app_id': APP_ID, 'app_secret': APP_SECRET}
        data = BaseHttpServer.get(url, params)
        return data['access_token']

    # @staticmethod
    # def send_text_message(openid, content):
    #     """发送文本消息"""
    #     json_data = {
    #         'openid': openid,
    #         'content': content
    #     }
    #     url = "%s/api/weixin/service_center/send_text_message/" % micro_service_domain
    #     data = BaseHttpServer.post(url, json_data)
    #     return data
    #
    # @staticmethod
    # def send_template_message(openid, template_id, url, send_data):
    #     """发送模板消息"""
    #     json_data = {
    #         'openid': openid,
    #         'template_id': template_id,
    #         'url': url,
    #         'send_data': send_data
    #     }
    #     url = "%s/api/weixin/service_center/send_template_message/" % micro_service_domain
    #     data = BaseHttpServer.post(url, json_data)
    #     return data

    # @staticmethod
    # def code_authorize(code):
    #     """通过code获取网页授权"""
    #     url = "%s/api/weixin/service_center/code_authorize/" % micro_service_domain
    #     params = {'code': code}
    #     data = BaseHttpServer.get(url, params)
    #     return data

    # @staticmethod
    # def get_web_user_info(openid, access_token):
    #     """获取网页授权用户信息"""
    #     url = "%s/api/weixin/service_center/get_web_user_info/" % micro_service_domain
    #     data = BaseHttpServer.get(url, {'openid': openid, 'access_token': access_token})
    #     return data
    #
    # @staticmethod
    # def get_base_user_info(openid, access_token):
    #     """获取基础的用户信息(非网页授权)"""
    #     url = "%s/api/weixin/service_center/get_user_info/" % micro_service_domain
    #     data = BaseHttpServer.get(url, {'openid': openid, 'access_token': access_token})
    #     return data
    #
    # @staticmethod
    # def get_temporary_qr_code(action_name, scene_id, expired_time=7 * 24 * 60 * 60):
    #     """获取临时二维码"""
    #     url = "%s/api/weixin/service_center/temporary_qr_code/" % micro_service_domain
    #     json_data = {
    #         "action_name": action_name,
    #         "scene_id": scene_id,
    #         "expired_time": expired_time
    #     }
    #     data = BaseHttpServer.post(url, json_data)
    #     return data['qr_img_url']
    #
    # @staticmethod
    # def get_forever_qr_code(action_name, scene_id):
    #     """获取永久二维码"""
    #     url = "%s/api/weixin/service_center/forever_qr_code/" % micro_service_domain
    #     json_data = {
    #         "action_name": action_name,
    #         "scene_id": scene_id,
    #     }
    #     data = BaseHttpServer.post(url, json_data)
    #     return data['qr_img_url']
    #
    # @staticmethod
    # def img_content_send(access_token, openid, articles):
    #     url = "%s/api/weixin/service_center/send_img_content_message/" % micro_service_domain
    #     data = {
    #         "access_token": access_token,
    #         "openid": openid,
    #         "articles": articles
    #     }
    #     data = BaseHttpServer.post(url, json_data=data)
    #     return data
    #
    # @staticmethod
    def upload_medias(media_type, media_file, openid, access_token):
        """上传图片"""
        with open(media_file, "rb") as upload_media_file:
            # url = "https://api.weixin.qq.com/cgi-bin/media/upload?access_token=%s&type=%s" % (access_token, media_type)
            # res = requests.post(url, files={"media": upload_media_file})
            # print(res.content)
            # print(res.text)
            url = 'https://api.weixin.qq.com/cgi-bin/message/custom/send?access_token=%s' % access_token
            data = {
                "touser": openid,
                "msgtype": "image",
                "image": {
                    "media_id": 'noK49V6hsstPONhEuW-rFlq_6xNHdSQQk-qALOdin76PmMO3HED6kgqmVSGlKHGf'
                }
            }
            res = requests.post(url=url, json=data)
            return res.json()
