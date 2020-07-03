import time

class StopWatch():
    def __init__(self):
        self.__starttime = 0.0
        self.__timespan = 0.0

    def start(self):
        self.__starttime = time.time()

    def stop(self):
        self.__timespan = time.time() - self.__starttime

    def getspan(self):
        return self.__timespan

sw1 = StopWatch()
sw1.start()
time.sleep(1.0) # 計測対象の処理
sw1.stop()
print('経過時間 : ',sw1.getspan(),'[s]')
