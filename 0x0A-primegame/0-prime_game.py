#!/usr/bin/python3

'''
Prototype: def isWinner(x, nums)
where x is the number of rounds and nums is an array of n
Return: name of the player that won the most rounds
If the winner cannot be determined, return None
assume n and x will not be larger than 10000
'''

def isWinner(x, nums):
    if not nums or x < 1:
        return None

    n = max(nums)
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False

    primes = []
    for i in range(len(sieve)):
        if sieve[i]:
            primes.append(i)

    wins = 0
    for n in nums:
        if n in primes:
            wins += 1

    if wins == x:
        return "Maria"
    if wins < x:
        return "Ben"
    return None



