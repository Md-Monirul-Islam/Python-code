from logging import *
basicConfig(filename="logfile_1.log",level=DEBUG)
debug("This is debug")
info("This is info")
basicConfig(filename="logfile.log")
warning("This is warning")
error("This is error")
critical("This is critical")