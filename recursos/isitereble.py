# Iterável é aquilo que pode ser percorrido item por item

def isiterable(obj):
    try:
        iter(obj)
        return True
    except TypeError: # não é iterável
        return False


print(isiterable('this is an string')) #true
print(isiterable(5)) #false