def total_profit(n):
    prices = [1, n, 1, n, 1]
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]
        return profit

input("total_profit(n) sums every upswing in prices [1, n, 1, n, 1]. Press enter")
print("total_profit(4) = ", total_profit(4))

n = int(input("Enter n: "))

print(f"total_profit({str(n)}) = {total_profit(n)}")
