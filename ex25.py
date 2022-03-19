#Jeszcze więcej praktyki

def break_words(stuff):
    """ Ta funkcja rozbija zadanie na slowa """
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sortuje slowa."""
    return sorted(words)

def print_first_word(words):
    """Drukuje pierwsze słowo i usuwa je ze zdania. """
    word = words.pop(0)
    print (word)

def print_last_word(words):
    """Drukuje pierwsze i ostatnie słowo zdania. """
    word = words.pop(-1)

def sort_sentence(sentence):
    """Drukuje pierwsze i ostatnie słowo zdania."""
    words = break_words(words)
    print_first_words(words)
    print_last_word(words)
def print_first_and_last_sorted(sentence):
    """ Sortuje słowa, a następnie drukuje pierwsze i ostatnie."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_words(words)
