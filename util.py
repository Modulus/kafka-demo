import datetime


def stamp_message(message, fmt='%Y-%m-%d-%H-%M-%S Message: {message}'):
    return datetime.datetime.now().strftime(fmt).format(message=message)

def get_timestamp(fmt='%Y-%m-%d-%H-%M-%S'):
    return datetime.datetime.now().strftime(fmt)