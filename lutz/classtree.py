"""
classtree.py: подъем по деревям наследования с применением связи
между пространствами имен и отображением находящихся выше суперклассов
с отступом согласно высоте
"""


def classtree(cls, indent):
    print('.' * indent + cls.__name__)
    for supercls in cls.__bases__:
        classtree(supercls, indent + 3)


def instancetree(inst):
    print('Tree of %s' % inst)
    classtree(inst.__class__, 3)

def selftest():
    class A: pass
    class B(A): pass
    class C(A) : pass
    class D(B, C): pass
    class E: pass
    class F(D, E): pass
    instancetree(B())
    instancetree(F())

if __name__ == '__main__':
    selftest()