#include <stdio.h>
#include <string.h>

#define KEY_SIZE 7
int key_order[KEY_SIZE] = {4, 3, 1, 2, 5, 6, 7};

void rail_fence_encrypt(char *plaintext, char *ciphertext) {
    int len = strlen(plaintext);
    char matrix[KEY_SIZE][len];
    memset(matrix, 0, sizeof(matrix));
    
    int row = 0;
    for (int col = 0; col < len; col++) {
        matrix[row][col] = plaintext[col];
        row = (row + 1) % KEY_SIZE;
    }
    
    int index = 0;
    for (int i = 0; i < KEY_SIZE; i++) {
        int actual_row = key_order[i] - 1;
        for (int col = 0; col < len; col++) {
            if (matrix[actual_row][col] != 0) {
                ciphertext[index++] = matrix[actual_row][col];
            }
        }
    }
    ciphertext[index] = '\0';
}

int main() {
    char plaintext[100], ciphertext[100];
    printf("Enter the plaintext: ");
    fgets(plaintext, sizeof(plaintext), stdin);
    plaintext[strcspn(plaintext, "\n")] = 0; // Remove newline character
    
    rail_fence_encrypt(plaintext, ciphertext);
    printf("Ciphertext: %s\n", ciphertext);
    
    return 0;
}
