#!/usr/bin/python3
"""Defines island perimeter finding function."""


def isWinner(x, nums):
    '''Prototype: def isWinner(x, nums)
    where x is the number of rounds and nums is an array of n
    Return: name of the player that won the most rounds
    If the winner cannot be determined, return None
    '''
    def sieve_of_eratosthenes(max_n):
        primes = [True] * (max_n + 1)
        primes[0] = primes[1] = False  # 0 and 1 are not primes
        for i in range(2, int(max_n ** 0.5) + 1):
            if primes[i]:
                for j in range(i * i, max_n + 1, i):
                    primes[j] = False
        return [i for i, is_prime in enumerate(primes) if is_prime]

    # Precompute all primes up to the largest n in nums
    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    # Game simulation
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # Initialize game state for numbers up to n
        available_primes = [p for p in primes if p <= n]
        if not available_primes:
            ben_wins += 1  # If no primes, Ben wins automatically
            continue

        turn = 0  # Maria's turn if 0, Ben's turn if 1
        while available_primes:
            current_prime = available_primes.pop(0)
            # Remove the current prime and all its multiples
            available_primes = [p for p in available_primes if p % current_prime != 0]
            turn = 1 - turn  # Switch turns

        # If turn is 0, it means Ben made the last move, so Maria wins
        if turn == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine who won the most games
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
