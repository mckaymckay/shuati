# 螺旋矩阵


def spiralOrder(matrix):
    if not matrix or not matrix[0]:
        return []
    m, n = len(matrix), len(matrix[0])
    left, right, up, down = 0, n - 1, 0, m - 1  #表示四个方向的边界
    res = []
    x, y = 0, 0  #表示当前位置
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]  #表示移动方向是：右下左上
    cur_d = 0  #表示当前的移动方向的下标
    while len(res) != m * n:
        res.append(matrix[x][y])
        if cur_d == 0 and y == right:
            cur_d += 1
            up += 1
        elif cur_d == 1 and x == down:
            cur_d += 1
            right -= 1
        elif cur_d == 2 and y == left:
            cur_d += 1
            down -= 1
        elif cur_d == 3 and x == up:
            cur_d += 1
            left += 1
        cur_d %= 4
        x += dirs[cur_d][0]
        y += dirs[cur_d][1]
    return res


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(spiralOrder(matrix))

dir=[(0, 1), (1, 0), (0, -1), (-1, 0)]
print(dir[0][1])
print(type(dir))