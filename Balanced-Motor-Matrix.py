import numpy as np

# Initialization
S = 12      # Slots number
P = 10      # Pole number
Nph = 3     # Phase number

Ncph = int(S/Nph)       # Slots per phase
Span = np.floor(S/P)    # Coil span
E_angle = 180*P/S       # Electrical angle per slot
Ncpp = S/P/Nph          # Slots per phase per pole

print('Nominal Coil Span =', Span)

# Calculate K0
K0 = np.zeros(int(S/2))
for q in range(int(S/2)):
    # K0[q] = 2*S/3/P*(1+3*q)
    K0[q] = 2*S/Nph/P*(1+Nph*q)
print('Possible K0 =')
print(K0)

# Choose the smallest as K0
K0 = np.min([int(x) for x in np.nditer(K0) if float(x).is_integer()])
print('Choose K0 = ',K0)