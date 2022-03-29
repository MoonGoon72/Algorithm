#include <stdio.h>

int main(void){

    int n = 0, m = 0;
    scanf("%d %d", &n, &m);
    int num[101] = {0, };
    for (int i = 0; i <n; i++){
        scanf("%d",&num[i]);
    }
    int max = 0;
    for (int i =0; i <n -2; i++){
        for (int j = i+1; j< n-1; j++){
            for (int k = j+1; k< n; k++){
                
                int sum = num[i] + num[j] + num[k];
                if (sum > max && sum <= m) {
                    max = sum;
                }
            }
        }
    }
    printf("%d",max);


    return 0;
}