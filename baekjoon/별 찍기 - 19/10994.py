import sys
input = sys.stdin.readline

def drawing(n):
    if n == 1:
        return "*"
    
    smaller_rectangle = drawing(n-1)
    top = ["*" * (1 + 4 * (n - 1)), "*" + " " * (4 * (n - 1) - 1) + "*"]
    middle = ["* " + line + " *" for line in smaller_rectangle]
    bottom = list(reversed(top))
    return top + middle + bottom

n = int(input())
result = drawing(n)
print("\n".join(result))