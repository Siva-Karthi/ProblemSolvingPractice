"""
Given
a
standard
M
X
N
chessboard, and a
static
bishop
we
want
to
find
the
minimum
number
of
steps
for a knight to reach a destination position  (S, T) from a source position (X, Y).Here, the source and destination position of the knight on a chessboard is known.

You
can
attack
a
bishop as well.

Algorithm

BFS
for shortest path on the steps is defined by knight at the same time skip the visited paths (dont go back), consider bishop's path and skip it and if its the bishop's place kill it and move freely on the upcoming movements ?

Pseudocode

"""


# def bfs(M,N,X, Y, S, T, BX, BY, visited, threats,bishop_alive = 1):
#     steps = 0
#     queue = []
#     # add position to the queue
#     queue.append([X, Y, bishop_alive])
#
#     # traverse the unvisited next possible knight positions
#     while queue:
#         # take next position from queue
#         _next = queue.pop(0)
#         x, y, is_bishop_alive = _next[0], _next[1], _next[2]
#         # visit the current position
#         visited[x][y] = 1
#         steps += 1
#
#         if x == S and y == T:
#             print(f"found destination( {x}, {y}), ({S}, {T})", )
#             return steps
#         # if bishop_alive and x== BX and y==BY and position == bishop position kill the bishop
#         # if bishop_alive and x == BX and y == BY:
#         #     is_bishop_alive = 0
#
#         next_positions = get_next_positions(M,N, x, y)
#         print("next_positions for ",x,y," = ", next_positions )
#         # next_safe_positions = []
#         bishop_alive = 0
#         # if bishop_alive:
#         #     next_positions = filter_safe_positions(next_positions, threats)
#
#         for pos in next_positions:
#             if visited[pos[0]][pos[1]] == 0:
#                 queue.append([pos[0], pos[1], bishop_alive])
#     return 0
#
#
# def get_next_positions(M, N,x, y):
#     next_possible_moves = []  # 8 moves
#     # x+2, y+1
#     if x + 2 < N and y + 1 < M:
#         next_possible_moves.append([x + 2, y + 1])
#     # x+2, y-1
#     if x + 2 < N and y - 1 >= 0:
#         next_possible_moves.append([x + 2, y - 1])
#     # x-2, y+1
#     if x - 2 >= 0 and y + 1 < M:
#         next_possible_moves.append([x - 2, y + 1])
#     # x-2, y-1
#     if x - 2 >= 0 and y - 1 >= 0:
#         next_possible_moves.append([x - 2, y - 1])
#     # y+2, x+1
#     if y + 2 < M and x + 1 < N:
#         next_possible_moves.append([y + 2, x + 1])
#     # y+2, x-1
#     if y + 2 < M and x - 1 >= 0:
#         next_possible_moves.append([y + 2, x - 1])
#     # y-2, x+1
#     if y - 2 >= 0 and x + 1 < N:
#         next_possible_moves.append([y - 2, x + 1])
#     # y-2, x-1
#     if y - 2 >= 0 and x - 1 >= 0:
#         next_possible_moves.append([y - 2, x - 1])
#     return next_possible_moves
#
#
# def filter_safe_positions(possible_positions, threats):
#     safe_positions = []
#     for pos in possible_positions:
#         if threats[pos[0]][pos[1]] == 0:
#             safe_positions.append(pos)
#     return safe_positions
#
# def get_kinight_min_steps():
#     # knight
#     X,Y = 0, 1
#     S, T = 4,6
#     M = 8
#     N = 8
#
#     # bishop
#     BX = 1
#     BY = 6
#
#     threats = [[0 for i in range(N)] for j in range(M)]
#     threats[BX][BY] = 1
#     # update threats
#     j = BY  # bottom right
#     for i in range(BX + 1, M):
#         j += 1
#         if j>=N:
#             break
#         threats[i][j] = 1
#
#     j = BY  # bottom left
#     for i in range(BX + 1, M):
#         j -= 1
#         if j < 0:
#             break
#         threats[i][j] = 1
#
#     j = BY  # top left
#     for i in range(BX - 1, -1, -1):
#         j -= 1
#         if j < 0:
#             break
#         threats[i][j] = 1
#
#     j = BY  # top right
#     for i in range(BX - 1, -1, -1):
#         j += 1
#         if j >= N:
#             break
#         threats[i][j] = 1
#
#     # from pprint import pprint
#     #
#     # pprint(threats)
#
#     visited = [[0 for i in range(N)] for j in range(M)]
#     steps = bfs(M,N,X, Y, S, T, BX, BY, visited, threats)
#     if steps:
#         return steps
#     return 0


