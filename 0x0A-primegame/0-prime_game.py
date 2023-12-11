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

    # Function to generate primes up to n
    def generate_primes(n):
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if sieve[i]:
                for j in range(i * i, n + 1, i):
                    sieve[j] = False
        return [i for i, is_prime in enumerate(sieve) if is_prime]

    # Function to play a round
    def play_round(n):
        primes = generate_primes(n)
        return len(primes) % 2 == 0  # Ben wins if the number of primes is even

    # Play all rounds and count Ben's wins
    ben_wins = sum(play_round(n) for n in nums)

    # Determine the winner
    if ben_wins > x / 2:
        return "Ben"
    elif ben_wins < x / 2:
        return "Maria"
    else:
        return None  # It's a draw