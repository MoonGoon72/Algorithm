import sys
import copy
input = sys.stdin.readline

col, row = map(int, input().split())
originalGraph = [list(map(str, input().rstrip())) for _ in range(col)]
mini = list()
for i in range(col - 7):
    for j in range(row - 7):
        case1 = 0  #처음이 Black인 경우
        case2 = 0  #처음이 White인 경우
        graph = copy.deepcopy(originalGraph)
        for k in range(i,i+8):  #col
            for l in range(j,j+8):  #row
                if((k+l)%2 == 0):
                    if(graph[k][l] == 'B'):
                        case1+=1
                    else:
                        case2+=1
                else:
                    if(graph[k][l] == 'W'):
                        case1+=1
                    else:
                        case2+=1
        mini.append(case1)
        mini.append(case2)
print(min(mini))
