import numpy as np
from tabulate import tabulate

def estimate_pi(num_samples=10000, num_iterations=10):
    results = []
    pi_values = []

    for i in range(num_iterations):
        x0 = np.random.uniform(-1, 1, num_samples)
        y0 = np.random.uniform(-1, 1, num_samples)
        x1, y1 = np.random.uniform(-1, 1), np.random.uniform(-1, 1)  # Single random points
        inside_circle = np.sum(x0**2 + y0**2 <= 1)  # Count points inside the circle
        pi_estimate = (inside_circle / num_samples) * 4
        pi_values.append(pi_estimate)

        results.append([
            i + 1, round(x1, 4), round(y1, 4), round(x0[0], 4), round(y0[0], 4), 
            round(inside_circle, 4), round(num_samples, 4), round(pi_estimate, 4)
        ])

    mean_pi = round(np.mean(pi_values), 4)
    error_percentage = round(abs((mean_pi - np.pi) / np.pi) * 100, 4)

    return results, mean_pi, error_percentage

num_samples = 10000
num_iterations = 10
results, mean_pi, error = estimate_pi(num_samples, num_iterations)

results.append(["Mean π", "-", "-", "-", "-", "-", "-", mean_pi])
results.append(["Error %", "-", "-", "-", "-", "-", "-", f"{error:.4f}%"])

# Print table with 4 decimal places
headers = ["Iteration", "x1", "y1", "x0", "y0", "n (Inside)", "N (Total)", "π Estimate"]
print(tabulate(results, headers, tablefmt="grid", floatfmt=".4f"))
