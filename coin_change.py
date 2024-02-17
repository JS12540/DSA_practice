coins = [1,2,5]
amount = 60

def calulate_minimum_coins_needed(amount, coins):

    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount+1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i-coin]+1)
            else:
                break
    print(dp)
    return dp[amount]


ans = calulate_minimum_coins_needed(amount, coins)
print(f"Answer is {ans}")
