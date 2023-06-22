import sys
input = sys.stdin.readline

n = int(input())
result = 0
for _ in range(n):
    word = input()
    err = 0
    for i in range(len(word) - 1):
        if word[i] != word[i+1]:
            new_word = word[i+1:]
            if new_word.count(word[i]) > 0:
                err += 1

    if err == 0: result += 1

print(result)
