#include <stdio.h>

int main(void){
    int number = 1000;
    int arr[1001] = {0, }; 

    for (int i = 2; i <= number; i++){
        if (arr[i]!= -1){  
            for (int j = 2; j <= number / 2; j++){
                if (i * j > number) break;  // index boundary를 넘어가면 안됨
                arr[i * j] = -1;    //i의 배수에 해당하는  index에 -1을 저장
            }
        }
    }

    for (int i = 2; i <= number; i++){
        if (arr[i] == 0){
            printf("%d ", i);
        }
    }
    printf("\n");
    return 0;
}