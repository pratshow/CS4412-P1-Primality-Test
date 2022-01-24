import math
import random


def prime_test(N, k):
    # This is main function, that is connected to the Test button. You don't need to touch it.
    return fermat(N, k), miller_rabin(N, k)

# Runs in O(n^3) time due to each recursive call reducing it by about 1/2 and the division is n^2 leading to O(n^3)
def mod_exp(x, y, N):
    if (y == 0):
        return 1
    else:
        z = mod_exp(x, (y//2), N)
        if (z % 2 == 0):             # if mod 2 is 0 then the number is even, otherwise odd
            return (z ** 2) % N      # z^2 mod N
        else:
            return x * (z ** 2) % N  # x * z^2 mod N

# Simply O(n^2) due to division
# this is the probability that the algorithm is incorrect
def fprobability(k):
    return 1 / (2 ** k)

# Simply O(n^2) due to division
# this is the probability that the algorithm is incorrect
def mprobability(k):
    return 1 / (4 ** k)

# runs k times and each iteration it does a mod multiplication witch is O(n^2) this results in O(kn^2) time or O(n^3)
def fermat(N, k):
    ranNumArray = []
    runs = k
    while (runs != 0):             # Filling the array with k random numbers
        ranNumArray.append(random.randint(2, 50))
        runs = runs - 1

    for _ in ranNumArray:
        result = k ** (N - 1) % N  # k^(N-1) mod N
        if (result != 1):
            return 'composite'
    return 'prime'

# Doing the initial fermat test takes O(n^2) time due to the modular multiplication then the square rooting will half
# the result every time being O(log(n)) but each iteration will take O(n^2) time, again due to modular multiplication
# thus we get O(log(k)) with each n^2 modular multiplication being O(n^3)
def miller_rabin(N, k):
    ranNumArray = []
    runs = k
    while (runs != 0):             # Filling the array with k random numbers
        ranNumArray.append(random.randint(2, 50))
        runs = runs - 1

    for _ in ranNumArray:
        fermat_result = k ** (N - 1) % N       # k^(N-1) mod N
        if (fermat_result != 1):
            return 'composite'                 # Fermat test should be 1
        else:
            sqrt = N - 1
            while (sqrt % 2 == 0):             # Continually does the sqrt of our exponent (originally N) until it's not even
                result = k ** (sqrt // 2) % N
                sqrt = sqrt // 2
                if result == (N - 1):          # check if the result is -1
                    return 'prime'
                if result != 1:                # If the result isn't 1 or -1 the number is composite
                    return 'composite'
    return 'prime'                             # If it's all 1's then it's prime as well