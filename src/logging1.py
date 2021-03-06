import logging

LOG_FORMAT = "%(asctime)s %(levelname)8s - %(message)s"
logging.basicConfig(filename=r"C:\Users\12818\workspace\python1\jwang.log", level=logging.ERROR, format=LOG_FORMAT)

logger = logging.getLogger("Huaxia")

logger.debug("My first debug message.")
logger.info("My first info message.")
logger.warning("My first warning message.")
logger.error("My first error message.")
logger.fatal("My first fatal message.")
print(logger.level)
