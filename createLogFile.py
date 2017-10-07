import logging


def log():
    logging.basicConfig(filename='~/debugServer.log', level=logging.DEBUG)
    logging.debug('This message should go to the log file')
    logging.info('So should this')
    logging.warning('And this, too')


if __name__ == '__main__':
    log()
