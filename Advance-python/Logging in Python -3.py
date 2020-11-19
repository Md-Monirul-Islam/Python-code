from logging import *
LOG_FORMAT = "%(asctime)s->>%(message)s->>%(lineno)d"
basicConfig(filename="logfile.log",level=DEBUG,filemode='w',format=LOG_FORMAT)
debug("This is debug in w mode")
info("This is info")
warning("This is warning")
error("This is error")
critical("This is critical")