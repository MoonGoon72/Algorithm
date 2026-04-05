def get_substring(value):
    candidates = []
    s = str(value)
    l = len(s)
    for i in range(l):
        count = 1
        while i+count <= l:
            tmp = int(s[i:i+count])
            if tmp != 0:
                candidates.append(tmp)
            count += 1
    return candidates

def main():
    n = int(input())
    dp = [i for i in range(n+1)]

    if n > 9:
        for i in range(10):
            dp[i] = -1
    else:
        for i in range(n+1):
            dp[i] = -1

    for value in range(10, n+1):
        for sub in get_substring(value):
            tmp = value - sub
            if dp[tmp] == -1:
                dp[value] = sub if sub < dp[value] else dp[value]
        dp[value] = -1 if dp[value] == value else dp[value]
    print(dp[n])

if __name__ == '__main__':
    main()