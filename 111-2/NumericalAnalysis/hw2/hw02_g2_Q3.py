import numpy as np
import NAFunc as nf

# Define the variables W, P, and T
W = 0.01
P = 1000
T = 300

# Define the function f(Tc)
def f(Tc):
    # Set the values of the variables used in the function
    w = W
    p0 = P
    T0 = T
    ep = 0.622
    A = 2.53*10**9
    B = 5420
    kp = 7/2
    # Calculate the value of the function and return it
    ans = Tc - B/np.log(((A*ep)/(w*p0))*(T0/Tc)**kp)
    return ans

# Set the tolerance and initial guesses
TOL = 1*10**(-6)
x1 = 1
x2 = 400

# Call the BracketRoot() function from the NAFunc module to find the root
Tc = nf.BracketRoot(f=f, target=0, x1=x1, x2=x2, Tolerance=TOL)

# Print the condensation temperature
print("The condensation temperature is:", Tc, "K")


# Explanation of f(Tc):
# The function f(Tc) calculates the value of the left-hand side of the Clausius-Clapeyron equation, which relates the pressure 
# and temperature of a gas to the amount of water vapor that can be held in the air. In this case, the function is being used 
# to determine the condensation temperature, which is the temperature at which water vapor begins to condense into liquid 
# water. The function is defined in terms of several constants and variables, including the saturation vapor pressure, the 
# gas constant for water vapor, and the latent heat of vaporization. Because the function is hard to be solved analytically, 
# it must be solved numerically using a method such as bisection.