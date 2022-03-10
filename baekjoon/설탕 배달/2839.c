#include <stdio.h>

int main(void)
{
    int kg = 0;
    scanf("%d",&kg);  //설탕의 총 무게

    int count = 0;
    while (kg > 3){
        if (kg % 5 == 0){
            printf("%d\n", count + kg / 5);
            return 0;
        }
// 4, 7 등 예외 일반화 해야함
        kg -= 3;
        count++;
    }
    printf("%d\n", count);

    return 0;
}