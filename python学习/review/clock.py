# python learing
# author:TNT
from time import sleep

class Clock(object):
    """数字时钟"""
    def __init__(self,hour = 0,minute = 0,second = 0):
        """初始化方法

        :param hour: 时
        :param minute: 分
        :param second: 秒
        """

        self._hour = hour
        self._minute = minute
        self._second = second\

    def run(self):
        """走字"""
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute ==60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show_time(self):
        """显示时间"""
        return '%02d:%02d:%02d' % \
               (self._hour,self._minute,self._second)
def main():
    clock = Clock(20,20,20)
    while True:
        clock.run()
        sleep(1)
        print(clock.show_time())
if __name__ == '__main__':
    main()


