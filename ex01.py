import time

def find_coins_greedy(amount, coins=[50, 25, 10, 5, 2, 1]):
    start_time = time.time()
    result = {}
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            amount -= count * coin
            result[coin] = count
    end_time = time.time()
    print(f"Жадібний алгоритм виконався за: {end_time - start_time:.6f} секунд")
    print(f"Монети: {result}")
    return result

def find_min_coins(amount, coins=[50, 25, 10, 5, 2, 1]):
    start_time = time.time()
    
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_used = [0] * (amount + 1)
    
    for coin in coins:
        for x in range(coin, amount + 1):
            if dp[x - coin] + 1 < dp[x]:
                dp[x] = dp[x - coin] + 1
                coin_used[x] = coin

    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin

    end_time = time.time()
    print(f"Динамічне програмування виконався за: {end_time - start_time:.6f} секунд")
    print(f"Монети: {result}")
    return result

amount = 113
print(f"Сума для видачі решти = {amount}")
print("=== Жадібний алгоритм ===")
find_coins_greedy(amount)
print("\n=== Алгоритм динамічного програмування ===")
find_min_coins(amount)

print("\n==================")
print("\nДля демонстрації часу:")

amount = 999999
print(f"Сума для видачі решти = {amount}")
print("=== Жадібний алгоритм ===")
find_coins_greedy(amount)
print("\n=== Алгоритм динамічного програмування ===")
find_min_coins(amount)