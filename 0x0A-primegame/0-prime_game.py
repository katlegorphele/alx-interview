#!/usr/bin/python3

def isWinner(x, nums):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def remove_multiples(num, nums):
        return [n for n in nums if n % num != 0]

    def can_make_move(nums):
        for num in nums:
            if is_prime(num):
                return True
        return False

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        current_nums = list(range(1, n + 1))
        maria_turn = True

        while can_make_move(current_nums):
            prime_candidates = [num for num in current_nums if is_prime(num)]

            if maria_turn:
                chosen_prime = min(prime_candidates)
                maria_wins += 1
            else:
                chosen_prime = max(prime_candidates)
                ben_wins += 1

            current_nums = remove_multiples(chosen_prime, current_nums)
            maria_turn = not maria_turn

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# Example usage:
# x = 3
# nums = [4, 5, 1]
# result = isWinner(x, nums)
# print(result)
