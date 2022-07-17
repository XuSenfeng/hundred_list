import logging

logger = logging.getLogger("aaa.asd")
logger.setLevel(logging.DEBUG)

# 处理器 可以设置多个
consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.WARNING)

formatter = logging.Formatter("%(asctime)s | %(message)s")
# 设置文字输出的格式
consoleHandler.setFormatter(formatter)
# 加入处理器
logger.addHandler(consoleHandler)

flt = logging.Filter("aaa")
logger.addFilter(flt)
logger.debug("debug")
logger.warning("warning")
