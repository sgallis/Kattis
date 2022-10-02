# https://open.kattis.com/problems/sumkindofprolem

P = int(input())

for _ in range(P):
    K, N = list(map(int, input().split()))
    print(K, int(N*(N+1)/2), N*(N-1)+N, N*(N+1))