s = input()
c = {}
for x in s:
    c[x] = c.get(x, 0) + 1

mid = ''
h = ''
for k in sorted(c):
    if c[k] % 2:
        if mid:
            print("NO SOLUTION")
            exit()
        mid = k * c[k]
    else:
        h += k * (c[k] // 2)

l = ''
for k in sorted(c):
    l += k * (c[k] // 2)

print(l + mid + l[::-1])
