import sys
input = sys.stdin.readline

def drawing(n):
    if n == 3:
        return [
            "  *  ",
            " * * ",
            "*****"
        ]
    
    smaller_triangle = drawing(n // 2)
    top = [" " * (n // 2) + line + " " * (n // 2) for line in smaller_triangle]
    bottom = [line + " " + line for line in smaller_triangle]
    return top + bottom

n = int(input())

result = drawing(n)
print("\n".join(result))