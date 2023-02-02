import logging

# 1
# logger = logging.getLogger(__name__)
# logger.info("Hello from helper")
# logger.propagate= False # this will stop the logger from propagating further
# logger.info("Hello from helper")

# 2
logger = logging.getLogger(__name__)
# stream handler and file handler
strm_handler = logging.StreamHandler()
file_handler = logging.FileHandler("file.txt")
# setting levels to the handler
strm_handler.setLevel(logging.WARNING)
file_handler.setLevel(logging.ERROR)
# defining formatter and asssing to handlers
formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
strm_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)
# add handler to logging
logger.addHandler(strm_handler)
logger.addHandler(file_handler)

logger.info("Hello from helper")
logger.debug("Hello from helper")
logger.warning("Hello from helper")
logger.error("Hello from helper")
logger.critical("Hello from helper")

