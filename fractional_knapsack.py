# Uses python3
import sys
density = []
def get_optimal_value(capacity, weights, values):
    
    
    V = 0.

    for i in range(n):

        density.append(values[i]/weights[i])

    for i in range(n):

        if capacity == 0:

            return V

        else:
            
            inde = density.index(max(density))
            a = min(weights[inde], capacity)
            V += a*density[inde]           
            capacity -= a
            density[inde] = 0
	    
    return V

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))
    
  
