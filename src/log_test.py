# coding=utf-8
from util.vlog import logger
import traceback

if __name__ == "__main__":
    for i in range(2000):
        logger.info("第%s条正确数据" % i)
        logger.error("第%s条错误数据" % i)
        logger.warning("第%s条警告数据" % i)
        try:
            a=1/0
        except:
            logger.error(traceback.format_exc())