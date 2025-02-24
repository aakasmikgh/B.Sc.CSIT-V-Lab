import numpy as np

# Define the transition probability matrix P
P = np.array([[0.9, 0.1],  # Coke to Coke, Coke to Pepsi
              [0.2, 0.8]]) # Pepsi to Coke, Pepsi to Pepsi

# Define the initial state vector X_0 (starting with Pepsi)
X_0 = np.array([1, 0])  # [Pepsi, Coke]

# Define the number of steps (third purchase means n=3)
n = 3

# Compute P^n
P_n = np.linalg.matrix_power(P, n)

# Compute X_n = X_0 * P^n
X_n = np.dot(X_0, P_n)

# Display results
print("Transition Probability Matrix (P):")
print(P)
print("\nP^{} (Transition probabilities after {} steps):".format(n, n))
print(P_n)
print("\nProbability distribution after {} purchases (Pepsi, Coke):".format(n))
print(X_n)
