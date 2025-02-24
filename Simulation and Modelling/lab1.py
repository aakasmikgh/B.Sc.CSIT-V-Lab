import numpy as np

# Step 1: Generate 100 Random Numbers using Arithmetic Congruential Method
X0, X1 = 7, 11  # Seed values
m = 31  # Modulus value
N = 100  # Number of random numbers

# Initialize the sequence
X = [X0, X1]

# Generate 98 more random integers
for i in range(2, N):
    Xi = (X[i-1] + X[i-2]) % m
    X.append(Xi)

# Compute the random numbers in the range [0,1]
R = [xi / m for xi in X]

# Step 2: Chi-Square Test for Uniformity
n_intervals = 10  # Number of class intervals
intervals = np.linspace(0, 1, n_intervals + 1)

# Count observed frequencies
observed_freq, _ = np.histogram(R, bins=intervals)

# Expected frequency assuming uniform distribution
expected_freq = [N / n_intervals] * n_intervals

# Compute Chi-Square statistic
chi_square_stat = sum(((observed_freq[i] - expected_freq[i]) ** 2) / expected_freq[i] for i in range(n_intervals))

# Critical value from lab sheet
chi_square_critical = 16.9  

# Step 3: Kolmogorov-Smirnov Test
# Sort the random numbers
R_sorted = sorted(R)

# Compute D+ and D-
D_plus = [(i + 1) / N - R_sorted[i] for i in range(N)]
D_minus = [R_sorted[i] - i / N for i in range(N)]

# Determine D_max
D_max = max(max(D_plus), max(D_minus))

# Critical value for KS test
D_critical = 1.36 / np.sqrt(N)

# Display Results
print("Generated Random Numbers:", R[:10], "...")  # Display first 10 as a preview
print("\nChi-Square Test Results:")
print("Observed Frequencies:", observed_freq)
print("Expected Frequency per interval:", expected_freq[0])
print("Chi-Square Statistic:", chi_square_stat)
print("Critical Value:", chi_square_critical)
print("Conclusion:", "Reject H0 (Not Uniform)" if chi_square_stat > chi_square_critical else "Accept H0 (Uniform)")

print("\nKolmogorov-Smirnov Test Results:")
print("D_max:", D_max)
print("Critical Value:", D_critical)
print("Conclusion:", "Reject H0 (Not Uniform)" if D_max > D_critical else "Accept H0 (Uniform)")
