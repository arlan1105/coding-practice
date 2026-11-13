def divisors(integer):
    nums = [n for n in range(2, integer) if integer%n == 0]
    return nums if nums else f'{integer} is prime'
