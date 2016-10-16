# coding: utf-8
from xml.etree import cElementTree as ET
import logging.handlers
import logging
import os
import sys

logfrom = os.path.join(sys.argv[0].split('/')[-1])


# 提供日志功能
class logger:
    # 先读取XML文件中的配置数据
    # 由于config.xml放置在与当前文件相同的目录下，因此通过 __file__ 来获取XML文件的目录，然后再拼接成绝对路径
    # 这里利用了lxml库来解析XML
    root = ET.parse(os.path.join(os.path.abspath("../common"), 'config.xml')).getroot()
    # 读取日志文件名称
    logname = root.find('logname').text
    # 日志保存的路径
    logfile = os.path.abspath('../%s' % logname)
    # 读取日志文件容量，转换为字节
    logsize = 1024 * 1024 * int(root.find('logsize').text)
    # 读取日志文件保存个数
    lognum = int(root.find('lognum').text)

    # 初始化logger
    log = logging.getLogger()
    # 日志格式，可以根据需要设置
    fmt = logging.Formatter('[%(levelname)s][%(asctime)s]%(message)s', '%Y-%m-%d %H:%M:%S')

    # 日志输出到文件，这里用到了上面获取的日志名称，大小，保存个数
    handle1 = logging.handlers.RotatingFileHandler(logfile, maxBytes=logsize, backupCount=lognum)
    handle1.setFormatter(fmt)
    # # 同时输出到屏幕，便于实时观察
    log.addHandler(handle1)

    # 设置日志基本，这里设置为INFO，表示只有INFO级别及以上的会打印
    log.setLevel(logging.INFO)

    # 日志接口，用户只需调用这里的接口即可，这里只定位了INFO, WARNING, ERROR三个级别的日志，可根据需要定义更多接口
    @classmethod
    def info(cls, msg):
        cls.log.info('[%s:%s]%s' % (logfrom, sys._getframe().f_back.f_lineno, msg))
        return

    @classmethod
    def warning(cls, msg):
        cls.log.warning('[%s:%s]%s' % (logfrom, sys._getframe().f_back.f_lineno, msg))
        return

    @classmethod
    def error(cls, msg):
        cls.log.error('[%s:%s]%s' % (logfrom, sys._getframe().f_back.f_lineno, msg))
