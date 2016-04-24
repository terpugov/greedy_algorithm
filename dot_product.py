#Uses python3

import sys
#import time 


def min_dot_product(a, b):
#    start = time.time()
    #write your code here
    a.sort()
    b.sort()
    b.reverse()
    res =0
    for i in range(len(a)):
        res += a[i] * b[i]
#    print(time.time()-start)
    return res
	


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print("\n")
    print(min_dot_product(a, b))

