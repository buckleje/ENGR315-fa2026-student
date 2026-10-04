import math


def my_pi(target_error):
    """
    Implementation of Gauss–Legendre algorithm to approximate PI from https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_algorithm

    :param target_error: Desired error for PI estimation
    :return: Approximation of PI to specified error bound
    """

    ### YOUR CODE HERE ###

    # starting values for the Gauss-Legendre Algorith
    a = 1
    b = 1 / (math.sqrt(2))
    t = 1/4
    p = 1

    pi_estimate = ((a + b)**2) / (4 * t)    # calculate an initial estimate for pi

    while abs(math.pi - pi_estimate) > target_error:    # while the error is above the target error, recalculate pi

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

        pi_estimate = ((a + b)**2) / (4 * t)    # re-estimate pi

    # return new pi estimate
    return pi_estimate




desired_error = 1E-10

approximation = my_pi(desired_error)

print("Solution returned PI=", approximation)

error = abs(math.pi - approximation)

if error < abs(desired_error):
    print("Solution is acceptable")
else:
    print("Solution is not acceptable")
