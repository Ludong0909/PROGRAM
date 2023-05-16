import numpy as np
import sympy as sym

# Set array
Time = np.linspace(0, 320, 17, dtype=float)
Height = np.array([1716.45,1753.47,1791.72,1823.87,1867.08,1895.52,1982.64,2080.91,2198.45,2286.98,2386.01,2460.10,2510.64,2562.53,2619.87,2675.90,2726.54], dtype=float)

# define diff function 
def Two_point_1st (x1, x2 ,y1, y2):
    '''
    Args:
        f: target equation \n
        x1 < x2 \n
        y1 < y2
    Returns:
        diff at x
    '''
    deltax = x1 - x2
    tpc = ((y1) - (y2)) / (deltax)
    return tpc

def Three_point_forward_1st (x1, x2, x3, y1, y2, y3):
    '''
    Args:
        f: target equation \n
        x1 < x2 < x3\n
        y1 < y2 <y3
    Returns:
        diff at x
    '''
    deltax = x2 - x1
    tpf = (-3*y1 + 4*y2 - y3) / (2*deltax)

    return tpf

def Three_point_backward_1st (x1, x2, x3, y1, y2, y3):
    '''
    Args:
        f: target equation \n
        x1 < x2 < x3\n
        y1 < y2 <y3
    Returns:
        diff at x
    '''
    deltax = x2 - x1
    tpb = (y1 - 4*y2 + 3*y3) / (2*deltax)

    return tpb

def Three_point_central_2nd (x1, x2, x3, y1, y2, y3):
    '''
    Args:
        f: target equation \n
        x1 < x2 < x3\n
        y1 < y2 <y3
    Returns:
        diff at x
    '''
    deltax = x1 - x2
    tpc = ((y1) - 2*(y2) + y3) / (deltax)**2
    return tpc

def Three_point_forward_2nd (x1, x2, x3, y1, y2, y3):
    '''
    Args:
        f: target equation \n
        x1 < x2 < x3\n
        y1 < y2 <y3
    Returns:
        diff at x
    '''
    deltax = x2 - x1
    tpf = (y1 - 2*y2 + y3) / (2**deltax)

    return tpf

def Three_point_backward_2nd (x1, x2, x3, y1, y2, y3):
    '''
    Args:
        f: target equation \n
        x1 < x2 < x3\n
        y1 < y2 <y3
    Returns:
        diff at x
    '''
    deltax = x2 - x1
    tpb = (y1 - 2*y2 + y3) / (2**deltax)

    return tpb

def Four_point_forward_2nd (x1, x2, x3, x4, y1, y2, y3, y4):
    '''
    Args:
        f: target equation \n
        x1 < x2 < x3 < x4\n
        y1 < y2 < y3 < y4
    Returns:
        diff at x
    '''
    deltax = x2 - x1
    fpf = (2*y1 - 5*y2 + 4*y3 - y4) / (2**deltax)

    return fpf

def Four_point_backward_2nd (x1, x2, x3, x4, y1, y2, y3, y4):
    '''
    Args:
        f: target equation \n
        x1 < x2 < x3 < x4\n
        y1 < y2 < y3 < y4
    Returns:
        diff at x
    '''
    deltax = x2 - x1
    fpb = (-y1 + 4*y2 - 5*y3 + 2*y4) / (2**deltax)

    return fpb


# Whole array diff 1st and 2nd
def diff_array_1st (X_array, Y_array):
    diff_1st = np.zeros(len(X_array), dtype=float)
    for i in range(len(X_array)-1):
        if i == 0:
            diff_1st[i] = Three_point_forward_1st(X_array[0], X_array[1], X_array[2], Y_array[0], Y_array[1], Y_array[2])
        
        else:
            diff_1st[i] = Two_point_1st(X_array[i-1], X_array[i+1] ,Y_array[i-1], Y_array[i+1])

        diff_1st[len(X_array)-1] = Three_point_backward_1st(X_array[-3], X_array[-2], X_array[-1], Y_array[-3], Y_array[-2], Y_array[-1])

    return (diff_1st)

def diff_array_2nd (X_array, Y_array):
    diff_1st = np.zeros(len(X_array), dtype=float)
    for i in range(len(X_array)-1):
        if i == 0:
            diff_1st[i] = Four_point_forward_2nd(X_array[0], X_array[1], X_array[2], X_array[3], Y_array[0], Y_array[1], Y_array[2], Y_array[3])
        
        else:
            diff_1st[i] = Three_point_central_2nd(X_array[i-1], X_array[i], X_array[i+1] ,Y_array[i-1], Y_array[i], Y_array[i+1])

        diff_1st[len(X_array)-1] = Four_point_backward_2nd(X_array[-4], X_array[-3], X_array[-2], X_array[-1], Y_array[-4], Y_array[-3], Y_array[-2], Y_array[-1])

    return (diff_1st)

# Compute 1st and 2nd diff
v = diff_array_1st(Time, Height)
a = diff_array_2nd(Time, Height)

print(v)
print(a)