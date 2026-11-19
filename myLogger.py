import logging


def giveMeLoggingObject():
    format_str = '%(asctime)s %(levelname)s %(message)s'
    file_name  = 'forensics_log.txt'
    logging.basicConfig(format=format_str, filename=file_name, level=logging.INFO)
    return logging.getLogger('kubesec')
