import sys
input = sys.stdin.readline



while True:
    str = input().rstrip()

    if (str == '0'):
        break

    reverseStr = str[::-1]
    if(str == reverseStr):
        print('yes')
    else:
        print('no')
