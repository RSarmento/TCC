from unicodedata import normalize


def remove_special_characters(text):
    return normalize('NFKD', text).encode('utf-8', 'ignore').decode('utf-8')


def remove_punctuation(text):
    return text


class Remover:
    pass
