import datetime


def stampMessage(message, fmt='%Y-%m-%d-%H-%M-%S Message: {message}'):
    return datetime.datetime.now().strftime(fmt).format(message=message)