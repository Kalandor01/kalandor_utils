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


def _timed_input(text="Quick: ", time=3000):
    """
    Runs a function after a scecified number of millisecounds.
    """
    from time import sleep
    from concurrent.futures import ThreadPoolExecutor 

    def t_input(text:str):
        res = -1
        res = input()
        return res

    future = ThreadPoolExecutor().submit(t_input, text)
    return_value = future.result()

    sleep(time/1000)
    if return_value == -1:
        print("\n")
    return return_value