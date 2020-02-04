import logging.config
from os import path, mkdir, getenv

currDir = path.dirname(path.abspath(__file__))
logsDir = path.join(currDir, '.logs')

if not path.exists(logsDir) or not path.isdir(logsDir):
    mkdir(logsDir)

LOGGER_DEBUG = getenv('ANVID_DEBUG', True)
LOGGER_NAME = 'anvid'
LOGGER_FORMAT = '[{asctime}] {levelname} {module}:{lineno:d} "{message}"'
LOGGER_FILE = path.join(logsDir, f'{LOGGER_NAME}.log')


class FilterDebugTrue(logging.Filter):
    def filter(self, record):
        return LOGGER_DEBUG


class FilterDebugFalse(logging.Filter):
    def filter(self, record):
        return not LOGGER_DEBUG


logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'debug_true': {
            '()': FilterDebugTrue
        },
        'debug_false': {
            '()': FilterDebugFalse
        }
    },
    'formatters': {
        'default': {
            'format': LOGGER_FORMAT,
            'style': '{',
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'formatter': 'default',
            'filters': ['debug_true'],
            'class': 'logging.StreamHandler',
        },
        'file': {
            'level': 'INFO',
            'formatter': 'default',
            'class': 'logging.handlers.RotatingFileHandler',
            'filters': ['debug_false'],
            'filename': LOGGER_FILE,
            'maxBytes': 100 * 1024,
            'backupCount': 10
        }
    },
    'loggers': {
        LOGGER_NAME: {
            'level': 'DEBUG',
            'handlers': ['console', 'file'],
            'propagate': False,
        },
    }
})

logger = logging.getLogger(LOGGER_NAME)
