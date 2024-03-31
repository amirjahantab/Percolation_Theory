from parent import *

from libraries import stdio, stdarray

def flow(is_open):
    # vertical percolation
    n = len(is_open)
    is_full = stdarray.create2D(n, n, False)
    
    for j in range(n):
        is_full[0][j] = is_open[0][j]
        
    for i in range(1, n):
        for j in range(n):
            is_full[i][j] = is_open[i][j] and is_full[i-1][j]

    return is_full

def percolates(is_open):
    n = len(is_open)
    is_full = flow(is_open)
    
    for j in range(n):
        if is_full[n-1][j]:
            return True
        
    return False


def main():
    is_open = stdarray.readBool2D()
    stdarray.write2D(flow(is_open))
    stdio.writeln(percolates(is_open))
    

if __name__ == '__main__':
    main()