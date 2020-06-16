# [BOJ 13458] 시험 감독 : https://www.acmicpc.net/problem/13458
# tag : 구현, 수학, 나머지
# solution by @subinium

if __name__ == '__main__':
    N, A = int(input()), list(map(int, input().split()))
    B, C = map(int, input().split())
    print(N+sum([(a-B+C-1)//C for a in A if a>=B]))