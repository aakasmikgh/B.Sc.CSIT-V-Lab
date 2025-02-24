#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

#define N 100  // Number of random numbers
#define INTERVALS 10  // Number of class intervals (for Chi-Square test)

// Function to generate 100 random numbers in range [0,1]
void generate_random_numbers(double numbers[]) {
    for (int i = 0; i < N; i++) {
        numbers[i] = (double)rand() / RAND_MAX;
    }
}

// Function to sort numbers in ascending order (Bubble Sort for simplicity)
void sort_numbers(double numbers[]) {
    for (int i = 0; i < N - 1; i++) {
        for (int j = i + 1; j < N; j++) {
            if (numbers[i] > numbers[j]) {
                double temp = numbers[i];
                numbers[i] = numbers[j];
                numbers[j] = temp;
            }
        }
    }
}

// Kolmogorov-Smirnov Test
void kolmogorov_smirnov_test(double numbers[]) {
    sort_numbers(numbers);  // Sort the random numbers first

    double d_plus[N], d_minus[N];
    double d_plus_max = 0.0, d_minus_max = 0.0;

    // Compute D+ and D-
    printf("\nKolmogorov-Smirnov Test Table:\n");
    printf("i\tRandom Number\tF_observed (i/N)\tD+\t\tD-\n");

    for (int i = 0; i < N; i++) {
        double i_n = (double)(i + 1) / N;  // i/N
        double i_minus_1_n = (double)i / N;  // (i-1)/N

        d_plus[i] = i_n - numbers[i];   // D+ = i/N - R_i
        d_minus[i] = numbers[i] - i_minus_1_n;  // D- = R_i - (i-1)/N

        if (d_plus[i] > d_plus_max) d_plus_max = d_plus[i];
        if (d_minus[i] > d_minus_max) d_minus_max = d_minus[i];

        printf("%d\t%.4f\t\t%.4f\t\t%.4f\t%.4f\n", i + 1, numbers[i], i_n, d_plus[i], d_minus[i]);
    }

    // Compute D0 = max(D+ max, D- max)
    double d0 = fmax(d_plus_max, d_minus_max);

    // Compute critical value: D_0.05,100 = 1.36 / sqrt(N)
    double critical_value = 1.36 / sqrt(N);

    printf("\nD+ max = %.4f, D- max = %.4f\n", d_plus_max, d_minus_max);
    printf("D0 = max(D+ max, D- max) = %.4f\n", d0);
    printf("Critical Value (D_0.05,100) = %.4f\n", critical_value);

    // Compare D0 with critical value
    if (d0 < critical_value) {
        printf("Result: The random numbers follow a uniform distribution (Fail to Reject H0)\n");
    } else {
        printf("Result: The random numbers do NOT follow a uniform distribution (Reject H0)\n");
    }
}

// Chi-Square Test
void chi_square_test(double numbers[]) {
    int observed_freq[INTERVALS] = {0};
    double expected_freq = (double)N / INTERVALS;  // E[i] = N/n

    // Count occurrences in each interval
    for (int i = 0; i < N; i++) {
        int index = (int)(numbers[i] * INTERVALS);  // Find interval index
        if (index == INTERVALS) index = INTERVALS - 1;  // Handle edge case
        observed_freq[index]++;
    }

    // Compute Chi-Square test statistic
    double chi_square = 0.0;
    printf("\nChi-Square Test Table:\n");
    printf("Interval\tObserved Freq (O_i)\tExpected Freq (E_i)\t(O_i - E_i)^2 / E_i\n");

    for (int i = 0; i < INTERVALS; i++) {
        double diff = observed_freq[i] - expected_freq;
        double term = (diff * diff) / expected_freq;
        chi_square += term;

        printf("[%0.1f, %0.1f]\t%d\t\t%.2f\t\t%.4f\n", 
                (double)i / INTERVALS, (double)(i + 1) / INTERVALS, 
                observed_freq[i], expected_freq, term);
    }

    // Given critical value: X^2_0.05,9 = 16.9
    double chi_critical = 16.9;

    printf("\nChi-Square Test Statistic: X^2_0 = %.4f\n", chi_square);
    printf("Critical Value (X^2_0.05,9) = %.2f\n", chi_critical);

    // Compare test statistic with critical value
    if (chi_square < chi_critical) {
        printf("Result: The random numbers follow a uniform distribution (Fail to Reject H0)\n");
    } else {
        printf("Result: The random numbers do NOT follow a uniform distribution (Reject H0)\n");
    }
}

int main() {
    double numbers[N];

    // Seed the random number generator
    srand(time(NULL));

    // Generate 100 random numbers
    generate_random_numbers(numbers);

    // Print generated numbers
    printf("Generated Random Numbers:\n");
    for (int i = 0; i < N; i++) {
        printf("%.2f ", numbers[i]);
        if ((i + 1) % 10 == 0) printf("\n");
    }

    // Perform Kolmogorov-Smirnov Test
    kolmogorov_smirnov_test(numbers);

    // Perform Chi-Square Test
    chi_square_test(numbers);

    return 0;
}

