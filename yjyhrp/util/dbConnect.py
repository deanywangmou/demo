import json
import os
import time

import pymysql
from dbutils.pooled_db import PooledDB

from yjyhrp.util.parserConf import ParserConf


class DB_CONN(object):
    def __init__(self, **kwargs):
        parse = ParserConf(os.environ['DATA_PATH'])
        database = kwargs.get('database', 'DATABASE')
        ip = parse.get_config_value_by_key(database, "ip")
        port = parse.get_config_value_by_key(database, "port")
        user = parse.get_config_value_by_key(database, "user")
        password = parse.get_config_value_by_key(database, "password")
        charset = parse.get_config_value_by_key(database, "charset")
        try:
            self.__pool = PooledDB(creator=pymysql,
                                   maxusage=None,
                                   maxconnections=10,
                                   mincached=5,
                                   maxcached=10,
                                   maxshared=10,
                                   blocking=True,
                                   host=ip,
                                   port=int(port),
                                   user=user,
                                   passwd=password,
                                   charset=charset)
        except Exception:
            print('数据库连接失败')

    def db_query_count(self, sql):
        conn = self.__pool.connection()
        cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
        try:
            cur.execute(sql)
            conn.commit()
            return cur
        except Exception as e:
            print('数据查询失败', e)
        finally:
            cur.close()
            conn.close()

    def db_Query_Json(self, sql):
        '''
        获取数据json格式游标，使用需要fetchall()或fetchone()fetchmany()
        :param sql: 查询语句
        :return: 游标json格式 使用时需要使用fetchall()或fetchone()fetchmaeeny()
        '''
        conn = self.__pool.connection()
        cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
        len = 0
        try:
            if len == 0:
                for i in range(5):
                    len = cur.execute(sql)
                    if len > 0:
                        conn.commit()
                        return cur
                    # time.sleep(1)
            return cur
        except Exception as e:
            print('数据查询失败', e)
        finally:
            cur.close()
            conn.close()
