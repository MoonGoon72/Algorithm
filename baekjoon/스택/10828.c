#include <stdio.h>
#include <string.h>


void push(int x);
void pop();
int size();
int isEmpty();
int top();

int main(void){
    int stack[10001] = {0, };
    int n = 0;
    scanf("%d", &n); //명령의 개수
    char commend[7];
    int index = 0;  
    int num = 0;
    
    for (int i = 0; i <n; i++){
        scanf("%s", commend);
        if (!strcmp(commend, "push")){
            scanf("%d",&num);
            stack[index++] = num;
        }else if (!strcmp(commend, "pop")){
            if (index == 0){
                printf("-1\n");
            }else printf("%d\n", stack[--index]);
            stack[index] = 0;
        }else if (!strcmp(commend, "size")){
            if (index == 0){
                printf("0\n");
            } else printf("%d\n", index);
        }else if (!strcmp(commend, "empty")){
            if (index == 0 && stack[index] == 0){

                printf("1\n");
            } else printf("%d\n", 0);
        }else if (!strcmp(commend, "top")){
            if (index == 0){

                printf("-1\n");
            } else printf("%d\n", stack[index -1]);
        } else printf("잘못 입력하셨습니다.\n");
    }

    return 0;
}