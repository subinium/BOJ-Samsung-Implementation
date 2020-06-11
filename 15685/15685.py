# [BOJ 15685] 드래곤 커브 : https://www.acmicpc.net/problem/15685
# tag : 구현, 기하, 재귀
# solution by @subinium

# 재귀적으로 드래곤 커브 방향 구하기
# 미리 path를 dict로 만들 수 있지만 큰 성능향상 없음
def curv_path(d, g):
    if g == 0 : return [d]
    ret = curv_path(d, g-1)
    return  ret + [(i+1)%4 for i in ret[::-1]]

# x, y에서 시작하는 드래곤 커브 그리기
# curv_path의 방향을 바탕으로 생성
def dragon_path(cord, x, y, d, g):
    dx, dy = [1, 0, -1, 0], [0, -1, 0, 1] # 방향벡터
    cord[x][y] = 1
    for w in curv_path(d, g):
        x, y = x+dx[w], y+dy[w]
        cord[x][y] = 1

# 특정 점에서 4점을 살펴 정사각형 확인
def count_square(cord):
    ret = 0
    for i in range(100):
        for j in range(100):
            ret += sum([cord[i+x//2][j+x%2] for x in range(4)]) == 4
    return ret

if __name__ == '__main__':
    N = int(input())
    params = [map(int, input().split()) for _ in range(N)] # x, y, d, g를 튜플로 받기
    cord = [[0 for _ in range(101)] for _ in range(101)] # 격자판
    for param in params: dragon_path(cord, *param) # dragon curve별로 그리기
    print(count_square(cord)) 