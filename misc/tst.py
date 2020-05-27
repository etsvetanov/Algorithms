class Test():
    a = None
    b = {
        'c': 3
    }

t = Test()

q = t.a and t.b['c']

print('q:', q)