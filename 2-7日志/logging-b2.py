import logging


class CreatLogger:

    def __init__(self, filename, formatter, level):
        self.filename = filename
        self.formatter = formatter
        self.level = level

    def create_logger(self, logger_name):
        log_obj = logging.getLogger(logger_name)
        # 设置记录器的等级
        log_obj.setLevel(self.level)
        handler = logging.FileHandler(self.filename, encoding="utf-8", mode="w")
        # 设置处理器的恩济
        handler.setLevel(self.level)
        formatter = logging.Formatter(self.formatter)
        handler.setFormatter(formatter)
        # 挂载处理器
        log_obj.addHandler(handler)

        return log_obj

if __name__ == '__main__':

    v_formatter = "时间：%(asctime)s || 文件名：%(filename)s ||" \
                  "行号：%(lineno)d|| 级别：%(levelname)s || 内容：%(message)s"
    v_file = "testlogging.log"
    v_level = logging.DEBUG
    logger = CreatLogger(v_file, v_formatter, v_level)
    logger_obj = logger.create_logger('test')

    logger_obj.debug("debug等级的数据")


