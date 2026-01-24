
import sys


def solve():
    x_str = sys.stdin.readline().strip()
    x = int(x_str)
    d = len(x_str)
    y = x * (10**d - 2)
    print(y)

solve()
    
