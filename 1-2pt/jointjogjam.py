# https://open.kattis.com/contests/pzmq28/problems/jointjogjam

from math import hypot

x_k,y_k,x_o,y_o,x_k_end,y_k_end,x_o_end,y_o_end = map(int,input().split())

print(max(hypot(x_k-x_o,y_k-y_o),hypot(x_k_end-x_o_end,y_k_end-y_o_end)))