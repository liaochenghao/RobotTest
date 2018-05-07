# coding: utf-8
import pymysql
import redis

from src.config.settings import db_config, REDIS_CONFIG


redis_valid_time = 1 * 60 * 60


def my_custom_sql(query, is_query=True):
    conn = pymysql.connect(**db_config)
    with conn.cursor() as cursor:
        cursor.execute(query)
        if is_query:
            data = cursor.fetchall()
        else:
            conn.commit()
            data = {'id': cursor.lastrowid}
    conn.close()
    return data


class RedisClient:

    @property
    def redis_client(self):
        client = redis.Redis(host=REDIS_CONFIG['host'], port=REDIS_CONFIG['port'])
        return client

    def get_instance(self, key, delete_cache=False):
        redis_instance = self.redis_client.get(key)
        if not redis_instance:
            return None
        try:
            res = eval(redis_instance)
        except:
            res = str(redis_instance, encoding='utf-8')
        if delete_cache:            # 默认获取redis数据之后立即删除数据
            self.redis_client.delete(key)
        return res

    def set_instance(self, key, value, default_valid_time=redis_valid_time):
        self.redis_client.set(key, value, default_valid_time)
        return

    def delete_instance(self, *key):
        self.redis_client.delete(*key)


redis_client = RedisClient()