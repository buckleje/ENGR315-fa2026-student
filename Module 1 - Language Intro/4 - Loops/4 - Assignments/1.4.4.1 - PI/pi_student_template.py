import math

"""
Use the Gauss-Legendre Algorithm to estimate Pi. Perform 10 approximation loops. Once complete, return the approximation.
:return:
"""

# a variable to hold your returned estimate for PI. When you are done,
# set your estimated value to this variable. Do not change this variable name
pi_estimate = 0

"""
Step 1: Declare and initialize all the values for the Gauss-Legendre algorithm
"""

# starting values for the Gauss-Legendre Algorith
a = 1
b = 1 / (math.sqrt(2))
t = 1/4
p = 1

# perform 10 iterations of this loop
for i in range(1, 11):
    """
    Step 2: Update each variable based upon the algorithm. Take care to ensure
    the order of operations and dependencies among calculations is respected. You
    may wish to create new "temporary" variables to hold intermediate results
    """

    ### YOUR CODE HERE ###
    # calculate new values of each variable using the old values
    a_new = (a + b)/2
    b_new = math.sqrt(a * b)
    t_new = t - p * (a - a_new)**2
    p_new = 2 * p

    # update variables
    a = a_new
    b = b_new
    t = t_new
    p = p_new


    # print out the current loop iteration. This is present to have something in the loop.
    print("Loop Iteration: ", i)

"""
Step 3: After iterating 10 times, calculate the final value for PI
"""

# use the 10th loop values to calculate pi
pi_estimate = ((a + b)**2) / (4 * t)

print("Final estimate for PI: ", pi_estimate) # print final pi calculation
print("Error on estimate: ", abs(pi_estimate - math.pi)) # print the error between estimation and the actual pi value
