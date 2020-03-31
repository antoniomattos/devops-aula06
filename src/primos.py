# programa python com os numeros primos

def ehprimo(primo):
    for i in range (2, primo+1):
        if i !=primo:
            i = primo % i
            if i ==0:
                return False
                break
        else:
            return True
            break

