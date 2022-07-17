import logging

logging.basicConfig(level=logging.DEBUG,
                    datefmt="%Y-%m-%d %H:%M:%S",
                    format="%(asctime)s | %(message)s")
logging.debug("这是一个debug格式的信息")
