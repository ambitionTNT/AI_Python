# python learing
# author:TNT
from time import time, localtime, sleep
class Clock(object):
    """数字时钟"""
    def __init__(self,hour = 0,minute = 0,second = 0):
        self._hour = hour
        self._minute = minute
        self._second = second

    '''，类方法的第一个参数约定名为cls，它代表的是当前类相关的信息的对象（类本身也是一个对象，
        有的地方也称之为类的元数据对象），通过这个参数我们可以获取和类相关的信息并且可以创建出类的对象
        类方法对类属性进行的处理是有记忆性的。
        
        需要注意的是，类方法处理的变量一定要是类变量。
        因为在类方法里你用不了self来寻址实例变量，所以需要把类变量放到最前面描述，
        如上面的"id=0"所示。类变量是可以被self访问的，所以，在类变量定义好了以后，
        不需要在_init_函数里对类变量再一次描述。所以，上面代码里self.id不一定需要。'''

    @classmethod
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)
    def run(self):
        """走字"""
        self._second += 1
        if self._second ==60 :
            self._minute += 1
            self._second = 0
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
    def show(self):
        return '%02d:%02d:%02d'%(self._hour,self._minute,self._second)

def main():
    #通过类方法创建对象并获取系统时间
    clock = Clock.now()
    while True:
        print(clock.show())
        sleep(1)
        clock.run()
if __name__ == '__main__':
    main()
