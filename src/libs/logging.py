import logging

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(module)s(%(funcName)s() line %(lineno)d)- %(message)s')

# create console handler and set level to debug
Streamhandler = logging.StreamHandler()
Streamhandler.setLevel(logging.DEBUG)

# create formatter

# add formatter to Streamhandler
Streamhandler.setFormatter(formatter)


# create console handler and set level to debug
FileHandler = logging.FileHandler("debug.log")
FileHandler.setLevel(logging.DEBUG)


# add formatter to Streamhandler
FileHandler.setFormatter(formatter)

def get_logger():
	# create logger
	logger = logging.getLogger("asm-observer")
	logger.setLevel(logging.DEBUG)

	# add Streamhandler to logger
	logger.addHandler(Streamhandler)
	logger.addHandler(FileHandler)

	return logger