import logging

log_levels = {
    'ERROR': logging.ERROR,
    'WARNING': logging.WARNING,
    'DEBUG': logging.DEBUG,
    'INFO': logging.INFO,
    'CRITICAL': logging.CRITICAL,
    'NOTSET': logging.NOTSET,
}

def enc_logger(logger, log_config):
    logging_format = '[%(levelname)s] %(asctime)-15s:%(message)s'
    Formatter = logging.Formatter(fmt=logging_format)
    log_level = log_levels.get(log_config.get('log_level'))
    file_handler = logging.FileHandler(log_config.get('log_file'))
    file_handler.setLevel(log_levels.get('DEBUG'))
    file_handler.setFormatter(Formatter)
    logger.addHandler(file_handler)

