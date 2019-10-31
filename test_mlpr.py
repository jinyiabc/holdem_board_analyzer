# prime_mutiprocessing.py

import time
import math
from multiprocessing import Pool
from multiprocessing import freeze_support
import traceback


'''Define function to run mutiple processors and pool the results together'''
def run_multiprocessing(func, i, n_processors):
    pool = Pool(processes=n_processors)
    return pool.map(func, i)


'''Define task function'''
def is_prime(n):
    try:
        if (n < 2) or (n % 2 == 0 and n > 2):
            return False
        elif n == 2:
            return True
        elif n == 3:
            return True
        else:
            for i in range(3, math.ceil(math.sqrt(n)) + 1, 2):
                if n % i == 0:
                    return False
            return True
    except Exception as e:
        print('Caught exception in worker thread (n = %d):' % n)

        # This prints the type, value, and stack trace of the
        # current exception being handled.
        traceback.print_exc()

        print()
        raise e


def main():
    start = time.clock()

    '''
    set up parameters required by the task
    '''
    num_max = 1000000
    n_processors =6
    x_ls = list(range(num_max))

    '''
    pass the task function, followed by the parameters to processors
    '''
    out = run_multiprocessing(is_prime, x_ls, n_processors)

    print("Input length: {}".format(len(x_ls)))
    print("Output length: {}".format(len(out)))
    print("Mutiprocessing time: {}mins\n".format((time.clock()-start)/60))
    print("Mutiprocessing time: {}secs\n".format((time.clock()-start)))


if __name__ == "__main__":
    freeze_support()   # required to use multiprocessing
    main()
