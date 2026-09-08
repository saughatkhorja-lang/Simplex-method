"""
Computing coursework file: to be completed.
"""

import numpy as np
import simplex_generation
"""
This variable must be updated to your student ID number. 
It is used to create a unique spreadsheet for you, and to link the spreadsheet to your code. 
The spreadsheet will be created in the same location as this file.
"""
student_id = 35737522

## Settings

"""
When you have completed your code, set `run_timings` to `True` so that an Excel workbook is created.
"""

run_timings = True

"""
If you want to create a spreadsheet before you have completed the code, 
set `time_largest_subscript` and `time_largest_change` to `False`. 
You can set just one to `False` if you do not yet want to include that result.
"""

time_largest_subscript = True
time_largest_change = True


## Code for Bland's rule

"""
This code is provided as an example. It works correctly, is fully documented, and will be used later."""

def find_pivot_bland(tableau):
    """
    Using Bland's rule and the minimum ratio test, find the pivot entry in the tableau.
    
    Parameters
    ----------
    tableau : array
        The simplex method tableau in basic form
    
    Returns
    -------
    r, s : integer
        Row and column indexes of the pivot

    Notes
    -----
    Assumes that there is a negative reduced cost that we can pivot on.
    """
    M, N = tableau.shape
    m = M-1  # Number of constraints
    n = N-1  # Number of variables
    # Bland's rule: find first negative reduced cost
    s = 0
    while tableau[-1, s] <= 0:
        s = s + 1
    # Minimum ratio test plus Bland's rule:
    # find the (first) row i minimizing b_i / a_{is}, a_{is} > 0
    r = -1
    theta_star = np.inf
    for i in range(m):
        if tableau[i, s] > 0:
            if tableau[i, -1] / tableau[i, s] < theta_star:
                r = i
                theta_star = tableau[i, -1] / tableau[i, s]
    return r, s


## Code for largest subscript case

"""
This is the first function you must complete.

It needs to return the `(row, column)` indexes `(r, s)` on which the Simplex method will pivot.
 
It needs to be fully and correctly documented.
"""


def find_pivot_largest_subscript(tableau):
    """
    Using the largest subscript rule and the minimum ratio test, find the pivot entry in the tableau.

    Parameters
    ----------
    tableau : array
    The simplex method tableau in basic form

    Returns
    -------
    r, s : integer
    Row and column indexes of the pivot

    Notes
    -----
    Chooses the valid column with the largest index with positive reduced cost,
    then uses the minimum ratio test to choose the pivot row.
    """
    M, N = tableau.shape
    m = M-1  # Number of constraints
    n = N-1  # Number of variables
    #go right to left unlike blands rule
    s = -1
    #scan collumns
    for col in range(n - 1, -1, -1):
        if tableau[-1, col] > 0:
            s = col
            break

    r = -1
    min_ratio = np.inf

    for row in range(m):
        if tableau[row, s] > 0: # validity
            ratio = tableau[row, -1] / tableau[row, s]#finding smallest ratio within constraints. its like limit testing in a way like the gym:p
            if ratio < min_ratio: # use < so it keeps first row index w said ratio if there is a tie
                min_ratio = ratio
                r = row

    return r, s


## Code for largest change case

"""
This is the second function you must complete.

It needs to return the `(row, column)` indexes `(r, s)` on which the Simplex method will pivot.
 
It needs to be fully and correctly documented.
"""


def find_pivot_largest_change(tableau):
    """
    Using the largest change rule and the minimum ratio test, find the pivot entry in the tableau.

    Parameters
    ----------
    tableau : array
    The simplex method tableau in basic form

    Returns
    -------
    r, s : integer
    Row and column indexes of the pivot

    Notes
    -----
    Set final r and final s to -1 at the start to indicate the best column hasnt been found yet.
    Chooses the column that gives the greatest improvement in the
    objective function, then uses the minimum ratio test to choose
    the pivot row.
    """
    M, N = tableau.shape
    m = M - 1
    n = N - 1
    
    largest_change = -np.inf #starts really small
    final_r = -1
    final_s = -1

    for col in range(n): #scan for neg col to improve objective func
        if tableau[-1, col] > 0:#check if i can use col
            row_for_col = -1
            min_ratio = np.inf
            for row in range(m):
                if tableau[row, col] > 0:
                    ratio = tableau[row, -1] / tableau[row, col]

                    if ratio < min_ratio: 
                        min_ratio = ratio
                        row_for_col = row

            if row_for_col != -1: #found valif col
                change = tableau[-1, col] * min_ratio
                if change > largest_change:
                    largest_change = change
                    final_r = row_for_col
                    final_s = col

    r = final_r
    s = final_s

    return r, s



## Code to create the spreadsheet

"""
When you want to create the timings, the following line will do so. 
You need to have modified the "Settings" section above appropriately.

If your code is working you should see the progress bar moving. 
The full case should complete in about a minute if the code is very efficient, 
and within less than 3 minutes even if inefficient. 
The generation code starts with small cases which complete quickly: 
the last few steps will take the longest time. 

If this step freezes for much longer it likely indicates a problem with your code above.
"""

if __name__ == "__main__":
    if run_timings: 
        success = simplex_generation.run_times(student_id,
                                            find_pivot_bland, 
                                            find_pivot_largest_subscript,
                                            find_pivot_largest_change,
                                            time_largest_subscript,
                                            time_largest_change)

