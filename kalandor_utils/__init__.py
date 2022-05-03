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


# _timed_input()

def thread_test():
    from time import sleep
    import concurrent.futures as future

    def func_input(text:str):
        ans = -1
        ans = input(text)
        return ans
    
    def func_timer(time:int=3, text:str="ask: "):
        with future.ThreadPoolExecutor() as th:
            th_input = th.submit(func_input, text)
            sleep(time)
            print("STOP")
            return_ans = th_input.result()
            resoult = return_ans
            return resoult

    with future.ThreadPoolExecutor() as th:
        th_1 = th.submit(func_timer, 5, "question: ")
        sleep(3)
        print("STOP")
        return_val = th_1.result()
        print(return_val)

# thread_test()








# from threading import Thread
# import time
# import os

# answer = None


# def ask():
#     global start_time, answer
#     start_time = time.time()
#     answer = input("Enter a number:\n")
#     time.sleep(0.001)


# def timing():
#     time_limit = 5
#     while True:
#         time_taken = time.time() - start_time
#         if answer is not None:
#             print(f"You took {time_taken} seconds to enter a number.")
#             os._exit(1)
#         if time_taken > time_limit:
#             print("Time's up !!! \n"
#                   f"You took {time_taken} seconds.")
#             os._exit(1)
#         time.sleep(0.001)


# t1 = Thread(target=ask)
# t2 = Thread(target=timing)
# t1.start()
# t2.start()