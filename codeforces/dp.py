def solution(S: int, coin_weights: set):
    ordered_weights = sorted(coin_weights)
    min_coins_to_reach_sum = [0] * (S + 1)

    # p - partial sum
    for p in range(1, S+1):
        min_coins = p + 1  # assume the worst case of coin value 1 (e.g. 100 cents to reach S of $1)

        for coin_value in ordered_weights:
            if coin_value <= p:
                current_coins = min_coins_to_reach_sum[p - coin_value] + 1
                min_coins = min(min_coins, current_coins)

        min_coins_to_reach_sum[p] = min_coins if min_coins <= p else 0

    return min_coins_to_reach_sum[S]


print(solution(10, {2, 3, 7}))