import logging

# more on: https://docs.python.org/3/library/logging.html

# 1
logging.basicConfig(
    level=logging.WARNING,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%d/%m/%Y %H:%M:%S",
)
logging.debug("cea1")
logging.info("cea2")
logging.warning("cea3")
logging.error("cea4")
logging.critical("cea5")

# 2
import logger_helper

# 3
try:
    arr = [1,2,3]
    print(arr[4])
except IndexError as e:
    logging.error(e,exc_info=True)

# 4
import traceback
try:
    arr = [1,2,3]
    print(arr[4])
except:
    logging.error(traceback.format_exc())

# 5 - not working
# from logging.handlers import RotatingFileHandler

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)

# handler = RotatingFileHandler("./intermediate_level/logger_module/logfile.log",maxBytes=2000, backupCount=5)
# logger.addHandler(handler)

# for _ in range(10000):
#     logging.info("this is an error")

# 6 - not working
# from logging.handlers import TimedRotatingFileHandler
# import time

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)

# handler = TimedRotatingFileHandler("./intermediate_level/logger_module/logfile.log",when="s", interval=5 ,backupCount=5)
# logger.addHandler(handler)

# for _ in range(3):
#     logging.info("this is an error")
#     time.sleep(5)