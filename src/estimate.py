from parent import *
from libraries import stdio
import percolationIO
import percolation

def evaluate(n, p, trials):
    '''
    Evaluate the probability of percolation.
    '''
    count = 0
    for t in range(trials):
        is_open = percolationIO.random_array(n, p)
        if percolation.percolates(is_open):
            count += 1
        
    return 1.0 * count / trials

def main():
    n = int(sys.argv[1])
    p = float(sys.argv[2])
    trials = int(sys.argv[3])
    
    q = evaluate(n, p, trials)
    stdio.writeln(q)

 
if __name__ == '__main__':
    main()