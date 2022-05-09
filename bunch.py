class Bunch(dict):
    def __getattribute__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(key)

    def __setattr__(self, key, value):
        self[key] = value

b = Bunch(a=5)
print(b.a)
print(b['a'])
b.a = 8
print(b.a)
b.c = 10
print(b.c)
print(b.d)


