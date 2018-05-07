# coding:utf-8
import pymysql

# 北美留学生微信公众号app_id, app_secret
APP_ID = 'wx5ac997cbc0ebe57b'
APP_SECRET = '44c699343b2f41c0b1b069e01411465d'

db_config = {
    'host': '42.51.8.152',
    'port': 3306,
    'db': 'stu_system',
    'user': 'root',
    'password': '1q2w3e4r!Q',
    'cursorclass': pymysql.cursors.DictCursor,
    'charset': 'utf8'
}

# REDIS_CONFIG = {
#     'host': '47.92.115.126',
#     'port': 6379,
#     'password': '1q2w3e4r!'
# }

micro_service_domain = 'http://47.92.115.126:7071'
