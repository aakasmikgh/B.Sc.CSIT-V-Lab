import random

def monte_carlo_run(num_points=200, seed_val=None):
    
    if seed_val is not None:
        random.seed(seed_val)
        
    # Generate the first four random numbers (we'll use these for display)
    x0 = random.uniform(0, 1)
    x1 = random.uniform(0, 1)
    y0 = random.uniform(0, 1)
    y1 = random.uniform(0, 1)
    
    count_inside = 0
    
    # Check the two points corresponding to (x0, y0) and (x1, y1)
    if x0**2 + y0**2 <= 1:
        count_inside += 1
    if x1**2 + y1**2 <= 1:
        count_inside += 1
    
    # We already generated 4 numbers, so generate the remaining points (each point uses two numbers)
    remaining_points = num_points - 2  # because we've already generated 2 points (each point is one (x,y) pair)
    # Note: We are treating (x0, y0) and (x1, y1) as our first 2 points.
    for _ in range(remaining_points - 0):  # remaining_points equals 200-2 = 198 additional points
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if x**2 + y**2 <= 1:
            count_inside += 1

    # Calculate estimated Pi value
    pi_val = (count_inside / num_points) * 4

    # Return the first four random numbers, count, total points, and estimated Pi
    return (x0, x1, y0, y1, count_inside, num_points, pi_val)

def monte_carlo_table(runs=10, num_points=200):
    results = []
    for run in range(1, runs + 1):
        # Seed the random number generator with the run number for reproducibility
        run_result = monte_carlo_run(num_points=num_points, seed_val=run)
        results.append(run_result)
    return results

def print_table(results):
    header = f"| {'Run':<3} | {'x0':<7} | {'x1':<7} | {'y0':<7} | {'y1':<7} | {'n':<3} | {'N':<3} | {'Pi[i]':<7} |"
    line = "-" * len(header)
    print(line)
    print(header)
    print(line)
    for i, row in enumerate(results, start=1):
        x0, x1, y0, y1, n, N, pi_val = row
        print(f"| {i:<3} | {x0:<7.4f} | {x1:<7.4f} | {y0:<7.4f} | {y1:<7.4f} | {n:<3} | {N:<3} | {pi_val:<7.4f} |")
    print(line)

if __name__ == "__main__":
    # Run the simulation for 10 runs, each with 200 points
    simulation_results = monte_carlo_table(runs=10, num_points=200)
    # Print the results in table format
    print_table(simulation_results)
