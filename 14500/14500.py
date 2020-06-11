# [BOJ 14500] 테트로미노 : https://www.acmicpc.net/problem/14500
# tag : 구현, 전수조사
# solution by @subinium
# PyPy3에서 AC, Python3에서 TLE

# 테트로미노 90도 회전 
def rotate(A):
    n, m = len(A), len(A[0])
    ret = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(n):
        for j in range(m):
            ret[j][n-i-1] = A[i][j]
    return ret

# 테트로미노 뒤집기
def flip(A): 
    return [row[::-1] for row in A]

# 테트로미노 모양 내의 숫자 합
def ck(A, i, j):
    n, m = len(A), len(A[0])
    if i+n > N or j+m > M: return -1
    # 반복문으로 구하면 더 빠름
    return sum([A[ii][jj] * P[i+ii][j+jj] for ii in range(n) for jj in range(m)]) 

if __name__ == '__main__':
    N, M = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    # 기본 테트로미노
    T = [[[1, 1, 1, 1]], [[1, 1], [1, 1]], [[1, 0, 0], [1, 1, 1]], [[1, 1, 0], [0, 1, 1]], [[0, 1, 0], [1, 1, 1]]]
    # 모든 테트로미노 배열 만들기
    NT = []
    for block in T[:]:
        for f in range(2): 
            if f : block = flip(block)
            for r in range(4): 
                if r : block = rotate(block)
                NT.append(block)

    # 모든 덮는 경우 확인
    print(max([max([ck(block, i, j) for i in range(N) for j in range(M)]) for block in NT]))
