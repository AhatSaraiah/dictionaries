# exercises 17-19 :


# exercise 17:

# given a list remove all the duplcates from it using set objects 

def remove_duplicates(l):
    return set(l)


# exercise 18 :
# wrire a method to find all primes less than or equal to n,

n=1000000

# def get_mersenne_prime(n):

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def mersenne_prime(p):
    return 2**p - 1

def print_mersenne_primes(n):
    primes_set = set(num for num in range(2, n + 1) if is_prime(num))

    # Set of Mersenne primes with exponents from 2 to 31 (inclusive) that are less than the n
    mersenne_primes = set(mersenne_prime(p) for p in range(2, 31) if mersenne_prime(p) < n)

    # Intersection of the sets to find Mersenne primes less than the limit
    mersenne_primes_less_than_n = primes_set.intersection(mersenne_primes)

    print("Mersenne primes less than", n, "are:")
    for prime in sorted(mersenne_primes_less_than_n):
        print(prime)


# exercise 19:

###write a generator function that returns the power set of a given set 

def power_set(s):
    """Yields each possible subset of s."""
    for i in range(2**n):
            subset = set()
            for j in range(n):
                if (i & (1 << j)) != 0:
                    subset.add(list(s)[j])
            yield subset


