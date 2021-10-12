'''
The function for creating loggers
'''
# Function for constructing a variety of logger commands
def construct_logger(log_name, name = 'testing'):
    import logging
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    hdlr = logging.FileHandler(log_name + ".log")
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    return logger
