import os
from yjyhrp.util.runner import yjytest

if __name__ == '__main__':
    set_env = 'DEV'
    os.environ['TEST_ENV'] = set_env
    runtest = yjytest(set_env, 'info')
    runtest.runtestcase(test_path='testsuites/渠道中心登录测试集.yml', report_title='渠道中心接口测试报告')
