# coding=utf-8
from util.vlog import logger

if __name__ == "__main__":
    for i in range(20000):
        logger.info("第%s条数据" % i)