import logging

handlers = logging.FileHandler(filename="test.log", encoding="utf-8", mode="w")

logging.basicConfig(handlers=[handlers],
                    format="时间：%(asctime)s || 文件名：%(filename)s ||"
                           "行号：%(lineno)d|| 级别：%(levelname)s || 内容："
                           "%(message)s", datefmt="%Y-%m-%d", level=logging.DEBUG)

logging.debug("test")

