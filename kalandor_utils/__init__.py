"""
This module contains some miscellaneous functions that couldn't fit into other modules.
"""
__version__ = '1.0'


def imput(ask="Num: ", type=int):
    """
    Input but only accepts (whole) numbers.
    """
    while True:
        try: return type(input(ask))
        except ValueError: print(f'Not{" whole" if type == int else ""} number!')


def timed_input(time=5000):
    """
    Runs a function after a scecified nomber of millisecounds
    """
    from time import sleep
    import threading

    sleep(time/1000)
