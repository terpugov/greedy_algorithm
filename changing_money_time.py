# Uses python3
import time
m = int(input())
#start = time.time()
def change_money(m):
    c1 = 1
    c5 = 5
    c10 = 10
    count = 0
    condition = True
    while m != 0:
        while m>=c10:
            m = m - c10
            count = count + 1
        while  m>=c5:
            m = m - c5
            count = count + 1
        while m>=c1:
            m = m-c1
            count = count + 1
    return count
a = change_money(m)
print(a)
#print(time.time()-start)
