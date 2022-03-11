#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int isPrime (int x);

int main(void)
{
    int size =0;
    int num = 0;
    int arr[101] = {2, 3, };
    int d = 2;
    scanf("%d",&size);
    int *numPtr = malloc(sizeof(int) * size);

    for (int i =0; i < size; i++){
        scanf("%d",&numPtr[i]);
    }
    for (int i = 0; i<size; i++){
        num += isPrime(numPtr[i]);
        
    }

    printf("%d\n", num);

    free(numPtr);
    return 0;
}

int isPrime (int x){
    if (x == 1) return 0;
    int num = (int)sqrt(x);  // 특정 수의 제곱근 까지만 약수를 구하면 됨
    for (int i = 2; i <= num; i++){
        
        if (x % i == 0){
            return 0;
        }
    }
    return 1;
}