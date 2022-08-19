import os
from configparser import ConfigParser


class ParserConf():
    def __init__(self, filename):
        self.conf = ConfigParser(allow_no_value=True, delimiters='=')
        self.confile = os.path.join(os.getcwd(), filename)
        if os.path.exists(self.confile):
            self.conf.read(self.confile, encoding='utf-8')
        else:
            print('不存在' + filename + '文件')

    def get_config_value_by_key(self, section, key):
        # self.conf.read(self.confile, encoding='utf-8')
        # 获取指定的section， 指定的option的值
        if self.conf.has_option(section, key):
            return self.conf.get(section, key)
        # print('获取%s 节点，%s 的值为 %s' % (section, key, key_value))

    # 获取所有的section
    def get_all_sections_from_config_file(self):
        # self.conf.read(self.confile, encoding='utf-8')
        sections = self.conf.sections()
        return sections

    # 更新指定section, option的值
    def update_value_by_section_and_key(
            self, section_name, key, key_value):
        # self.conf.read(self.confile, encoding='utf-8')
        self.conf.set(section_name, key, key_value)
        self.conf.write(open(self.confile, 'w'))

    def get_section_value(self, section):
        # self.conf.read(self.confile, encoding='utf-8')
        value = self.conf.items(section)
        return value


if __name__ == '__main__':
    pass
