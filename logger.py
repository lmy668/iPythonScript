import logging
import sys

LOG_FORMMAT = "%(levelname)-5s %(asctime)s %(pathname)s %(funcName)s %(module)s %(filename)s:%(lineno)d %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


class Logger(logging.Logger):
    def __init__(self, name, level=logging.DEBUG, file=None):
        super().__init__(name, level)
        init_logger = logging.getLogger(name)
        formatter = logging.Formatter(LOG_FORMMAT, DATE_FORMAT)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        self.addHandler(console_handler)
        init_logger.addHandler(console_handler)

        if file:
            file_handler = logging.FileHandler(file, encoding="utf-8")
            file_handler.setFormatter(formatter)
            self.addHandler(file_handler)
        # self.addHandler(console_handler)
        self.propagate = False
        # 先初始化init方法，然后给实列self添加一个对象名称教logger1，已备后用
        self.logger1 = init_logger

    def info(self, msg, *args, **kwargs):
        # 下面确实调用父类的方法，可能因为init后，子类的实例就拥有父类的所有方法了，但实例未设置init_logger.setLevel(level)级别，所以不打印日志
        self.logger1.info(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        super().warning(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        # 这是使用的父类的方法，init的时候传入子类的level给父类完成了初始化，所以打印日志
        super().error(msg, *args, **kwargs)

    def critical(self, msg, *args, **kwargs):
        super().critical(msg, *args, **kwargs)


def get_logger(name):
    return Logger(name)


COLORS = {
    "DEBUG": "\033[94m",  # Blue
    "INFO": "\033[92m",  # Green
    "WARNING": "\033[93m",  # Yellow
    "ERROR": "\033[91m",  # Red
    "CRITICAL": "\033[91m",  # Red
    "ENDC": "\033[0m",  # Reset color
}


# class ColoredFormatter(logging.Formatter):
#     def format(self, record):
#         levelname = record.levelname
#         if levelname in COLORS:
#             record.levelname = f"{COLORS[levelname]}{levelname}{COLORS['ENDC']}"
#         return super().format(record)


if __name__ == "__main__":
    logger = get_logger("test")
    print("hello")
    logger.info("info %d", 1)
    # logger.warning('warning')
    logger.error("error")
    # logger.critical('critical')
