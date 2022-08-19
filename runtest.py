import os

from httprunner.api import HttpRunner
from httprunner.report import gen_html_report
from yjyhrp.util.runner import yjytest

if __name__ == '__main__':
    # runner = HttpRunner(log_level='info')
    #
    # # # 方式一：
    # # runner.run(path_or_tests='testsuites/渠道中心登录测试集.yml')
    # # gen_html_report(runner._summary)
    #
    # # # 方式二:
    # summary = runner.run(path_or_tests='testsuites/渠道中心/渠道商测试集.yml')
    # # summary = runner.run(path_or_tests='testcases/检查百度正则表达式.yml')
    # gen_html_report(summary)

    # 方式三:
    # gen_html_report(runner.run(path_or_tests='testsuites/渠道中心/渠道商测试集.yml'))

    # runner.run(path_or_tests='data/save_qudao.json')
    # gen_html_report(runner._summary)

    set_env = 'DEV'
    os.environ['TEST_ENV'] = set_env
    runtest = yjytest(set_env, 'info')
    runtest.runtestcase(test_path='testsuites/渠道中心登录测试集.yml', report_title='渠道中心接口测试报告')
    # runtest.runtestcase(test_path='api/百度正则表达式演示.yml', report_title='渠道中心接口测试报告')
