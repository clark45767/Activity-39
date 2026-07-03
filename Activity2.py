heights = [0, 1, 0, 3, 1, 0, 1, 3, 2, 1, 2, 1, ]
n = len (heights)
left_tallest = [0] * n
left_tallest[0] = heights[0]
for i in range(1, n):
    left_tallest[i] = max(left_tallest[i - 1], heights[i])
print('Heights:     ',heights)
print('Left tallest:', left_tallest)


right_tallest = [0] * n
right_tallest[n - 1] = heights[n -1]
for i in range(n -2, -1, -1):
    right_tallest[i] = max(right_tallest[i + 1], heights[i])
print('right tallest:', right_tallest)


water = 0
for i in range(n):
    water += min(left_tallest[i], right_tallest[i]) - heights[i]
print('Total water trapped:', water)
