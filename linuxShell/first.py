import os
import sys
import autoShell

######### 控制台所有的信息都打印到文件当中 #########
class Logger(object):
    def __init__(self, filename='default.log', stream=sys.stdout):
        self.terminal = stream
        self.log = open(filename, 'w')

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass

# 将控制台的结果输出到a.log文件，可以改成a.txt
sys.stdout = Logger('serverInfo.log', sys.stdout)
# sys.stderr = Logger('a.log_file', sys.stderr)
autoShell.info()

