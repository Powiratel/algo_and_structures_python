from random import random

N = 15
arr = [0] * N
for i in range(N):
    arr[i] = int(random() * 100)
    print(arr[i], end=' ')
print()

# 1-й вариант
mn = min(arr)
mx = max(arr)
imn = arr.index(mn)
imx = arr.index(mx)
print('arr[%d]=%d arr[%d]=%d' % (imn + 1, mn, imx + 1, mx))
arr[imn], arr[imx] = arr[imx], arr[imn]