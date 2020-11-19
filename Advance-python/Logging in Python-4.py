from logging import *
LOG_FORMAT = "{lineno}->>{name}->>{asctime}->>{message}"
basicConfig(filename="logfile.log",level=DEBUG,filemode='w',style="{",format=LOG_FORMAT)
logger = getLogger("Munna")
logger.debug("This is debug")
logger.info("This is info")
logger.warning("This is warning")
logger.error("This is error")
logger.critical("This is critical")