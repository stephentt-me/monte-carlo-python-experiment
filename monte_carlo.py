import time
import sys
from random import random
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed

DEFAULT_TOSSING_AMOUNT = int(1e8)


def tossing_amount(n: int):
    p = 0
    for _ in range(n):
        if random() ** 2 + random() ** 2 < 1:
            p += 1
    return p


def monte_carlo_normal(n: int = DEFAULT_TOSSING_AMOUNT):
    return tossing_amount(n) * 4 / n


def monte_carlo_multiprocess(n:int=DEFAULT_TOSSING_AMOUNT, m:int=4):
    p = 0
    n_sub = n // m
    with ProcessPoolExecutor() as executor:
        futures = [executor.submit(tossing_amount, n_sub) for _ in range(m)]
        for future in as_completed(futures):
            p += future.result()
    return p * 4 / n


def monte_carlo_thread(n:int=DEFAULT_TOSSING_AMOUNT, m:int=4):
    p = 0
    n_sub = n // m
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(tossing_amount, n_sub) for _ in range(m)]
        for future in as_completed(futures):
            p += future.result()
    return p * 4 / n


if __name__ == "__main__":
    start_time = time.time()

    if len(sys.argv) >= 2:
        if sys.argv[1] == "normal":
            print(monte_carlo_normal())
        elif sys.argv[1] == "multiprocess":
            print(monte_carlo_multiprocess())
        elif sys.argv[1] == "thread":
            print(monte_carlo_thread())
    else:
        print("Give a valid parameter in [normal|multiprocess|thread]")

    print("Executed time: {}s".format(time.time() - start_time))
