#include <stdio.h>
#include <string.h>


int main(void)
{
    int num = 0;
    char arr[51];
    int stack[51] = {
        0,
    };
    int index = 0;
    scanf("%d", &num);
    for (int i = 0; i < num; i++)
    {
        scanf("%s", arr);
        int len = strlen(arr);
        int a = 0;  // 스택을 구현해도 좋으나 입출력을 할 필요는 없기에
        for (int j = 0; j < len; j++)
        {
            if (arr[j] == '(')
            {
                a += 1;
            }
            else if (arr[j] == ')')
            {
                if (a == 0)
                {
                    printf("NO\n");
                    a -= 1;
                    break;
                }
                else
                    a -= 1;
            }

        }
            if (a > 0)
            {
                printf("NO\n");
            }
            else if (a == 0) printf("YES\n");

        a = 0;
    }
        return 0;
}
