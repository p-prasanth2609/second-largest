a = list(map(int, input().split()))
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] > a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
if len(a) == 1 or len(a) == 0 or a[-1] == a[0]:
    print(-1)
else:
    print(a[-2])
