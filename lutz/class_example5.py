class rec: pass


rec.name = 'Bob'
rec.age = 40
print(rec.name)

y = rec()
x = rec()

print(x.name, y.name)

x.name = 'Sue'
print(rec.name, x.name, y.name)
print([name for name in rec.__dict__ if not name.startswith('__')])

# print(x.__dict__['age'])

print(x.__class__)

print(rec.__bases__)  # Вывод связей с суперклассом


def uppername(obj):
    return obj.name.upper()


print(uppername(x))

rec.method = uppername
print(x.method())
print(y.method())
print(rec.method(x))

rec = ('Bob', 40.5, ['dev', 'mgr'])
print(rec[0])

rec = {}
rec['name'] = 'Bob'
rec['age'] = 40.5
rec['jobs'] = ['dev', 'mgr']

print(rec['name'])


class rec: pass


rec.name = 'Bob'
rec.age = 40.5
rec.jobs = ['dev', 'mgr']

print(rec.name)


class Person:
    def __init__(self, name, jobs, age=None):
        self.name = name
        self.jobs = jobs
        self.age = age

    def info(self):
        return (self.name, self.jobs)


rec1 = Person('Bob', ['dev', 'mgr'], 40.5)
rec2 = Person('Sue', ['dev', 'cto'])

print(rec1.jobs, rec2.info())

