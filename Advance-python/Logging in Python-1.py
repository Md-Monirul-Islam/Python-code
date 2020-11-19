from logging import *
basicConfig(filename="logfile.log",level=DEBUG,filemode='w',format="%(asctime)s--%(message)s")
debug("This is debug in w mode")
info("This is info")
warning("This is warning")
error("This is error")
critical("This is critical")