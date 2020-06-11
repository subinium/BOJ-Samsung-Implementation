# [BOJ 16236] 아기 상어 : https://www.acmicpc.net/problem/16236
# tag : 구현, BFS/DFS, 탐색
# solution by @subinium

from collections import deque

# bfs (너비우선탐색)
# 매순간 가장 가까운 물고기와 거리와 위치 반환
def bfs(x, y, A):
    dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]
    ck = [[0 for _ in range(N)] for _ in range(N)]
    ans, q = (1e9, -1, -1), deque([(0, x, y)])
    while len(q):
        d, x, y = q.popleft()
        if ck[x][y]: continue
        ck[x][y] = 1
        if 0 < A[x][y] < sz: ans = min(ans, (d, x, y))
        for w in range(4):
            xx, yy = x+dx[w], y+dy[w]
            # 배열을 벗어나지 않으며 자기보다 작거나 같은 물고기 빈 곳 + 가보지 않은 곳
            if 0 <= xx < N and 0 <= yy < N and not ck[xx][yy] and A[xx][yy] <= sz: 
                q.append((d+1, xx, yy))
    return ans if ans[0] != 1e9 else (0, -1, -1)


if __name__ == '__main__':
    N = int(input()) # 
    A = [list(map(int, input().split())) for _ in range(N)] # 초기 물고기 배열
    sz, eat, t = 2, 0, 0 # 초기 상어 사이즈, 먹은 물고기 수, 시간

    # 초기 상어 위치
    for idx, r in enumerate(A):
        if 9 in r: x, y = idx, r.index(9)

    # 먹을 수 없을 때까지 반복
    A[x][y] = 0
    while True:
        d, x, y = bfs(x, y, A)
        if x == -1: break
        t, eat = t+d, eat+1
        A[x][y] = 0
        if eat == sz: sz, eat = sz+1, 0

    print(t)
