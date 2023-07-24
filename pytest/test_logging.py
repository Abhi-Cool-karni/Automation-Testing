import logging

def test_loggingDemo():

    logger = logging.getLogger(__name__)

    # File location 
    fileHandler = logging.FileHandler("logfile.log")

    # Log format
    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)

    logger.setLevel(logging.DEBUG)

    logger.debug("Debug is executed")
    logger.info("Specific Information is optional if argument is blank then runtime info will save.")
    logger.warning("Something is in warning mode.")
    logger.error("A major error has happened")
    logger.critical("Critical issue")
