import os
from yjyhrp.util.runner import yjytest

if __name__ == '__main__':
    set_env = 'DEV'
    os.environ['TEST_ENV'] = set_env
    runtest = yjytest(set_env, 'info')
    runtest.runtestcase(test_path='testsuites/P端接口/API对接主要接口流程/通用api主流程测试集.yml', report_title='小前端P端api测试集报告')
    # runtest.runtestcase(test_path='testcases/P端接口/h5模块登录', report_title='小前端测试报告')
    # runtest.runtestcase(test_path='testcases/P端接口/API对接主要接口/用户兑换优惠券.yml', report_title='小前端测试报告')
    # runtest.runtestcase(test_path='testcases/P端接口/API对接主要接口', report_title='小前端测试报告')

