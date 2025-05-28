n = int(input())
if n == 2 or n == 3:
    print("NO SOLUTION")
else:
    print(*range(2, n+1, 2), *range(1, n+1, 2))
