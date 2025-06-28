import timeit
from typing import Dict, Tuple


atm_nominal = [50, 25, 10, 5, 2, 1]


def find_coins_greedy(amount: int) -> Dict[int, int]:
    coins_count = {coin: 0 for coin in atm_nominal}
    remaining = amount

    for coin in atm_nominal:
        count = remaining // coin
        remaining = remaining % coin
        coins_count[coin] = count
        if remaining == 0:
            break
    return coins_count


def find_min_coins(amount: int) -> Dict[int, int]:
    max_value = float('inf')
    min_coins = [0] + [max_value] * amount
    coin_choice = [0] * (amount + 1)

    for sub_amount in range(1, amount + 1):
        for coin in atm_nominal:
            if coin <= sub_amount and min_coins[sub_amount - coin] + 1 < min_coins[sub_amount]:
                min_coins[sub_amount] = min_coins[sub_amount - coin] + 1
                coin_choice[sub_amount] = coin

    coins_count = {coin: 0 for coin in atm_nominal}
    remaining = amount

    while remaining > 0:
        coin = coin_choice[remaining]
        coins_count[coin] += 1
        remaining -= coin
    return coins_count


def measure_execution_time(algorithm, amount) -> Tuple[Dict[int, int], float]:
    start = timeit.default_timer()
    result = algorithm(amount)
    elapsed = timeit.default_timer() - start
    return result, elapsed


def main():
    amounts = [1, 113, 99, 1234, 20, 99999, 37]

    for amount in amounts:
        print(f"Testing amount: {amount}")

        coins_greedy, time_greedy = measure_execution_time(find_coins_greedy, amount)
        print(f"Greedy algorithm took {time_greedy:.8f}s, coins: {coins_greedy}")

        coins_dynamic, time_dynamic = measure_execution_time(find_min_coins, amount)
        print(f"Dynamic programming took {time_dynamic:.8f}s, coins: {coins_dynamic}\n")


if __name__ == "__main__":
    main()

