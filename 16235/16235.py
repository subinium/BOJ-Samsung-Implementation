# [BOJ 16235] 나무 재테크 : https://www.acmicpc.net/problem/16235
# tag : 구현, 시뮬레이션
# solution by @subinium
# PyPy3에서 AC, Python3에서 TLE

from itertools import product

def spring(N, soil, tree):
    die = [[[] for _ in range(N)] for _ in  range(N)]
    for i, j in product(range(N), repeat=2):
        tree[i][j], tmp = [], sorted(tree[i][j])
        for idx, t in enumerate(tmp): 
            if soil[i][j] < t : die[i][j].append(t)
            else :
                tree[i][j].append(t+1)
                soil[i][j] -= t
    return die

def summer(N, soil, die):
    for i, j in product(range(N), repeat=2): 
        soil[i][j] += sum(t//2 for t in die[i][j])

def fall(N, tree):
    dx = [0, 0, 1, 1, 1, -1, -1, -1]
    dy = [1, -1, 0, -1 ,1, 0, -1, 1]
    for i, j in product(range(N), repeat=2):
        for t in tree[i][j]:
            if t % 5 != 0: continue
            for d in range(8):
                ii, jj = i+dx[d], j+dy[d]
                if 0<=ii<N and 0<=jj<N : tree[ii][jj].append(1)

def winter(N, A, soil):
    for i, j in product(range(N), repeat=2): 
        soil[i][j] += A[i][j]

def next_year(N, soil, tree, A):
    die = spring(N, soil, tree)
    summer(N, soil, die)
    fall(N, tree)
    winter(N, A, soil)

if __name__ == '__main__':
    N, M, K = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    soil = [[5 for _ in range(N)] for _ in range(N)]
    tree = [[[] for _ in range(N)] for _ in range(N)]
    for _ in range(M):
        x, y, z = map(int, input().split())
        tree[x-1][y-1].append(z)

    for _ in range(K): next_year(N, soil, tree, A)
    print(sum([len(tree[i][j]) for i, j in product(range(N), repeat=2)]))