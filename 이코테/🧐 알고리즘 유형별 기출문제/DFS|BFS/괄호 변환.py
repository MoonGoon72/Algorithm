def splitter(p): # 쪼개기
    open_bracket, close_bracket = 0, 0
    u, v = "", ""
    for i in range(len(p)):
        b = p[i]
        if b == "(":
            open_bracket += 1
        else:
            close_bracket += 1
        
        if open_bracket == close_bracket:
            u, v = p[:i + 1], p[i + 1:]
            break
    return [u, v]

def bracket_reversal(u):
    if u == "":
        return u
    s = ""
    for b in u[1:-1]:
        if b == "(":
            s += ")"
        else:
            s += "("
    return s

def is_correct_bracket_string(s): # 올바른 괄호 문자열 확인
    stack = []
    for b in s:
        if b == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                return False
        else:
            stack.append(b)
    return True

def make_correct_bracket_string(p): # 4 수행
    if p == "": 
        return p
    u, v = splitter(p)
    if is_correct_bracket_string(u):
        cv = make_correct_bracket_string(v)
        return u + cv
    else:
        s = "(" + make_correct_bracket_string(v) + ")"
        cu = bracket_reversal(u)
        return s + cu
    
def solution(p):
    answer = make_correct_bracket_string(p)
    return answer