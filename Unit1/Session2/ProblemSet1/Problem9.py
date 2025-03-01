def divider(n):
    mylst = []
    for num in range(1, n  + 1):
        if n % num == 0:
            mylst.append(num)
    return mylst

print(divider(6))