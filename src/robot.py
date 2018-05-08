# coding:utf-8
import logging

from werobot import WeRoBot
from werobot.replies import SuccessReply

from src.common.operate_menu import create_menu
from src.config.settings import APP_ID, APP_SECRET
from src.functions import handle_text_message, handle_image_message, subscribe_message_func

config = dict(
    TOKEN='robottest123456',
    SERVER="gunicorn",
    HOST="0.0.0.0",
    PORT="8888",
    SESSION_STORAGE=False,
    APP_ID=APP_ID,
    APP_SECRET=APP_SECRET,
    ENCODING_AES_KEY=None
)
robot = WeRoBot(config=config)


@robot.text
def text_message(message):
    text = handle_text_message(message)
    return text


@robot.subscribe
def subscribe_message(message):
    text = subscribe_message_func(message)
    return text


@robot.image
def image_message(message):
    handle_image_message(message)
    return SuccessReply(message)


@robot.unsubscribe
def unsubscribe_message(message):
    return SuccessReply(message)


@robot.scan
def scan_message(message):
    return


@robot.handler
def common_replay(message):
    return SuccessReply(message)


@robot.click
def submission_001(message):
    text = """我们希望建立渠道了解大家的身边事，推送更多与大家息息相关的新闻。

无论是你的学校、你的圈子发生了什么大事，还是你有什么灵光一现的想法、有什么无法排解的感情，都欢迎向我们「爆料或投稿」。

你可以在后台直接留言，我们会在后台及时关注和回复，也可以发送邮件到：tui@lxhelper.com！ 
"""
    return text
