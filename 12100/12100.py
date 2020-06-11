# [BOJ 12100] 2048(Easy) : https://www.acmicpc.net/problem/12100
# tag : 구현, DFS
# solution by @subinium

from copy import deepcopy

# 2048판 회전
def rotate90(B, N):
    NB = deepcopy(B)
    for i in range(N):
        for j in range(N):
            NB[j][N-i-1] = B[i][j]
    return NB

# 한줄을 swip했을 때 변화
def convert(lst, N):
    new_list = [i for i in lst if i]
    for i in range(1, len(new_list)):
        if new_list[i-1] == new_list[i]:
            new_list[i-1] *= 2
            new_list[i] = 0
    new_list = [i for i in new_list if i]
    return new_list + [0] * (N-len(new_list))


# dfs로 다음 상태로 옮김
def dfs(N, B, count):
    ret = max([max(i) for i in B])
    if count == 0: return ret
    for _ in range(4):
        X = [convert(i, N) for i in B]
        if X != B: ret = max(ret, dfs(N, X, count-1))
        B = rotate90(B, N)
    return ret

if __name__ == '__main__':
    N = int(input())
    Board = [list(map(int, input().split())) for i in range(N)]
    print(dfs(N, Board, 5))
