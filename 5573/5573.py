# [BOJ 5573] 큐빙 : https://www.acmicpc.net/problem/5373
# tag : 구현, 기하
# solution by @subinium

# ufl : 큐브별로 UFL 회전시 각면이 바라보는 방향 변화
# cw : 시계방향으로 돌리는 경우 3 * 3에서 변화되는 내용
ufl, cw = ['015423', '452310', '320145'], '258147036'

# 3 * 3 * 3에서 한 변을 뽑는 방법
# 한 변의 숫자는 반드시 순서대로 등차수열임을 활용


def side_(ith, st, a, b):
    return [st+a*(i % 3)+b*(i//3)-1 for i in range(9)]


# UDFBLR 순서에서 각 변을 얻기 위한 상수값 사용
side = [side_(i, *stab) for i, stab in enumerate([(1, 1, 3),
                                                  (19, 3, 1), (7, 1, 9), (1, 9, 1), (1, 3, 9), (3, 9, 3)])]

# 기존의 배치에서 바뀐 부분만 재배치
# a, st, ed : 배열, 기존위치, 바뀐위치


def realign(a, st, ed):
    ret = a[:]
    for s, e in zip(st, ed):
        ret[int(e)] = a[int(s)]
    return ret

# 한 변을 돌리는 함수 / 큐브의 위치와 상태 변경
# 시계방향 또는 반시계방향 중 하나만 정의 => 반시계 == 시계*3


def rotate(op, pos, state):
    idx, ccw = 'UDFBLR'.index(op[0]), op[1]  # 변확인 및 시계/반시계 방향 확인
    blocks = side[idx]  # 볼 변의 번호들만 선택
    # 큐브의 위치 변경
    for i in range(1+(ccw == '+')*2):
        blocks = realign(blocks, range(9), cw)
    pos = realign(pos, side[idx], blocks)

    # 큐브의 상태 변경
    for i in range(1+((ccw == '+') ^ (idx % 2))*2):
        for j in range(9):  # 한변당 큐브의 개수 9개
            state[pos[blocks[j]]] = realign(
                state[pos[blocks[j]]], range(6), ufl[idx//2])

    return pos, state

# 초기 상태 pos, state 정의
# pos[i] : 매 상태에서 3 * 3 * 3에서 순서대로 넘버링했을 때, i번쨰 큐브의 번호
# state[i] : 초기 i번 큐브의 상태


def init():
    pos, state = [i for i in range(27)], [
        [0 for _ in range(6)] for i in range(27)]
    for idx, col in enumerate('wyrogb'):
        for block in side[idx]:
            state[block][idx] = col
    return pos, state

# 각 과정별 함수


def process():
    N = input()
    # 회전 별로 pos, state 변경
    pos, state = init()  # 초기화
    for order in input().split():
        pos, state = rotate(order, pos, state)

    # 윗면 큐브들에서 위만 출력
    for i, idx in enumerate(side[0]):
        print(state[pos[idx]][0], end=''+(i % 3 == 2)*'\n')


# Main 함수
if __name__ == '__main__':
    # 테스트 케이스 별 과정 진행
    TC = int(input())
    for _ in range(TC):
        process()
