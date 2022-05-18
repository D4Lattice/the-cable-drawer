#A collection of interesting and/or useful Python code snippets.

#Sieve of Eratosthenes
from math import sqrt,ceil

def get_primes(space):
    primes = []
    
    for x in range(2,space):
        is_prime = True
        root = ceil(sqrt(x))
        
        for prime in primes:
            if prime > root:
                break
            if x%prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(x)
    return(primes)
  
#Pythagorean Triples - list comprehension, integers only
from math import sqrt,ceil

def get_trips(upper_bound):
  triples = [(a,b,c)
             for a in range(1,upper_bound)
             for b in range(a,upper_bound)
             if (c:= sqrt(a**2+b**2)).is_integer()]
  
  
