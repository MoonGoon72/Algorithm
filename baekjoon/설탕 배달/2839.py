import sys
N = int(input())
sum = int(0)
while (N != 0):
    while (N-5 >=0):
        N-=5
        sum+=1
    if (N !=0):
        while(N%3 !=0):
            N += 5
            sum-=1
            if (sum == -1):
                print(sum)
                sys.exit()
    while (N !=0):
        N -=3
        sum+=1
print(sum)