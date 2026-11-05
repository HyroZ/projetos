/*Criando matriz com dimensões 5x5*/

int main() {
    int matriz[5][5];

    for (int i = 0; i < 5; i++) {
        for(int j = 0; j < 5; j++) {
           if (i == j) {
            matriz[i][j] = 1;
           } 
           else {
            matriz[i][j] = 0;
           }
    }
}

printf("Matriz identidade 5x5:\n");
for (int i = 0; i < 5; i++) {
    for(int j = 0; j < 5; j++) {
            printf("%d ", matriz[i][j]);
        }
        printf("\n");
    }

    return 0;
}