from parent import *

from libraries import stdio, stdarray


def _flow(is_open, is_full, i, j):
    n = len(is_open)
    if i < 0 or i >= n or j < 0 or j >= n:
        return
    if not is_open[i][j]:
        return
    if is_full[i][j]:
        return
    is_full[i][j] = True
    _flow(is_open, is_full, i+1, j)
    _flow(is_open, is_full, i-1, j)
    _flow(is_open, is_full, i, j+1)
    _flow(is_open, is_full, i, j-1)
    


def flow(is_open):

    n = len(is_open)
    is_full = stdarray.create2D(n, n, False)
    for j in range(n):
        _flow(is_open, is_full, 0, j)

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