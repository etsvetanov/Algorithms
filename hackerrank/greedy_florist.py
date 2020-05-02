def get_min_cost(k, c):
    total_cost = 0
    sorted_prices = sorted(c, reverse=True)

    for i, price in enumerate(sorted_prices):
        total_cost += price * ((i // k) + 1)

    return total_cost
