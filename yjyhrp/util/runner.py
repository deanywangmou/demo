import os

from httprunner.api import HttpRunner
from httprunner.report import gen_html_report

from yjyhrp.util.load import load_dot_env_file
from yjyhrp.util.sysTime import RunTime


class yjytest:
    def __init__(self, envir, log_level='INFO'):
        self.summary = ''
        self.envir = envir
        self.loadEnv(self.envir)
        self.log_level = log_level.upper()
        self.reportName = ''

    def loadEnv(self, envir):
        TEST_ENV = os.environ.get('TEST_ENV', envir)
        PATH = 'env' + os.sep + TEST_ENV
        dirname = os.getcwd()
        os.environ['ENV_PATH'] = os.path.join(dirname, PATH, 'host.env')
        os.environ["DATA_PATH"] = os.path.join(dirname, PATH, 'database.ini')
        os.environ['REDIS_PATH'] = os.path.join(dirname, PATH, 'redis.ini')
        envpath = os.environ['ENV_PATH']
        load_dot_env_file(envpath)

    def runtestcase(self, test_path=None, report_title=None, **kwargs):
        templatePath = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "templates",
            "report_template.html"
        )
        try:
            runner = HttpRunner(failfast=False, log_level=self.log_level,
                                log_file=None)  # report_template=templatePath)
            runner.run(test_path)
            runner._summary['html_report_name'] = report_title
            gen_html_report(runner._summary, report_template=templatePath)
            # 修改原生框架生成的报告名
            start_datetime = runner._summary["time"]["start_datetime"]
            start_at_timestamp = str(runner._summary["time"]["start_at"]).split('.')[0]
            report_file_name = "{}.html".format(start_datetime.replace(":", "").replace("-", ""))
            report_dir = os.path.join(os.getcwd(), "reports")
            reporttime = RunTime().getToDateTime(int(start_at_timestamp), "%Y-%m-%d_%H_%M_%S")
            report_file = os.path.join(report_dir, report_file_name)

            if os.path.exists(report_file):
                reportpath = os.path.join(report_dir, report_title + "{}.html".format(str(reporttime)))
                os.rename(report_file, reportpath)
            self.summary = runner._summary
            args = kwargs.get('args')
        finally:
            pass
        return self.summary


if __name__ == '__main__':
    yjytest('DEV').loadEnv()
