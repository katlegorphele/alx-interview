#!/usr/bin/python3

'''
Module that contains the isWinner function
'''

def isWinner(x, nums):
    '''
    Prime Game
    '''
    if not nums or x < 1:
        return None
    n = max(nums)
    sieve = [True] * (n + 1)
    sieve[0] = False
    sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i] == True:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    primes = []
    for i in range(len(sieve)):
        if sieve[i] == True:
            primes.append(i)
    player1 = 0
    for i in nums:
        if i in primes:
            player1 += 1
    if player1 % 2 == 0:
        return "Ben"
    else:
        return "Maria"