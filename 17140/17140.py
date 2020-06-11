# [BOJ 17140] 이차원 배열과 연산 : https://www.acmicpc.net/problem/17140
# tag : 구현, 조건문
# solution by @subinium

from collections import Counter

# 0-padding transpose
def rotate(A, r, c):
    ret = [[0 for _ in range(r)] for _ in range(c)]
    for i, row in enumerate(A):
        for j, val in enumerate(row): ret[j][i] = val
    return ret

# R 연산
def process(row):
    counter = Counter(row) # Counter로 쉽게 카운팅 
    del counter[0]
    ret, tmp = [], sorted([(cnt, val) for val, cnt in counter.items()])
    for i in range(min(50, len(tmp))): ret += tmp[i][::-1] # 개수 제한에 따라 설정
    return ret

if __name__ == '__main__':
    # 초기 상태 정의
    r, c, k = map(int, input().split())
    r, c = r-1, c-1 # r, c는 각각 0-based로
    A = [list(map(int, input().split())) for _ in range(3)]

    ans, flip = -1, False
    for t in range(101):
        rp, cp = len(A), max([len(row) for row in A])
        if rp > r and len(A[r]) > c and A[r][c] == k: 
            ans = t
            break
        
        # R연산만 하기 위해 R < C인 경우, 행렬 회전
        if rp < cp or (rp==cp and flip): 
            flip ^= True
            A = rotate(A, rp, cp)
            rp, cp, r, c = cp, rp, c, r
        
        # R연산
        A = [process(row) for row in A]
        
    print(ans)