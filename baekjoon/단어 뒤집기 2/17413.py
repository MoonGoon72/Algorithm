from collections import deque
import sys
input = sys.stdin.readline

txt = str(input().rstrip())

def reverseWord(txt):
    isTag = False
    tag = ""
    word = ""
    result = ""

    for c in txt:
        if c == "<":
            isTag = True
            tag = "<"
            result += word[::-1]
            word = ""
        elif c == ">":
            isTag = False
            tag += ">"
            result += tag
            tag = ""
        else:
            if isTag:
                tag += c
            else:
                if c != " ":
                    word += c
                else:
                    result += word[::-1]
                    word = ""
                    result += " "

    if word != "":
        result += word[::-1]

    return result

print(reverseWord(txt))