import re

def is_numbered_list(sentence: str):
    return re.match("[0-9][0-9]*.", sentence) is None

def get_numbered_list(message: str):
    return [x[3:] for x in message.split("\n") if not is_numbered_list(x)]
