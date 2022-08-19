import os

from yjyhrp.util.dbConnect import DB_CONN
from yjyhrp.util.parserConf import ParserConf


def filterDatabaseSession(tableName):
    parse = ParserConf(os.environ['DATA_PATH'])
    allSession = parse.get_all_sections_from_config_file()
    session = 'DATABASE'
    db = None
    table = None
    tableinfo = {}
    for data in allSession:
        db_tables = parse.get_config_value_by_key(data, 'db_tables')
        isStop = False
        if db_tables:
            db_tablesList = db_tables.split(',')
            for db_table in db_tablesList:
                db = db_table.split(':')[0].strip()
                table = db_table.split(':')[1].strip()
                if tableName.strip() == table:
                    isStop = True
                    session = data
                    break
            if isStop:
                break
    ip = parse.get_config_value_by_key(session, "ip")
    port = parse.get_config_value_by_key(session, "port")
    user = parse.get_config_value_by_key(session, "user")
    password = parse.get_config_value_by_key(session, "password")
    charset = parse.get_config_value_by_key(session, "charset")
    tableinfo['ip'] = ip
    tableinfo['port'] = port
    tableinfo['user'] = user
    tableinfo['password'] = password
    tableinfo['charset'] = charset
    tableinfo['table'] = table
    tableinfo['db'] = db
    return tableinfo


def getTableName(sql):
    lowersql = str(sql).lower()
    tablename = None
    if lowersql.startswith('select', 0) or lowersql.startswith('delete', 0):
        indexfrom = lowersql.index('from ')
        try:
            sqltext = lowersql[indexfrom + 5:].strip()
            indextable = sqltext.index(" ")
            tablename = sqltext[0:indextable]
        except Exception:
            tablename = sql[indexfrom + 5:]
        tablename = tablename.replace(';', '')
        if '.' in tablename:
            dbtablename = tablename.split('.')
            tablename = dbtablename[1]
    return tablename


def query_count(sql):
    if sql:
        db = DB_CONN()
        cur = db.db_query_count(sql)
        return cur
    else:
        print('没有匹配到相应的数据库信息，请在配置文件中配置相应数据库信息')


def executeSql(sql, **kwargs):
    if sql:
        db = DB_CONN(**kwargs)
        cur = db.db_Query_Json(sql)
        return cur
    else:
        print('没有匹配到相应的数据库信息，请在配置文件中配置相应数据库信息')


def selectRowCount(sql):
    print('执行SQL语句为：', sql)
    cur = query_count(sql)
    if cur:
        count = cur.rowcount
        print('查询到的记录数为: {}'.format(count))
        return count


def selectSqlJson(sql):
    print('执行SQL语句为：', sql)
    cur = executeSql(sql)
    if cur:
        sqldata = cur.fetchone()
        print('查询到的数据记录为：{}'.format(sqldata))
        return sqldata


def selectSqlOneData(sql, *args, **kwargs):
    print('执行SQL语句为：', sql)
    cur = executeSql(sql, **kwargs)
    keyvalue = ''
    if cur:
        sqlData = cur.fetchone()
        if sqlData:
            for key in args:
                value = str(sqlData.get(key, ''))
                keyvalue += value + ','
                print('查询到{}字段的值为：{}'.format(key, value))
            return keyvalue[0:-1]
        else:
            print('没有查询到数据记录')
            return ''


if __name__ == '__main__':
    selectSqlOneData()
