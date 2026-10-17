def rainwater(n):
    bars = [0, n, 0, n, 0]
    return min(max(bars[:3]), max(bars[2:])) - bars[2]

n = int(input("Enter bar height"))

print(f"rainwater({str(n)}) = {rainwater(n)}")
