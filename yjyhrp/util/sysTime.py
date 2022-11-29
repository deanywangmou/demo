import time
import datetime


class RunTime:

    # 时间模块
    def getTime(self, strFormat):
        # 按照格式获取时间
        nowTime = time.localtime()
        strFormatTime = time.strftime(strFormat, nowTime)
        return strFormatTime

    def getDateTime(self):
        return self.getTime("%Y-%m-%d %H:%M:%S")

    def getDate(self):
        return self.getTime("%Y-%m-%d")

    def getNumSecondTime(self):
        return self.getTime("%Y%m%d%H%M%S")

    def getNumHourTime(self):
        return self.getTime("%Y%m%d%H")

    def getNumDayTime(self):
        return self.getTime("%Y%m%d")

    def getPastDataDay(self, intDayNum):
        # 根据天数，来获取过去距离今天intDayNum天的日期
        # intDayNum: int类型, 表示天数
        # 返回的是一个date对象类型的日期,格式是"%Y-%m-%d"
        strToday = datetime.date.today()
        # strToday的日期格式就是"%Y-%m-%d"
        strOtherday = strToday - datetime.timedelta(days=intDayNum)
        return strOtherday

    def getFutureDataDay(self, intDayNum):
        # 根据天数，来获取未来距离今天intDayNum天的日期
        # intDayNum: int类型, 表示天数
        # 返回的是一个date对象类型的日期,格式是"%Y-%m-%d"
        strToday = datetime.date.today()
        # strToday的日期格式就是"%Y-%m-%d"
        strOtherday = strToday + datetime.timedelta(days=intDayNum)
        return strOtherday

    def getAfterTime(self, intHourNum):
        now_time = datetime.datetime.now()
        return (now_time + datetime.timedelta(hours=intHourNum)).strftime("%Y-%m-%d %H:%M:%S")

    def getAfterMinutes(self, intMinutes):
        now_time = datetime.datetime.now()
        return (now_time + datetime.timedelta(minutes=intMinutes)).strftime("%Y-%m-%d %H:%M:%S")

    def getFutureDayToFuture(self, futureTime, intDayNum):
        timeStamp = self.getTimeStamp(futureTime, '%Y-%m-%d %H:%M:%S')
        futuredata = datetime.date.fromtimestamp(timeStamp)
        future = futuredata + datetime.timedelta(days=intDayNum)
        return future

    def getFutureDayToDate(self, futureTime, intDayNum):
        timeStamp = self.getTimeStamp(futureTime, '%Y-%m-%d')
        futuredata = datetime.date.fromtimestamp(timeStamp)
        future = futuredata + datetime.timedelta(days=intDayNum)
        return future

    def getTimeStamp(self, strDate, strFormatDate):
        # 根据日期，获取时间戳
        # strDate: 字符串类型的日期
        # strFormatDate: 与strDate先对应的日期格式，例如"%Y-%m-%d"
        # 返回一个int类型的时间戳
        timeArray = time.strptime(strDate, strFormatDate)
        timeStamp = time.mktime(timeArray)
        return int(timeStamp)

    def getTodayStamp(self):
        # 获取今天的时间戳
        # 返回的是一个int类型的时间戳,日期格式是"%Y-%m-%d"
        strToday = datetime.date.today()
        timeArray = time.strptime(str(strToday), "%Y-%m-%d")
        timeStamp = time.mktime(timeArray)
        return int(timeStamp)

    def getToDateTime(self, timestamp, strFormatDate):
        from datetime import datetime
        return datetime.fromtimestamp(timestamp).strftime(strFormatDate)



if __name__ == '__main__':
    run = RunTime()
