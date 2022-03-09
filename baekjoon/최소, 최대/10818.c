#include <stdio.h>
#include <stdlib.h>
void swap(int *a, int *b);

int main(void)
{
    int size;scanf("%d",&size);
    int *numPtr = malloc(sizeof(int) * size);

    for (int i = 0; i < size; i++){
        scanf("%d", &numPtr[i]);
    }

    int max = numPtr[0];
    int min = numPtr[size -1];
    for (int i = 0; i <size; i++){
        if (max < numPtr[i]) max = numPtr[i];
        if (min > numPtr[i]) min = numPtr[i];
    }


    printf("%d %d\n", min, max);
    free(numPtr);
    return 0;
}

void swap(int *a, int *b){
    int bmp = *a;
    *a = *b;
    *b = bmp;
}