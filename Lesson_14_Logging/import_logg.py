# import logging

# a = 5
# b = 0

# try:
#   c = a / b
# except Exception as e:
#   logging.error("Exception occurred", exc_info=True)
#   logging.warning('This is a warning message', exc_info > 0)
#   logging.debug('This is a debug message')
#   logging.critical('This is a critical message')



# import logging

# logging.basicConfig(format="%(levelname)s | %(asctime)s | %(message)s")
# logging.warning("Something bad is going to happen")



# import logging
# from logging.config import dictConfig

# logging_config = dict(
#     version = 1,
#     formatters = {
#         'f': {'format':
#               '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'}
#         },
#     handlers = {
#         'h': {'class': 'logging.StreamHandler',
#               'formatter': 'f',
#               'level': logging.DEBUG}
#         },
#     root = {
#         'handlers': ['h'],
#         'level': logging.DEBUG,
#         },
# )

# dictConfig(logging_config)

# logger = logging.getLogger()
# logger.debug('often makes a very good meal of %s', 'visiting tourists')


# import logging

# logger = logging.getLogger()
# handler = logging.StreamHandler()
# formatter = logging.Formatter(
#         '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
# handler.setFormatter(formatter)
# logger.addHandler(handler)
# logger.setLevel(logging.DEBUG)

# logger.debug('often makes a very good meal of %s', 'visiting tourists')