def switch(x):
    return {
        'a': 1,
        'b': 2,
    }.get(x, 45) # returns the defalut

print(switch('c'))