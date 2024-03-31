import random

from parent import *

from libraries import stdarray, stddraw
import percolation

def random_array(n, p):
    '''
    Return a random boolean 2D array
    '''
    is_open = stdarray.create2D(n, n, False)
    
    for i in range(n):
        for j in range(n):
            if random.random() < p:
                is_open[i][j] = True
                
    return is_open

    
def draw(arr, which):
    '''
    Draw the array.
    '''
    n = len(arr)
    stddraw.setXscale(-0.5, n)
    stddraw.setYscale(-0.5, n)
    
    for i in range(n):
        for j in range(n):
            if arr[i][j] == which:
                stddraw.filledSquare(j, n-1-i, 0.45)
                

def main():
    
    n = int(sys.argv[1])
    p = float(sys.argv[2])
    trials = int(sys.argv[3])
    
    for t in range(trials):
        stddraw.clear()
        is_open = random_array(n, p)
        stddraw.setPenColor(stddraw.BLACK)
        draw(is_open, False)
        
        is_full = percolation.flow(is_open)
        stddraw.setPenColor(stddraw.BLUE)
        draw(is_full, True)

        stddraw.show(1000)
        
    stddraw.show()
if __name__ == '__main__':
    main()
    