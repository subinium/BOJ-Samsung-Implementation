# [BOJ 14888] 연산자 끼워넣기 : https://www.acmicpc.net/problem/14888
# tag : 재귀, 탐색
# solution by @subinium

from math import ceil
from copy import deepcopy
from operator import add, sub, mul, truediv

mn, mx = 1e10, -1e10

def f(A, idx, res, op_num):
    global mn, mx # 전역변수 사용
    if sum(op_num) == 0: 
        mx = max(res, mx)
        mn = min(res, mn)
        return
    for i, op in zip(range(4), [add, sub, mul, truediv]):
        if op_num[i] == 0: continue
        op_num_tmp = deepcopy(op_num)
        op_num_tmp[i]-=1
        f(A, idx+1, int(op(res, A[idx])), op_num_tmp)

if __name__ == '__main__':
    N, A = int(input()), list(map(int, input().split()))
    op = list(map(int, input().split()))
    f(A, 1, A[0], op)
    print(mx, mn)