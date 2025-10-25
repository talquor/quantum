import numpy as np
import os
import datetime  # For timestamps
from qutip import * # type: ignore
from qutip.measurement import measure # type: ignore

print("Qubit Basics: Superposition Example")

# Create folder if it doesn't exist
folder = 'bloch_plots'
os.makedirs(folder, exist_ok=True)

# Get unique timestamp
now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Define |0> and |1> basis states
zero = basis(2, 0)  # |0> # type: ignore
one = basis(2, 1)   # |1> # type: ignore

# Superposition: |psi> = (1/sqrt(2))|0> + (1/sqrt(2))|1>
psi = (zero + one).unit()  # .unit() ensures unit norm

print("Superposition state:\n", psi)

# Save pre-measurement Bloch sphere (always the same for this state)
b_pre = Bloch() # type: ignore
b_pre.add_states(psi)
pre_file = os.path.join(folder, f'pre_superposition_{now}.png')
b_pre.save(pre_file)
print(f"Pre-measurement Bloch sphere saved: {pre_file}")

# Measure it (simulate collapse)
outcome, collapsed_state = measure(psi, [zero.proj(), one.proj()])
print(f"Measured outcome: {outcome} (0 or 1 randomly)")
print("Collapsed state after measurement:\n", collapsed_state)

# Save post-measurement Bloch sphere (looks different for 0 vs. 1)
b_post = Bloch() # type: ignore
b_post.add_states(collapsed_state)
post_file = os.path.join(folder, f'post_measurement_outcome-{outcome}_{now}.png')
b_post.save(post_file)
print(f"Post-measurement Bloch sphere saved: {post_file}")
