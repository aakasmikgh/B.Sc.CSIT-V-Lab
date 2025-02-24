# Initial base values (from the previous year, e.g., 2022)
Y_base = 80   # National income for the base year
G_base = 20   # Government expenses for the base year

print("Year |    I    |    T    |    G    |     C    |     Y")
print("---------------------------------------------------------")

# Calculate parameters for the next 5 years (e.g., 2023 to 2027)
for year in range(2023, 2023 + 5):
    I = 2 + 0.1 * Y_base
    T = 0.2 * Y_base
    G = 1.15 * G_base  # Increase government expenses by 15%
    C = 45.45 + 2.27 * (I + G)
    Y = C + I + G
    
    # Print values in the order I, T, G, C, Y
    print(f"{year} | {I:7.2f} | {T:7.2f} | {G:7.2f} | {C:8.2f} | {Y:8.2f}")
    
    # Update base values for the next iteration
    Y_base = Y
    G_base = G