def bfs(M, N, X, Y, S, T, BX, BY, visited, threats, is_bishop_alive=1):
    steps = -1
    queue = []
    # add position to the queue
    queue.append([X, Y, is_bishop_alive, steps])
    parent = {(X, Y): None}

    # traverse the unvisited next possible knight positions
    while queue:
        # take next position from queue
        _next = queue.pop(0)
        x, y, is_bishop_alive = _next[0], _next[1], _next[2]
        # visit the current position
        visited[x][y] = 1
        steps = _next[3] + 1
        if is_bishop_alive and x == BX and y == BY:
            print("kill bishop")
            is_bishop_alive = 0

        if is_bishop_alive:
            is_safe = filter_safe_positions([[x, y]], threats)
            if not is_safe:
                continue

        if x == S and y == T:
            print(f"found destination( {x}, {y}), ({S}, {T})", )
            path = []
            node = (S, T)
            while node is not None:
                path.append(node)
                node = parent.get(node)

            # Return the path from source to destination (reverse the backtracked path)
            print("path  = ", path[::-1] if path[-1] == (X, Y) else None)  # Return None if there's no path

            return steps
        # if bishop_alive and x== BX and y==BY and position == bishop position kill the bishop

        # next_positions = get_next_positions(M,N, x, y)
        next_positions = get_next_positions_2(M, N, x, y)
        # print("_next", _next)
        # print("next_positions for ",x,y," = ", next_positions )
        # next_safe_positions = []

        for pos in next_positions:
            if visited[pos[0]][pos[1]] == 0:
                queue.append([pos[0], pos[1], is_bishop_alive, steps])
                parent[(pos[0], pos[1])] = (x, y)
    return 0


def is_valid(x, y, M, N):
    if (x >= 0 and x < N and y >= 0 and y < M):
        return True


def get_next_positions_2(M, N, x, y):
    next_possible_moves = []  # 8 moves
    x_moves = [2, 2, -2, -2, 1, 1, -1, -1]
    y_moves = [1, -1, 1, -1, 2, -2, 2, -2]
    for i in range(8):
        new_x = x + x_moves[i]
        new_y = y + y_moves[i]
        if is_valid(new_x, new_y, M, N):
            next_possible_moves.append([new_x, new_y])
    # pdb.set_trace()
    return next_possible_moves


def filter_safe_positions(possible_positions, threats):
    safe_positions = []
    for pos in possible_positions:
        if threats[pos[0]][pos[1]] == 0:
            safe_positions.append(pos)
    return safe_positions


def get_kinight_min_steps(M, N, X, Y, S, T, BX, BY):
    threats = [[0 for i in range(N)] for j in range(M)]
    threats[BX][BY] = 1
    # update threats
    # j = BY  # bottom right
    # for i in range(BX + 1, M):
    #     j += 1
    #     if j>=N:
    #         break
    #     threats[i][j] = 1

    i = BX
    j = BY
    while i < M and j < N:
        print(i, j, M, N, i < M, j < N, i < M and j < N)
        threats[i][j] = 1
        i += 1
        j += 1

    j = BY  # bottom left
    for i in range(BX + 1, M):
        j -= 1
        if j < 0:
            break
        threats[i][j] = 1

    j = BY  # top left
    for i in range(BX - 1, -1, -1):
        j -= 1
        if j < 0:
            break
        threats[i][j] = 1

    j = BY  # top right
    for i in range(BX - 1, -1, -1):
        j += 1
        if j >= N:
            break
        threats[i][j] = 1

    from pprint import pprint
    pprint(threats)

    visited = [[0 for i in range(N)] for j in range(M)]
    steps = bfs(M, N, X, Y, S, T, BX, BY, visited, threats)
    if steps:
        return steps
    return 0


if __name__ == '__main__':
    res = get_kinight_min_steps(M=6, N=6, X=1, Y=3, S=5, T=0, BX=4, BY=2)
    print("res", res)
