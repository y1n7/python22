import logging


class LoggerHandler(logging.Logger):

    def __init__(self,
                 name,
                 level=0,
                 file_name=None,
                 handler_level=0,
                 fmt="%(asctime)s-%(name)s-%(levelname)s-%(filename)s-%(lineno)d-%(message)s",
                 **kw):
        super().__init__(name, level)
        if not file_name:
            handler = logging.StreamHandler()
        else:
            handler = logging.FileHandler(file_name)
        handler.setLevel(handler_level)
        self.addHandler(handler)
        handler_format = logging.Formatter(fmt)
        handler.setFormatter(handler_format)


if __name__ == '__main__':

    logger = LoggerHandler('test_logger_handler')
    logger.info('test_info_two')
    logger.debug('test_debug_two')
    logger.warning('test_warning_two')
    logger.error('test_error_two')
    logger.critical('test_critical_two')

    logger = LoggerHandler('file logger', 0, 'logger_file.log', 0)
    logger.info('info-file')
    logger.debug('debug-file')
    logger.warning('warning-file')
    logger.error('error-file')
    logger.critical('critical-file')


