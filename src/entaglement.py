from qutip import *

print("Entanglement Example: Bell State")

# Two qubits: |00> + |11> / sqrt(2)
bell = (tensor(basis(2,0), basis(2,0)) + tensor(basis(2,1), basis(2,1))).unit()

print("Bell state:\n", bell)

# Measure first qubit
meas_op = [tensor(sigmaz(), qeye(2))]  # Measure Z on first qubit
result = expect(meas_op, bell)
print("Expectation value (correlation):", result)

# To simulate full measurement, you'd use partial trace or more code—expand as practice!