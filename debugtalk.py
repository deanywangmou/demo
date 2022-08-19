import os
import time
from decimal import Decimal
from urllib import parse

import yaml
import random
from faker import Faker

from yjyhrp.util import operateDatabase


def sleep(n_secs):
    time.sleep(n_secs)


def yaml_read(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        print(data)


data1 = {
    "data1": 123,
    "data2": {
        "k1": "v1",
        "k2": [4, 5, 6]
    }
}


def yaml_write(path):
    with open(path, 'w', encoding='utf-8') as f:
        yaml.dump(data1, f)


# 生成随机0到num的随机数字
def get_random_int(start, end):
    return random.randint(start, end)


def setup_case():
    print("测试用例----开始执行")


def teardown_case():
    print("测试用例----结束执行")
    time.sleep(2)


def createSSN():
    '''
    随机生成身份证号
    :return:
    '''
    fake = Faker(locale='zh_CN')
    return fake.ssn()


def createphone_number():
    '''
    随机生成电话号码
    :return:
    '''
    fake = Faker(locale='zh_CN')
    return fake.phone_number()


def createName():
    '''
    随机生成一个姓名
    :return:
    '''
    fake = Faker(locale='zh_CN')
    return fake.name()


def createAddress():
    '''
    随机生成一个地址
    :return:
    '''
    fake = Faker(locale='zh_CN')
    return fake.address()


def createEmail():
    '''
    随机生成一个邮箱
    :return:
    '''
    fake = Faker(locale='zh_CN')
    return fake.email()


def createSentence():
    '''
    随机生成一句话
    :return:
    '''
    fake = Faker(locale='zh_CN')
    return fake.sentence()


def createCredit_card_number():
    '''
    随机生成一个信号卡号
    :return:
    '''
    fake = Faker(locale='zh_CN')
    return fake.credit_card_number()


# 读取文件内容
def get_file(filePath):
    return open(filePath, "rb")


def sum_status_code(status_code, expect_code):
    sum_value = 0
    for key in str(status_code):
        sum_value += int(key)
    assert sum_value == expect_code


def has_token(var):
    if var:
        return True
    return False


# 金额精度转化
def awardSwap(value):
    return str(Decimal(value).quantize(Decimal('0.0')))


# 将字符转换成url
def strSwapUrl(keyword):
    quote = parse.quote(keyword, safe='')
    return quote


# 将url转换成字符
def urlSwapStr(keyword):
    unquote = parse.unquote(keyword)
    return unquote


def selectSqlRowCount(sql):
    '''
    返回查询到的记录数
    :param sql: sql语句
    :return:
    '''
    return operateDatabase.selectRowCount(sql)


def selectSqlOneData(sql, *args):
    '''
    返回一条记录中指定的字段值
    :param sql: sql语句
    :param key: 指定的字段
    :return:
    '''
    return operateDatabase.selectSqlOneData(sql, *args)


def selectSqlRowCount(sql):
    '''
    返回查询到的记录数
    :param sql: sql语句
    :return:
    '''
    return operateDatabase.selectRowCount(sql)


def updateSql(sql, *args, **kwargs):
    '''
    返回查询到的记录数
    :param sql: sql语句
    :return:
    '''
    print("开始执行update语句为:", sql)
    curson = operateDatabase.executeSql(sql, *args, **kwargs)
    if curson:
        print('update语句执行完成')
    else:
        print('update语句执行失败')


if __name__ == '__main__':
    # yaml_read('api/渠道中心登录测试集.yml')
    # yaml_write('testcases/yaml文件写入.yml')
    # print(createAddress())
    # print(strSwapUrl('http://www.baidu.com'))
    # print(urlSwapStr('http%3A%2F%2Fwww.baidu.com'))

    os.environ['DATA_PATH'] = './env/DEV/database.ini'
    sql = "SELECT use_order_id  from  yijiayou_rds2.user_merchandise WHERE use_order_id=9110000020155839"
    selectSqlOneData(sql, 'use_order_id')
