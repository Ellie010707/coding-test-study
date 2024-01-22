from collections import deque

def findPieces(i, j, op, target):
    global xSize, ySize, visited
    dv = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    queue = deque()
    queue.append((i, j))
    tmp_piece = [(i,j), ]
    while queue:
        x, y = queue.popleft()

        for dx, dy in dv:
            nx = x + dx
            ny = y + dy

            if nx < 0 or nx >= xSize or ny < 0 or ny >= ySize or visited[nx][ny] == 1 or target[nx][ny] != op:
                continue
            tmp_piece.append((nx, ny))
            queue.append((nx, ny))
            visited[nx][ny] = 1
    
    return tmp_piece

def makePiece(piece):
    xs, ys = zip(*piece)
    xSize = max(xs) - min(xs) + 1
    ySize = max(ys) - min(ys) + 1
    xs = [x - min(xs) for x in xs]
    ys = [y - min(ys) for y in ys]
    tmp_piece = [[0 for _ in range(ySize)] for _ in range(xSize)]
    for x, y in zip(xs, ys):
        tmp_piece[x][y] = 1
    return tmp_piece  

def rotate(array_2d):
    list_of_tuples = zip(*array_2d[::-1])
    return [list(e) for e in list_of_tuples]

def getCount(piece):
    count = 0
    for p in piece:
        count += p.count(1)
    return count

def find_block(board, f):
    dv = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    empty_board_list = []
    visited = [[False] * len(board[0]) for _ in range(len(board))]

    for i in range(len(board)):
        for j in range(len(board[i])):
            if not visited[i][j] and board[i][j] == f:
                queue = deque([(i, j)])
                board[i][j] = f ^ 1
                visited[i][j] = True
                lst = [(i, j)]

                while queue:
                    x, y = queue.popleft()
                    for dx, dy in dv:
                        nx, ny = x + dx, y + dy
                        if nx < 0 or nx > len(board) - 1 or ny < 0 or ny > len(board) - 1:
                            continue
                        elif board[nx][ny] == f:
                            queue.append((nx, ny))
                            board[nx][ny] = f ^ 1
                            visited[nx][ny] = True
                            lst.append((nx, ny))
                empty_board_list.append(lst)

    return empty_board_list

def solution(game_board, table):
    global xSize, ySize, visited
    xSize, ySize = len(table), len(table[0])

    answer = 0
    empty_blocks = find_block(game_board, 0)
    puzzles = find_block(table, 1)

    for empty in empty_blocks:
        filled = False
        table = makePiece(empty)

        for puzzle_origin in puzzles:
            if filled == True:
                break

            puzzle = makePiece(puzzle_origin)
            for _ in range(4):
                puzzle = rotate(puzzle)

                if table == puzzle:
                    answer += getCount(puzzle)
                    puzzles.remove(puzzle_origin)
                    filled = True
                    break
    # answer = 0
    # visited = [0 for _ in range(len(table_pieces))]
    # for g in game_pieces:
    #     for idx, t in enumerate(table_pieces):
    #         if visited[idx] == 0 and g in t:
    #             answer += getCount(g)
    #             visited[idx] = 1
    #             break
                    

    return answer

print(solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]], [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]))