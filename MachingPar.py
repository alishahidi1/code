# from collections import deque
def matchpar (str):
    List_of_pars = []
    for char in str:
        if char == "(":
            List_of_pars.append(char)
        elif char == ")":
            if not List_of_pars:
                return False
            List_of_pars.pop()
    return len(List_of_pars) == 0 

print("I like that") 

print(matchpar("(Alish)"))
print(matchpar("(Alish)())"))
