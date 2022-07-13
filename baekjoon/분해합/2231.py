num = int(input())

for i in range(1, num+1):
    a = list(map(int, str(i)))
    s = i + sum(a)
    if(s == num):
        print(i)
        break
else:
    print(0)
