import numpy as np
from qutip import *
from qutip.measurement import measure

print("Qubit Basics: Superposition Example")

# Define |0> and |1> basis states
zero = basis(2, 0)  # |0>
one = basis(2, 1)   # |1>

# Superposition: |psi> = (1/sqrt(2))|0> + (1/sqrt(2))|1>
psi = (zero + one).unit()  # .unit() ensures unit norm

print("Superposition state:\n", psi)

# Measure it (simulate collapse)
measurement = psi.proj()  # Projector, but for actual measurement:
outcome, state = measure(psi, [zero.proj(), one.proj()])
print(f"Measured outcome: {outcome} (0 or 1 randomly)")

# Visualize on Bloch sphere
b = Bloch()
b.add_states(psi)
b.show()  # This will pop up a plot