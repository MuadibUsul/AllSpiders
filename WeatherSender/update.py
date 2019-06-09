import calendar
import datetime


class Update:
    def __init__(self, year, month, day):
        """
        :param year:
        :param month:
        :param day:
        """
        self.date = datetime.datetime.now()
        self.year = year
        self.month = month
        self.day = day
        self.month_list = {
            1: 31,
            2: 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31
        }

    def year_property(self):
        """
        判断是否是闰年如果是返回True
        如果是平年返回False
        :return:
        """
        return calendar.isleap(self.date.year)

    def month_property(self):
        """
        获取当前年的性质（闰年或者平年）
        计算出当前月数的天数并返回
        :return:
        """
        if self.year_property():
            self.month_list[2] = 29
        return self.month_list[self.date.month]

    def update(self):
        """
        更新天数、月数、年数
        :return:
        """
        if self.day == self.month_property() + 1:
            self.day = 1
            if self.month == 12 + 1:
                self.month = 1
                self.year += 1
            else:
                self.month += 1
        else:
            self.day += 1
        return self.year, self.month, self.day


