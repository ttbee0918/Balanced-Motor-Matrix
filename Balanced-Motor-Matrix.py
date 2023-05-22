import numpy as np

# Initialization
S = 12      # Slots number
P = 10      # Pole number
Nph = 3     # Phase number

Check = np.zeros((S,P), dtype=bool)
for S in range(2,S):
    for P in range(2,P): 
        # Calculate K0
        K0 = np.zeros(int(S/2))
        for q in range(int(S/2)):
            K0[q] = 2*S/Nph/P*(1+Nph*q)
        print('S, P, K0 =', S, P, K0)

        # Check any int in K0
        Any_int = any(float(x).is_integer() for x in np.nditer(K0))
        # print('Any_int = ',Any_int)
        
        Check[S-1,P-1] = Any_int
print('Check = ')
print(Check)