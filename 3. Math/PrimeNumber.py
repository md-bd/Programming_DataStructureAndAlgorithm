def is_prime(n):
    """ 
    returns 1 if prime, otherwise 0
    """
    i = 2
    if n <= 1:
        return 0

    while(i*i <= n):
        if n % i == 0:
            return 0
        i += 1
        
    return 1

if __name__ == "__main__":

    print(is_prime(13))
    print(is_prime(100))

