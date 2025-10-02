import numpy as np


def spiral_matrix(n, m):
    left, top, right, bottom = 0, 0, m, n
    res = np.zeros((n, m))

    num = 1

    while left < right and top < bottom:

        res[top, left: right] = np.arange(num, num+right-left)
        num += right - left
        top += 1

        res[top:bottom, right-1] = np.arange(num, num+bottom-top)
        num += bottom - top
        right -= 1

        if not (left < right and top < bottom):
            break

        res[bottom-1, left:right][::-1] = np.arange(num, num+right-left)
        num += right - left
        bottom -= 1

        res[top:bottom, left][::-1] + np.arange(num, num+bottom-top)
        num += bottom - top
        left += 1

    return res

x = int(input())
y = int(input())
ans = spiral_matrix(x, y)
for i in range(x):
    ans[i] *= (i+1)

print(ans)