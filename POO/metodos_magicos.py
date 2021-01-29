class MyClass(object):
    def __str__(self):
        return 'is my class'


obj = MyClass()

print("This " + str(obj))


class MyClass(object):
    def __call__(self):
        print('Hello World!')


obj = MyClass()

obj()


class Person(object):
    def __init__(self, name):
        self.name = name


p = Person('Wallace')

print(p.name)
