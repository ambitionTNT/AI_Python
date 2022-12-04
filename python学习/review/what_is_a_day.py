# python learing
# author:TNT
"""
判断指定的年份是不是闰年

:param year: 年份
:return: 闰年返回True平年返回False
"""
def is_leap_year(year):
    if year % 4 == 0 and year % 100  != 0 or year % 400 == 0:
        return True
    else:
        return False


def which_day(year,month,date):
    """
    计算传入的日期是这一年的第几天

    :param year: 年
    :param month: 月
    :param date: 日
    :return: 第几天
    """
    if year<0 or month <0 or date<0:
        print("日期输入错误")
        exit(0)

    if month>12 or date >31 or(is_leap_year(year) and month ==2 and date >30) \
            or (is_leap_year(year) == False and month == 2 and month <29):
        print("日期输入错误")
        exit(0)
    days_of_month=[
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ][is_leap_year(year)]
    total = 0
    for index in range(month -1):
        total += days_of_month[index]


    return total + date


if __name__ == '__main__':
    print(which_day(2022,9,17))
    print(which_day(2022,2,29))
    print(which_day(2020, 9, 170))
    print(which_day(2016, 3, 1))

