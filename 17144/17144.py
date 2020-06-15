# [BOJ 17144] 미세먼지 안녕! : https://www.acmicpc.net/problem/17144
# tag : 구현, 시뮬레이션, 방향벡터
# solution by @subinium
# PyPy3에서 AC, Python3에서 TLE

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

def diffusion(R, C, A):
    add = [[0 for _ in range(C)] for _ in range(R)]
    for x in range(R):
        for y in range(C):
            if A[x][y] < 5: continue
            cnt = 0
            for w in range(4):
                nx, ny = x+dx[w], y+dy[w]
                if 0<=nx<R and 0<=ny<C and A[nx][ny]!=-1: 
                    add[nx][ny] += A[x][y]//5
                    cnt += 1
            A[x][y] -= A[x][y]//5*cnt
    
    for x in range(R):
        for y in range(C): A[x][y] += add[x][y]

def clean(R, C, A, purifier):
    for idx, r in enumerate(purifier):
        Ru, Rd = (0, r+1) if idx==0 else (r, R)
        x, y, way, nxt = r, 0, idx*2, 1+idx*2
        while True:
            nx, ny = x+dx[way], y+dy[way]
            if nx==r and ny==0: break
            if Ru<=nx<Rd and 0<=ny<C : A[x][y], x, y = A[nx][ny], nx, ny
            else : way = (way+nxt)%4
        A[x][y], A[r][0] = 0, -1

def tiktok(R, C, A, purifier):
    diffusion(R, C, A)
    clean(R, C, A, purifier)

if __name__ == '__main__':
    R, C, T = map(int, input().split())
    A  = [list(map(int, input().split())) for _ in range(R)]
    purifier = [idx for idx in range(R) if A[idx][0]==-1]
    for _ in range(T): tiktok(R, C, A, purifier)
    print(sum([sum(row) for row in A])+2)