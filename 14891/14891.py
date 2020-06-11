# [BOJ 14891] 톱니바퀴 : https://www.acmicpc.net/problem/14891
# tag : 구현, 모델링
# solution by @subinium
# S, T를 전역변수로 사용하면 구현이 훨씬 깔끔

# 톱니의 회전에 따른 맨꼭대기 변화
def mv(n, lth) : return (n+8+lth)%8

# 재귀적으로 좌/우로 계속 전파
def rotate(kth, cw, p, S, T):
    nxt = kth + p # 보고 있는 톱니의 number
    # 회전해야하는 조건에 따라 회전
    if  0 <= nxt < 4 and S[kth][mv(T[kth], 2*p)] != S[nxt][mv(T[nxt],-2*p)] :
        rotate(nxt, -cw, p, S, T)
    T[kth] = mv(T[kth], -cw) # 한꺼번에 움직이기 위해 마지막에 자신 톱니 회전

# 왼쪽의 톱니 변화와 오른쪽 톱니 변화를 따로 계산
def process(ith, cw, S, T):
    rotate(ith, cw, 1, S, T)
    T[ith] = mv(T[ith], cw)
    rotate(ith, cw, -1, S, T)

if __name__ == '__main__':
    # 초기 톱니와 12시 방향 톱니의 index
    S, T= [input() for i in range(4)], [0, 0, 0, 0]

    # 각 과정별로 진행
    for _ in range(int(input())):
        ith, cw = map(int, input().split())
        process(ith-1, cw, S, T) # ith는 0부터니까
        
    # 12시 방향의 톱니를 문제 조건대로 합 구하는데 사용    
    print(sum([2**i * (int(S[i][T[i]])) for i in range(4)]))
