#include <stdio.h>

int main(void){
    int num = 0;
    int n = 1;
    int k = 1;
    int a = 0;
    scanf("%d", &num);
    if (num == 1){
        printf("1\n");
        return 0;
    }
    while (n < num)
    {
        n += 6*a;
        k++;
        if (n >= num){
            printf("%d\n", k -1);
            break;
        }
        a++;
    }
    return 0;
    
}