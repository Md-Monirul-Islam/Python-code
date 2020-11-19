''''
1. Write logging conﬁguration for a program which logs to a ﬁle called log.txt and discards
all logs less important than INFO.
'''
import logging
logging.basicConfig(filename='log.txt', level=logging.INFO)