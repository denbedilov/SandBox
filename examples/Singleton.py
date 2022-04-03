class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


c1 = Singleton()
c2 = Singleton()
c3 = Singleton()

print(c1)
print(c2)
print(c3)
