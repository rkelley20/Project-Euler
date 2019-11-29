from euler.primes import nth_prime

def euler7():
    '''
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

    What is the 10 001st prime number?
    '''
    return nth_prime(10001)
