import logging

from pubg.config import DEBUG


def logger_init(debug=False):
	logger = logging.getLogger()

	if debug:
		logger.setLevel(logging.DEBUG)
	else:
		logger.setLevel(logging.INFO)

	ch = logging.StreamHandler()
	ch.setLevel(logging.DEBUG)

	formatter = logging.Formatter('[%(levelname)s] %(asctime)s %(message)s')

	ch.setFormatter(formatter)

	logger.addHandler(ch)

	return logger


logger = logger_init(DEBUG)